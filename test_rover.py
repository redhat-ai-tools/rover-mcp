#!/usr/bin/env python3
"""
Simple test script to call the rover_group function directly.
"""
import asyncio
import sys
from mcp_server import rover_group, get_user_by_uid, get_user_groups, get_groups, get_group_owners

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

async def test_endpoints():
    """Test the various rover endpoints."""
    
    print("Testing rover_group with: exd-guild-distribution")
    print("Querying group: exd-guild-distribution")
    result = await rover_group("exd-guild-distribution")
    print(f"Result: {result}")
    print("\n" + "="*50 + "\n")
    
    # Test get_groups (list groups)
    print("Testing get_groups (first 5 groups)")
    result = await get_groups(limit=5, offset=0)
    print(f"Result: {result}")
    print("\n" + "="*50 + "\n")
    
    # Test get_group_owners
    print("Testing get_group_owners for: exd-guild-distribution")
    result = await get_group_owners("exd-guild-distribution")
    print(f"Result: {result}")
    print("\n" + "="*50 + "\n")
    
    # Get a user ID from the previous group result to test user endpoints
    # Using 'rbikar' who was shown as an owner in the test above
    print("Testing get_user_by_uid with: rbikar")
    result = await get_user_by_uid("rbikar")
    print(f"Result: {result}")
    print("\n" + "="*50 + "\n")
    
    print("Testing get_user_groups with: rbikar")
    result = await get_user_groups("rbikar")
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(test_endpoints()) 