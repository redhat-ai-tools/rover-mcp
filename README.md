# Rover MCP Server

MCP (ModelContextProvider) server for querying Red Hat internal groups API using client certificate authentication.

## Features

- **rover_group**: Retrieve information about Red Hat internal groups by name
- Client certificate authentication for secure API access
- Proper error handling for common scenarios (404, 403, certificate issues)

## Prerequisites

- Client certificate (`sa-cert.crt`) and private key (`privkey.pem`) files
- Access to Red Hat internal groups API

## Building locally

To build the container image locally using Podman, run:

```sh
podman build -t rover-mcp:latest .
```

This will create a local image named `rover-mcp:latest` that you can use to run the server.

## Running with Podman or Docker

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "rover": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v", "./sa-cert.crt:/app/sa-cert.crt:ro",
        "-v", "./privkey.pem:/app/privkey.pem:ro",
        "-e", "CERT_FILE=/app/sa-cert.crt",
        "-e", "KEY_FILE=/app/privkey.pem",
        "-e", "MCP_TRANSPORT=stdio",
        "localhost/rover-mcp:latest"
      ],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

## Tools

### rover_group

Retrieve information about a Red Hat internal group.

**Parameters:**
- `group_name` (string, required): The name of the group to retrieve information for

**Example usage:**
```bash
# Using the equivalent curl command that this tool replicates:
curl -H "Accept: application/json" --cert sa-cert.crt --key privkey.pem \
  -X GET https://internal-groups.iam.redhat.com/v1/groups/<group-name-test>
```

**Returns:**
- Success: Group information as JSON
- Error cases:
  - Group not found (404)
  - Access denied (403)
  - Certificate file missing
  - Other HTTP errors

## Environment Variables

- `CERT_FILE`: Path to the client certificate file (default: `sa-cert.crt`)
- `KEY_FILE`: Path to the private key file (default: `privkey.pem`)
- `MCP_TRANSPORT`: Transport method for MCP communication (default: `stdio`)

## Local Development

1. Ensure you have the required certificate files in the project directory
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python mcp_server.py`

## Security Notes

- Keep certificate and private key files secure
- Never commit certificate files to version control
- Use read-only volume mounts when running in containers
