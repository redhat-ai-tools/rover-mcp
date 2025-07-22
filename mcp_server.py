import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-server")

API_BASE_URL = os.environ["API_BASE_URL"]
CERT_PATH = os.environ.get("CERT_PATH")
KEY_PATH = os.environ.get("KEY_PATH")


async def make_request(
    url: str, method: str = "GET", data: dict[str, Any] = None
) -> dict[str, Any] | None:

    headers = {}

    try:
        async with httpx.AsyncClient(cert=(CERT_PATH, KEY_PATH)) as client:
            if method.upper() == "GET":
                response = await client.request(
                    method, url, headers=headers, params=data
                )
            else:
                response = await client.request(
                    method, url, headers=headers, json=data
                )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


@mcp.tool()
async def get_groups(group_name: str = "dno-jenkins"):
    """Get information about a specific group.
    
    Args:
        group_name: Name of the group to retrieve information for
    """
    url = f"{API_BASE_URL}/groups/{group_name}"
    try:
        response = await make_request(url)
        return response
    except Exception as e:
        return {"error": f"Failed to retrieve group information: {str(e)}"}


if __name__ == "__main__":
    mcp.run(transport=os.environ.get("MCP_TRANSPORT", "stdio"))
