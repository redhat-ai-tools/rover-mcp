#!/usr/bin/env python3

import asyncio
import os

# Set the environment variables BEFORE importing the module
os.environ["API_BASE_URL"] = "https://internal-groups.iam.redhat.com/v1"
os.environ["CERT_PATH"] = os.path.expanduser("~/iam-csr/serviceaccount/sa-cert.crt")
os.environ["KEY_PATH"] = os.path.expanduser("~/iam-csr/serviceaccount/privkey.pem")

from mcp_server import get_groups

async def test_get_groups():
    """Test the get_groups function directly"""
    print("Testing get_groups for 'dno-integration-dev'...")
    try:
        result = await get_groups("dno-integration-dev")
        print("Result:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_get_groups()) 