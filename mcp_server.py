import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("rover")

# Red Hat internal groups API base URL
API_BASE_URL = "https://internal-groups.iam.redhat.com/v1"

# Certificate paths
CERT_FILE = os.environ.get("CERT_FILE", "sa-cert.crt")
KEY_FILE = os.environ.get("KEY_FILE", "privkey.pem")


async def make_authenticated_request(
    url: str, method: str = "GET", data: dict[str, Any] = None
) -> dict[str, Any] | None:
    """Make an authenticated request using client certificates."""
    headers = {
        "Accept": "application/json",
    }

    # Verify certificate files exist
    if not os.path.exists(CERT_FILE):
        raise FileNotFoundError(f"Certificate file not found: {CERT_FILE}")
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError(f"Private key file not found: {KEY_FILE}")

    async with httpx.AsyncClient(
        cert=(CERT_FILE, KEY_FILE),
        verify=False  # Disable SSL verification for internal APIs
    ) as client:
        if method.upper() == "GET":
            response = await client.request(method, url, headers=headers, params=data)
        else:
            response = await client.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def rover_group(group_name: str) -> dict[str, Any]:
    """
    Retrieve information about a Red Hat internal group.
    
    Args:
        group_name: The name of the group to retrieve information for
        
    Returns:
        Group information from the Red Hat internal groups API
    """
    if not group_name:
        raise ValueError("group_name is required")
    
    url = f"{API_BASE_URL}/groups/{group_name}"
    try:
        response = await make_authenticated_request(url)
        return response
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return {"error": f"Group '{group_name}' not found"}
        elif e.response.status_code == 403:
            return {"error": f"Access denied for group '{group_name}'"}
        else:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except FileNotFoundError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


@mcp.tool()
async def get_comprehensive_member_profile(member_id: str) -> dict[str, Any]:
    """
    Get complete member profile including rover groups and basic member information.
    For JIRA data, use the separate JIRA MCP server tools.
    
    Args:
        member_id: The Red Hat ID of the member to analyze
        
    Returns:
        Member profile with rover groups and basic information
    """
    if not member_id:
        raise ValueError("member_id is required")
    
    # Get rover groups that include this member
    # Note: This would require searching across groups or having a member->groups API
    # For now, we'll return a basic structure that focuses on rover data only
    
    formatted_response = {
        "member_id": member_id,
        "formatted_summary": format_member_profile_summary(member_id),
        "raw_data": {
            "rover_groups": [],  # Would need to implement group search by member
            "note": "Use JIRA MCP server tools for JIRA project data"
        },
        "integration_note": "This tool provides rover group data only. Use separate JIRA MCP server for JIRA analysis."
    }
    
    return formatted_response


def format_member_profile_summary(member_id: str) -> str:
    """Format the member profile summary focusing on rover data."""
    
    summary = f"""🏢 **Rover Group Analysis for {member_id}**

**Group Memberships:**
To get complete group membership information, you can:
1. Use the rover_group tool if you know specific group names
2. Use the separate JIRA MCP server tools for JIRA project involvement

**Next Steps:**
- Use rover_group('group-name') to check specific groups
- Use JIRA MCP tools (list_jira_issues, get_jira_project_summary) for project analysis
- Combine results from both MCP servers for comprehensive analysis

**Architecture Note:**
This rover MCP focuses on Red Hat internal groups data.
JIRA analysis is handled by the separate JIRA MCP server.
The LLM can choose which tools to use based on the query."""
    
    return summary


@mcp.tool()
async def rover_integration_help() -> dict[str, Any]:
    """
    Get help information about the rover MCP server and integration with other MCP servers.
    
    Returns:
        Help and usage information for rover tools and integration guidance
    """
    return {
        "rover_mcp_server": {
            "description": "Red Hat internal groups (rover) data access",
            "available_tools": [
                {
                    "name": "rover_group",
                    "description": "Get Red Hat internal group information",
                    "usage": "rover_group('group-name')"
                },
                {
                    "name": "get_comprehensive_member_profile", 
                    "description": "Get member profile with rover group context",
                    "usage": "get_comprehensive_member_profile('member-id')",
                    "note": "Focuses on rover data only - use JIRA MCP for project data"
                }
            ],
            "architecture": {
                "purpose": "Dedicated to Red Hat internal groups (rover) data",
                "integration": "Works alongside separate JIRA MCP server",
                "benefits": [
                    "Clean separation of concerns",
                    "LLM can choose appropriate tools",
                    "No complex internal MCP-to-MCP calls",
                    "Better error handling and reliability"
                ]
            },
            "jira_integration": {
                "approach": "Use separate JIRA MCP server",
                "jira_tools": [
                    "list_jira_issues(search_text='member-id')",
                    "get_jira_issue_details(issue_key='KEY-123')",
                    "get_jira_project_summary()",
                    "list_jira_components(project='PROJECT')"
                ],
                "combined_workflow": [
                    "1. Use rover_group to get group information",
                    "2. Use JIRA tools to get project involvement",
                    "3. LLM combines results for comprehensive analysis"
                ]
            },
            "examples": {
                "get_group_info": "rover_group('sp-ai-support-chatbot')",
                "member_profile": "get_comprehensive_member_profile('member-id')",
                "combined_analysis": "Use both rover and JIRA MCP tools together"
            }
        }
    }


if __name__ == "__main__":
    mcp.run(transport=os.environ.get("MCP_TRANSPORT", "stdio"))
