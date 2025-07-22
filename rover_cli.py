#!/usr/bin/env python3
"""
Rover CLI - Command line interface for querying Red Hat internal groups.
"""
import asyncio
import argparse
import json
import sys
from mcp_server import rover_group

async def query_group(group_name: str, output_format: str = "table"):
    """Query a group and format the output."""
    try:
        result = await rover_group(group_name)
        
        if "error" in result:
            print(f"Error: {result['error']}", file=sys.stderr)
            return False
            
        if output_format == "json":
            print(json.dumps(result, indent=2))
        elif output_format == "table":
            print_group_table(result)
        else:
            print(f"Unknown format: {output_format}", file=sys.stderr)
            return False
            
        return True
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False

def print_group_table(group_data):
    """Print group information in a readable table format."""
    print(f"\n🏢 Group: {group_data.get('name', 'N/A')}")
    print(f"📝 Description: {group_data.get('description', 'N/A')}")
    print(f"👤 Owner: {', '.join([owner['id'] for owner in group_data.get('owners', [])])}")
    print(f"📧 Contact: {group_data.get('contactList', 'N/A')}")
    print(f"✅ Approval Type: {group_data.get('memberApprovalType', 'N/A')}")
    
    members = group_data.get('members', [])
    print(f"\n👥 Members ({len(members)} total):")
    print("-" * 50)
    
    for i, member in enumerate(members, 1):
        print(f"{i:2d}. {member['id']} ({member['type']})")

def main():
    parser = argparse.ArgumentParser(
        description="Query Red Hat internal groups via Rover API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s exd-guild-distribution          # Query a specific group
  %(prog)s my-group --format json         # Output as JSON
  %(prog)s --interactive                   # Interactive mode
        """
    )
    
    parser.add_argument("group_name", nargs="?", help="Name of the group to query")
    parser.add_argument("--format", "-f", choices=["table", "json"], default="table",
                       help="Output format (default: table)")
    parser.add_argument("--interactive", "-i", action="store_true",
                       help="Interactive mode - prompt for group names")
    
    args = parser.parse_args()
    
    if args.interactive:
        print("🚀 Rover Interactive Mode")
        print("Enter group names to query (Ctrl+C to exit)")
        try:
            while True:
                group_name = input("\nGroup name: ").strip()
                if not group_name:
                    continue
                asyncio.run(query_group(group_name, args.format))
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)
    elif args.group_name:
        success = asyncio.run(query_group(args.group_name, args.format))
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 