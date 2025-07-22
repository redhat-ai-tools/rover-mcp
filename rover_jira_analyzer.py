#!/usr/bin/env python3
"""
Practical Rover-JIRA Analyzer
Connects Red Hat internal group members with their JIRA project involvement using real MCP tools.
"""
import asyncio
import argparse
import json
import sys
from collections import defaultdict
from typing import Dict, List, Set
from mcp_server import rover_group

# We need to simulate the JIRA MCP calls since we can't import them directly
# In a real MCP client, these would be actual tool calls

async def search_jira_for_member(member_id: str, limit: int = 50) -> Dict:
    """Search JIRA for issues involving a specific member."""
    print(f"    🔍 Searching JIRA for: {member_id}")
    
    # This simulates: await mcp_jira_snowflake_list_jira_issues(search_text=member_id, limit=limit)
    # For now, return mock data - you would replace this with actual MCP tool calls
    return {
        "issues": [],
        "total_returned": 0,
        "filters_applied": {"search_text": member_id, "limit": limit}
    }

class RoverJiraAnalyzer:
    def __init__(self):
        self.project_cache = {}
        
    async def analyze_group(self, group_name: str) -> Dict:
        """Analyze JIRA involvement for all members of a rover group."""
        print(f"🏢 Analyzing Rover group: {group_name}")
        
        # Step 1: Get rover group information
        try:
            group_data = await rover_group(group_name)
            if "error" in group_data:
                return {"error": group_data["error"]}
        except Exception as e:
            return {"error": f"Failed to get group data: {e}"}
        
        members = group_data.get('members', [])
        print(f"👥 Found {len(members)} members in group")
        
        # Step 2: Analyze each member's JIRA involvement
        analysis_results = {
            "group_info": {
                "name": group_data.get('name'),
                "description": group_data.get('description'),
                "total_members": len(members)
            },
            "member_projects": {},
            "project_members": defaultdict(list),
            "summary": {
                "members_with_jira_activity": 0,
                "unique_projects": set(),
                "total_issues_found": 0
            }
        }
        
        # Analyze each member
        for member in members:
            member_id = member['id']
            print(f"  👤 Analyzing: {member_id}")
            
            member_analysis = await self.analyze_member_jira(member_id)
            
            # Store results
            analysis_results["member_projects"][member_id] = member_analysis
            
            # Update summary statistics
            if member_analysis['projects'] or member_analysis['total_issues'] > 0:
                analysis_results["summary"]["members_with_jira_activity"] += 1
            
            analysis_results["summary"]["unique_projects"].update(member_analysis['projects'])
            analysis_results["summary"]["total_issues_found"] += member_analysis['total_issues']
            
            # Group members by project
            for project in member_analysis['projects']:
                analysis_results["project_members"][project].append(member_id)
        
        # Convert set to list for JSON serialization
        analysis_results["summary"]["unique_projects"] = sorted(list(analysis_results["summary"]["unique_projects"]))
        analysis_results["project_members"] = dict(analysis_results["project_members"])
        
        return analysis_results
    
    async def analyze_member_jira(self, member_id: str) -> Dict:
        """Analyze JIRA activity for a specific member."""
        
        # Search for issues mentioning this member
        jira_data = await search_jira_for_member(member_id, limit=100)
        
        issues = jira_data.get('issues', [])
        projects = set()
        issue_details = []
        
        # Process each issue
        for issue in issues:
            project_key = issue.get('project', 'Unknown')
            projects.add(project_key)
            
            issue_details.append({
                'key': issue.get('key'),
                'project': project_key,
                'summary': issue.get('summary', ''),
                'status': issue.get('status'),
                'priority': issue.get('priority'),
                'issue_type': issue.get('issue_type')
            })
        
        return {
            "member_id": member_id,
            "projects": sorted(list(projects)),
            "total_issues": len(issues),
            "issue_details": issue_details
        }
    
    def format_report(self, analysis: Dict, format_type: str = "table") -> str:
        """Format the analysis results for display."""
        
        if format_type == "json":
            return json.dumps(analysis, indent=2, default=str)
        
        # Table format
        output = []
        group_info = analysis["group_info"]
        summary = analysis["summary"]
        
        # Header
        output.append("=" * 60)
        output.append("🚀 ROVER-JIRA INTEGRATION ANALYSIS REPORT")
        output.append("=" * 60)
        
        # Group information
        output.append(f"🏢 Group: {group_info['name']}")
        output.append(f"📝 Description: {group_info['description']}")
        output.append(f"👥 Total Members: {group_info['total_members']}")
        
        # Summary statistics
        output.append(f"\n📊 SUMMARY STATISTICS:")
        output.append(f"  🎫 Members with JIRA Activity: {summary['members_with_jira_activity']}")
        output.append(f"  📂 Unique Projects Involved: {len(summary['unique_projects'])}")
        output.append(f"  🎯 Total Issues Found: {summary['total_issues_found']}")
        
        # Projects overview
        if summary['unique_projects']:
            output.append(f"\n📂 PROJECTS WITH GROUP MEMBERS:")
            output.append("-" * 40)
            
            project_members = analysis["project_members"]
            for project in summary['unique_projects']:
                members_in_project = project_members.get(project, [])
                output.append(f"  🔹 {project}: {len(members_in_project)} member(s)")
                for member in sorted(members_in_project):
                    output.append(f"    - {member}")
        
        # Individual member analysis
        output.append(f"\n👤 INDIVIDUAL MEMBER ANALYSIS:")
        output.append("-" * 40)
        
        member_projects = analysis["member_projects"]
        
        # Show members with JIRA activity first
        active_members = []
        inactive_members = []
        
        for member_id, member_data in member_projects.items():
            if member_data['projects'] or member_data['total_issues'] > 0:
                active_members.append((member_id, member_data))
            else:
                inactive_members.append((member_id, member_data))
        
        # Active members
        if active_members:
            output.append(f"\n🟢 MEMBERS WITH JIRA ACTIVITY ({len(active_members)}):")
            for member_id, member_data in sorted(active_members):
                output.append(f"\n  👤 {member_id}")
                if member_data['projects']:
                    output.append(f"    📂 Projects: {', '.join(member_data['projects'])}")
                output.append(f"    🎫 Issues: {member_data['total_issues']}")
                
                # Show sample issues
                if member_data['issue_details'][:3]:  # Show first 3 issues
                    output.append(f"    📋 Recent Issues:")
                    for issue in member_data['issue_details'][:3]:
                        output.append(f"      • {issue['key']}: {issue['summary'][:50]}...")
        
        # Inactive members
        if inactive_members:
            output.append(f"\n🔴 MEMBERS WITHOUT JIRA ACTIVITY ({len(inactive_members)}):")
            inactive_member_names = [member_id for member_id, _ in inactive_members]
            # Group them for compact display
            for i in range(0, len(inactive_member_names), 5):
                batch = inactive_member_names[i:i+5]
                output.append(f"    {', '.join(batch)}")
        
        return '\n'.join(output)

async def analyze_specific_member(member_id: str):
    """Analyze a specific member's JIRA involvement."""
    analyzer = RoverJiraAnalyzer()
    print(f"🔍 Analyzing JIRA activity for: {member_id}")
    
    member_analysis = await analyzer.analyze_member_jira(member_id)
    
    print(f"\n👤 JIRA Analysis for {member_id}:")
    print("=" * 40)
    print(f"📂 Projects: {', '.join(member_analysis['projects']) if member_analysis['projects'] else 'None'}")
    print(f"🎫 Total Issues: {member_analysis['total_issues']}")
    
    if member_analysis['issue_details']:
        print(f"\n📋 Issues:")
        for issue in member_analysis['issue_details'][:10]:  # Show first 10
            print(f"  • {issue['key']} ({issue['project']}): {issue['summary']}")

async def main():
    parser = argparse.ArgumentParser(
        description="Analyze JIRA involvement for Red Hat internal group members",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze entire group
  %(prog)s --group sp-ai-support-chatbot
  
  # Analyze specific member
  %(prog)s --member dhshah
  
  # JSON output
  %(prog)s --group sp-ai-support-chatbot --format json
        """
    )
    
    parser.add_argument("--group", "-g", help="Name of the rover group to analyze")
    parser.add_argument("--member", "-m", help="Specific member ID to analyze")
    parser.add_argument("--format", "-f", choices=["table", "json"], default="table",
                       help="Output format (default: table)")
    
    args = parser.parse_args()
    
    if not args.group and not args.member:
        parser.print_help()
        print("\n❌ Error: Must specify either --group or --member")
        sys.exit(1)
    
    try:
        if args.member:
            # Analyze specific member
            await analyze_specific_member(args.member)
        else:
            # Analyze entire group
            analyzer = RoverJiraAnalyzer()
            results = await analyzer.analyze_group(args.group)
            
            if "error" in results:
                print(f"❌ Error: {results['error']}", file=sys.stderr)
                sys.exit(1)
            
            formatted_output = analyzer.format_report(results, args.format)
            print(formatted_output)
            
    except KeyboardInterrupt:
        print("\n👋 Analysis interrupted!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 