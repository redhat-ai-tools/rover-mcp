# Rover MCP Server

Red Hat internal groups (rover) MCP server that provides access to internal group information and member data.

## Architecture

This MCP server focuses specifically on Red Hat internal groups (rover) data. For JIRA project analysis, use the separate JIRA MCP server alongside this one. The LLM can choose which tools to use based on the query requirements.

## Available Tools

- `rover_group(group_name)` - Get information about a specific Red Hat internal group
- `get_comprehensive_member_profile(member_id)` - Get member profile with rover group context
- `rover_integration_help()` - Get help and integration guidance

## Setup

1. **Prerequisites:**
   - Valid Red Hat certificates (`sa-cert.crt` and `privkey.pem`)
   - Python 3.8+
   - Required dependencies (`pip install -r requirements.txt`)

2. **Configuration:**
   Add both rover and JIRA MCP servers to your MCP configuration:

```json
{
  "mcpServers": {
    "rover": {
      "command": "python3",
      "args": ["/path/to/rover-mcp/mcp_server.py"],
      "cwd": "/path/to/rover-mcp",
      "env": {
        "MCP_TRANSPORT": "stdio",
        "CERT_FILE": "sa-cert.crt",
        "KEY_FILE": "privkey.pem"
      }
    },
    "jira-snowflake": {
      "command": "python3", 
      "args": ["/path/to/jira-mcp-snowflake/mcp_server.py"],
      "cwd": "/path/to/jira-mcp-snowflake",
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

## Usage Examples

### Rover Group Analysis
```
rover_group('sp-ai-support-chatbot')
```

### Combined Analysis Workflow
1. Use `rover_group()` to get group information
2. Use JIRA MCP tools (`list_jira_issues()`, `get_jira_project_summary()`) for project data  
3. LLM combines results for comprehensive analysis

### Member Profile
```
get_comprehensive_member_profile('member-id')
```

## Integration Benefits

- **Clean Separation**: Each MCP server handles its domain expertise
- **LLM Choice**: The assistant can choose appropriate tools for each query
- **Better Reliability**: No complex internal MCP-to-MCP calls
- **Error Handling**: Each server handles its own errors independently

## Development

Run the server:
```bash
python3 mcp_server.py
```

Test with the MCP client:
```bash
python3 test_client.py
```
