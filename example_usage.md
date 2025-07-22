# Example: Analyzing a Red Hat Member with Multiple MCP Servers

This example demonstrates how the LLM uses both the rover MCP and JIRA MCP servers independently to provide comprehensive analysis.

## Scenario
User asks: *"Can you analyze the member 'jdoe' and tell me about their group memberships and project involvement?"*

## Step 1: Get Rover Group Information

**LLM calls rover MCP:**
```json
{
  "tool": "get_comprehensive_member_profile",
  "parameters": {
    "member_id": "jdoe"
  }
}
```

**Rover MCP Response:**
```json
{
  "member_id": "jdoe",
  "formatted_summary": "🏢 **Rover Group Analysis for jdoe**\n\n**Group Memberships:**\nTo get complete group membership information, you can:\n1. Use the rover_group tool if you know specific group names\n2. Use the separate JIRA MCP server tools for JIRA project involvement\n\n**Next Steps:**\n- Use rover_group('group-name') to check specific groups\n- Use JIRA MCP tools (list_jira_issues, get_jira_project_summary) for project analysis\n- Combine results from both MCP servers for comprehensive analysis",
  "raw_data": {
    "rover_groups": [],
    "note": "Use JIRA MCP server tools for JIRA project data"
  },
  "integration_note": "This tool provides rover group data only. Use separate JIRA MCP server for JIRA analysis."
}
```

## Step 2: Check Specific Groups

**LLM calls rover MCP to check likely groups:**
```json
{
  "tool": "rover_group",
  "parameters": {
    "group_name": "platform-engineering"
  }
}
```

**Rover MCP Response:**
```json
{
  "name": "platform-engineering",
  "description": "Platform Engineering Team",
  "members": [
    {"id": "jdoe", "role": "member"},
    {"id": "asmith", "role": "owner"},
    {"id": "bwilson", "role": "member"}
  ],
  "owners": ["asmith"],
  "membership_type": "approval_required"
}
```

## Step 3: Get JIRA Project Involvement

**LLM calls JIRA MCP:**
```json
{
  "tool": "list_jira_issues",
  "parameters": {
    "search_text": "jdoe",
    "limit": 50
  }
}
```

**JIRA MCP Response:**
```json
{
  "issues": [
    {
      "key": "PLAT-1234",
      "project": "PLAT",
      "summary": "Implement monitoring dashboard for platform services",
      "status": "In Progress",
      "assignee": "jdoe",
      "created": "2024-01-15T10:30:00Z"
    },
    {
      "key": "INFRA-5678", 
      "project": "INFRA",
      "summary": "Upgrade Kubernetes cluster to v1.29",
      "status": "Done",
      "assignee": "jdoe",
      "created": "2024-01-10T14:20:00Z"
    },
    {
      "key": "DEVOPS-9012",
      "project": "DEVOPS", 
      "summary": "Setup CI/CD pipeline for microservices",
      "status": "Code Review",
      "reporter": "jdoe",
      "created": "2024-01-08T09:15:00Z"
    }
  ],
  "total": 3,
  "metadata": {
    "search_term": "jdoe",
    "projects_involved": ["PLAT", "INFRA", "DEVOPS"]
  }
}
```

## Step 4: Get Project Summaries

**LLM calls JIRA MCP for project context:**
```json
{
  "tool": "get_jira_project_summary",
  "parameters": {
    "random_string": "dummy"
  }
}
```

**JIRA MCP Response:**
```json
{
  "projects": {
    "PLAT": {
      "name": "Platform Engineering",
      "total_issues": 1247,
      "open_issues": 89
    },
    "INFRA": {
      "name": "Infrastructure Operations", 
      "total_issues": 2156,
      "open_issues": 156
    },
    "DEVOPS": {
      "name": "DevOps Automation",
      "total_issues": 987,
      "open_issues": 67
    }
  }
}
```

## Final LLM Analysis

**Combined Response:**
```markdown
# Member Analysis: jdoe

## 🏢 Rover Group Memberships
- **platform-engineering**: Member (approval-required group)
  - Owner: asmith
  - 3 total members
  - Indicates trusted access to platform engineering initiatives

## 📊 JIRA Project Involvement

**Active Projects (3 projects, 3+ issues):**

### Platform Engineering (PLAT)
- **Current Work**: Implement monitoring dashboard for platform services (PLAT-1234) - In Progress
- **Role**: Technical contributor and implementer
- **Project Scale**: 1,247 total issues, 89 currently open

### Infrastructure Operations (INFRA)  
- **Recent Achievement**: Upgraded Kubernetes cluster to v1.29 (INFRA-5678) - Completed
- **Role**: Infrastructure specialist
- **Project Scale**: 2,156 total issues, 156 currently open

### DevOps Automation (DEVOPS)
- **Initiative**: Setup CI/CD pipeline for microservices (DEVOPS-9012) - Code Review
- **Role**: Process initiator and designer
- **Project Scale**: 987 total issues, 67 currently open

## 🎯 Profile Summary

**jdoe** is a trusted platform engineering team member with active involvement across critical infrastructure projects. His rover group membership aligns perfectly with his JIRA activity, showing consistent focus on:

- **Platform Monitoring & Observability**
- **Infrastructure Management & Upgrades** 
- **DevOps Process Automation**

**Activity Level**: High - actively working across 3 major platform projects with both implementation and leadership responsibilities.

**Technical Focus**: Full-stack platform engineering from infrastructure to monitoring to automation pipelines.
```

## Architecture Benefits Demonstrated

1. **Clean Data Sources**: Rover provides authoritative group data, JIRA provides project activity
2. **LLM Orchestration**: The assistant automatically chose which tools to use for each data type
3. **Independent Servers**: Each MCP server handled its domain without complex integrations
4. **Rich Analysis**: Combined data provides comprehensive member understanding
5. **Error Isolation**: If one server fails, the other continues working

## Configuration Used

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

This approach gives you the best of both worlds: specialized MCP servers with clean separation of concerns, and intelligent LLM orchestration for comprehensive analysis. 