#!/usr/bin/env python3
"""
Rover-JIRA Integration Tool
Connects Red Hat internal group members with their JIRA project involvement.
"""
import asyncio
import argparse
import json
import sys
from collections import defaultdict
from typing import Dict, List, Set
from mcp_server import rover_group

# Mock the JIRA MCP functions for now - in real usage these would be MCP calls
async def list_jira_issues(search_text: str = None, limit: int = 50) -> Dict:
    """Mock function - replace with actual MCP call to jira-mcp-snowflake"""
    # This would be: await mcp_jira_snowflake_list_jira_issues(search_text=search_text, limit=limit)
    print(f"🔍 Searching JIRA for: {search_text}")
    return {"issues": [], "total": 0}

async def get_jira_project_summary() -> Dict:
    """Mock function - replace with actual MCP call"""
    # This would be: await mcp_jira_snowflake_get_jira_project_summary()
    return {"projects": {}}

class RoverJiraIntegrator:
    def __init__(self):
        self.member_projects = defaultdict(set)
        self.member_issues = defaultdict(list)
        
    async def analyze_group_jira_involvement(self, group_name: str, detailed: bool = False) -> Dict:
        """Analyze JIRA involvement for all members of a rover group."""
        print(f"🏢 Analyzing group: {group_name}")
        
        # Get rover group information
        try:
            group_data = await rover_group(group_name)
            if "error" in group_data:
                return {"error": group_data["error"]}
        except Exception as e:
            return {"error": f"Failed to get group data: {e}"}
        
        print(f"👥 Found {len(group_data.get('members', []))} members")
        
        # Analyze each member's JIRA involvement
        results = {
            "group_info": group_data,
            "member_analysis": {},
            "project_summary": defaultdict(list),
            "stats": {
                "total_members": len(group_data.get('members', [])),
                "members_with_jira_activity": 0,
                "unique_projects": set(),
                "total_issues_found": 0
            }
        }
        
        for member in group_data.get('members', []):
            member_id = member['id']
            print(f"🔍 Analyzing JIRA activity for: {member_id}")
            
            member_analysis = await self.analyze_member_jira_activity(
                member_id, detailed=detailed
            )
            
            if member_analysis['projects'] or member_analysis['issues']:
                results['stats']['members_with_jira_activity'] += 1
            
            results['member_analysis'][member_id] = member_analysis
            results['stats']['unique_projects'].update(member_analysis['projects'])
            results['stats']['total_issues_found'] += len(member_analysis['issues'])
            
            # Group by projects
            for project in member_analysis['projects']:
                results['project_summary'][project].append(member_id)
        
        # Convert set to list for JSON serialization
        results['stats']['unique_projects'] = list(results['stats']['unique_projects'])
        
        return results
    
    async def analyze_member_jira_activity(self, member_id: str, detailed: bool = False) -> Dict:
        """Analyze JIRA activity for a specific member."""
        analysis = {
            "member_id": member_id,
            "projects": [],
            "issues": [],
            "roles": set(),
            "activity_summary": {}
        }
        
        # Search for issues involving this member
        # In real implementation, you would use the actual MCP calls here
        print(f"  📋 Searching JIRA issues for {member_id}...")
        
        # Mock searches - replace with actual JIRA MCP calls
        search_patterns = [
            f"assignee:{member_id}",
            f"reporter:{member_id}",
            f"creator:{member_id}",
            member_id  # General search
        ]
        
        for pattern in search_patterns:
            try:
                # Replace with: await mcp_jira_snowflake_list_jira_issues(search_text=pattern, limit=100)
                issues_data = await list_jira_issues(search_text=pattern, limit=100)
                
                for issue in issues_data.get('issues', []):
                    analysis['issues'].append({
                        'key': issue.get('key'),
                        'project': issue.get('project'),
                        'summary': issue.get('summary'),
                        'status': issue.get('status'),
                        'role': self.determine_role(issue, member_id, pattern)
                    })
                    
                    if issue.get('project'):
                        analysis['projects'].append(issue['project'])
                        
            except Exception as e:
                print(f"    ❌ Error searching with pattern '{pattern}': {e}")
        
        # Remove duplicates and count
        analysis['projects'] = list(set(analysis['projects']))
        analysis['roles'] = list(analysis['roles'])
        
        if detailed:
            analysis['activity_summary'] = self.create_activity_summary(analysis['issues'])
        
        return analysis
    
    def determine_role(self, issue: Dict, member_id: str, search_pattern: str) -> str:
        """Determine the member's role in an issue based on search pattern."""
        if f"assignee:{member_id}" in search_pattern:
            return "assignee"
        elif f"reporter:{member_id}" in search_pattern:
            return "reporter"
        elif f"creator:{member_id}" in search_pattern:
            return "creator"
        else:
            return "mentioned"
    
    def create_activity_summary(self, issues: List[Dict]) -> Dict:
        """Create a summary of activity across issues."""
        summary = {
            "total_issues": len(issues),
            "by_project": defaultdict(int),
            "by_status": defaultdict(int),
            "by_role": defaultdict(int)
        }
        
        for issue in issues:
            if issue.get('project'):
                summary['by_project'][issue['project']] += 1
            if issue.get('status'):
                summary['by_status'][issue['status']] += 1
            if issue.get('role'):
                summary['by_role'][issue['role']] += 1
        
        return dict(summary)
    
    def format_results(self, results: Dict, output_format: str = "table") -> str:
        """Format results for display."""
        if output_format == "json":
            return json.dumps(results, indent=2, default=str)
        
        # Table format
        output = []
        group_info = results['group_info']
        stats = results['stats']
        
        output.append(f"\n🏢 ROVER-JIRA INTEGRATION REPORT")
        output.append(f"{'='*50}")
        output.append(f"📋 Group: {group_info.get('name', 'Unknown')}")
        output.append(f"📝 Description: {group_info.get('description', 'N/A')}")
        output.append(f"👥 Total Members: {stats['total_members']}")
        output.append(f"🎫 Members with JIRA Activity: {stats['members_with_jira_activity']}")
        output.append(f"📊 Unique Projects Involved: {len(stats['unique_projects'])}")
        output.append(f"🎯 Total Issues Found: {stats['total_issues_found']}")
        
        if stats['unique_projects']:
            output.append(f"\n📂 PROJECTS WITH GROUP MEMBERS:")
            output.append(f"{'-'*40}")
            for project in sorted(stats['unique_projects']):
                members_in_project = results['project_summary'].get(project, [])
                output.append(f"  🔹 {project}: {len(members_in_project)} members")
                for member in sorted(members_in_project):
                    output.append(f"    - {member}")
        
        output.append(f"\n👤 INDIVIDUAL MEMBER ANALYSIS:")
        output.append(f"{'-'*40}")
        
        for member_id, analysis in results['member_analysis'].items():
            if analysis['projects'] or analysis['issues']:
                output.append(f"\n🔸 {member_id}")
                if analysis['projects']:
                    output.append(f"  📂 Projects: {', '.join(analysis['projects'])}")
                output.append(f"  🎫 Issues: {len(analysis['issues'])}")
                if analysis.get('activity_summary'):
                    summary = analysis['activity_summary']
                    if summary.get('by_role'):
                        roles = ', '.join([f"{role}({count})" for role, count in summary['by_role'].items()])
                        output.append(f"  🎭 Roles: {roles}")
        
        return '\n'.join(output)

async def main():
    parser = argparse.ArgumentParser(
        description="Analyze JIRA involvement for Red Hat internal group members",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s sp-ai-support-chatbot                    # Basic analysis
  %(prog)s sp-ai-support-chatbot --detailed         # Detailed analysis
  %(prog)s sp-ai-support-chatbot --format json      # JSON output
        """
    )
    
    parser.add_argument("group_name", help="Name of the rover group to analyze")
    parser.add_argument("--detailed", "-d", action="store_true",
                       help="Include detailed activity summary for each member")
    parser.add_argument("--format", "-f", choices=["table", "json"], default="table",
                       help="Output format (default: table)")
    
    args = parser.parse_args()
    
    integrator = RoverJiraIntegrator()
    
    print(f"🚀 Starting Rover-JIRA Integration Analysis...")
    print(f"📋 Group: {args.group_name}")
    print(f"🔍 Detailed: {args.detailed}")
    
    try:
        results = await integrator.analyze_group_jira_involvement(
            args.group_name, 
            detailed=args.detailed
        )
        
        if "error" in results:
            print(f"❌ Error: {results['error']}", file=sys.stderr)
            sys.exit(1)
        
        formatted_output = integrator.format_results(results, args.format)
        print(formatted_output)
        
    except KeyboardInterrupt:
        print("\n👋 Analysis interrupted!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 