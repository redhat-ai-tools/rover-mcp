#!/usr/bin/env python3
"""Simple debug script to test MCP server startup."""

import os
import subprocess
import json

def test_server_startup():
    """Test if the MCP server can start without errors."""
    print("Testing MCP server startup...")
    
    # Check certificate files
    cert_file = "sa-cert.crt"
    key_file = "privkey.pem"
    
    if not os.path.exists(cert_file):
        print(f"❌ Certificate file not found: {cert_file}")
        return False
    
    if not os.path.exists(key_file):
        print(f"❌ Key file not found: {key_file}")
        return False
        
    print(f"✅ Certificate files found")
    
    # Test if server can start
    try:
        env = os.environ.copy()
        env["MCP_TRANSPORT"] = "stdio"
        env["CERT_FILE"] = cert_file
        env["KEY_FILE"] = key_file
        
        process = subprocess.Popen(
            ["python3", "mcp_server.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env
        )
        
        # Send simple initialize request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "debug", "version": "1.0"}
            }
        }
        
        request_json = json.dumps(init_request) + "\n"
        
        # Send request and wait for response
        stdout, stderr = process.communicate(input=request_json, timeout=5)
        
        if stderr:
            print(f"❌ Server stderr: {stderr}")
            return False
            
        if stdout:
            print(f"✅ Server responded: {stdout.strip()}")
            return True
        else:
            print("❌ No response from server")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Server timeout")
        process.kill()
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_server_startup()
    print(f"\nMCP Server Test: {'✅ PASSED' if success else '❌ FAILED'}") 