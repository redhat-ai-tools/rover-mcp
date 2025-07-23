#!/usr/bin/env python3
"""
Simple test script to call the rover_group function directly.
"""
import asyncio
import os
from mcp_server import rover_group

async def test_rover_group(group_name: str):
    """Test the rover_group function with a specific group name."""
    print(f"Querying group: {group_name}")
    try:
        result = await rover_group(group_name)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    group_name = "exd-guild-distribution"
    print(f"Testing rover_group with: {group_name}")
    result = asyncio.run(test_rover_group(group_name)) 