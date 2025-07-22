# mcp-server for Rover api

MCP (ModelContextProvider) server template

---

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
    "mcp-server": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "API_BASE_URL",
        "-e", "MCP_TRANSPORT",
        "localhost/rover-mcp:latest"
      ],
      "env": {
        "API_BASE_URL": "https://internal-groups.iam.redhat.com/v1",
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```
# Manual steps to test

```
python3 -m venv venv
source venv/bin/activate && pip install -r requirements.txt

source venv/bin/activate && python test_client.py
```
# To Check if mcp server is already running

```
ps aux | grep mcp_server.py
```