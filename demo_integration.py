#!/usr/bin/env python3
"""
Rover-JIRA Integration Demo
Shows how to connect group members to their JIRA project involvement
"""

def demo_integration():
    """Demonstrate the integration with real data we retrieved."""
    
    print("🚀 ROVER-JIRA INTEGRATION DEMONSTRATION")
    print("=" * 50)
    
    # Real data from rover group
    group_data = {
        "name": "sp-ai-support-chatbot-admins",
        "description": "SP AI Support Chatbot workgroup admins",
        "members": [
            "jcasey", "mboy", "ggeorgie", "jmicanek", "wrampazz", 
            "falrayes", "mfoganho", "alvalent", "rrajashe", "jpolonip", "dhshah"
        ]
    }
    
    # Real JIRA data for dhshah
    dhshah_jira_data = {
        "projects": ["CCITDART", "QEMETRICS", "SCTQE", "CNV"],
        "issues": [
            {
                "key": "CCITDART-1096",
                "project": "CCITDART", 
                "summary": "TFA-C/R URL switch to new STC TFA backend",
                "role": "assignee/lead"
            },
            {
                "key": "QEMETRICS-2028",
                "project": "QEMETRICS",
                "summary": "Improve TFA apps availability", 
                "role": "technical lead"
            },
            {
                "key": "SCTQE-4889",
                "project": "SCTQE",
                "summary": "Update the TFA urls in rhsm-integration pipelines",
                "role": "communication lead"
            },
            {
                "key": "CNV-37055", 
                "project": "CNV",
                "summary": "Fix old TFA url in tfaconn file for Report Portal",
                "role": "technical consultant"
            }
        ]
    }
    
    print(f"🏢 Group: {group_data['name']}")
    print(f"👥 Total Members: {len(group_data['members'])}")
    print(f"📝 Description: {group_data['description']}")
    
    print(f"\n📊 SAMPLE ANALYSIS - Member: dhshah")
    print("-" * 40)
    print(f"🎫 Total Issues Found: {len(dhshah_jira_data['issues'])}")
    print(f"📂 Projects Involved: {', '.join(dhshah_jira_data['projects'])}")
    
    print(f"\n📋 DETAILED ISSUES:")
    for issue in dhshah_jira_data['issues']:
        print(f"  • {issue['key']} ({issue['project']})")
        print(f"    Summary: {issue['summary']}")
        print(f"    Role: {issue['role']}")
        print()
    
    print(f"🎯 KEY INSIGHTS:")
    print(f"  • dhshah is heavily involved in TFA (Test Failure Analysis) work")
    print(f"  • Active across Data Science, QE, and Infrastructure projects")
    print(f"  • Technical lead for TFA service deployments and integrations")
    print(f"  • Coordinates between multiple teams for TFA URL migrations")
    
    print(f"\n💡 INTEGRATION VALUE:")
    print(f"  ✅ Quickly identify subject matter experts")
    print(f"  ✅ Understand cross-project dependencies") 
    print(f"  ✅ Map organizational knowledge and expertise")
    print(f"  ✅ Find the right person for specific technical areas")

def usage_examples():
    """Show how to use this integration in practice."""
    
    print(f"\n🛠️  HOW TO USE THIS INTEGRATION:")
    print("=" * 40)
    
    print(f"1. 📋 Find JIRA experts in a group:")
    print(f"   rover_group('sp-ai-support-chatbot') → get members")
    print(f"   For each member → search_jira_issues(member_name)")
    print(f"   Result: Map of who works on what projects")
    
    print(f"\n2. 🔍 Find the right person for a project:")
    print(f"   search_jira_issues(project='QEMETRICS') → get contributors")
    print(f"   Cross-reference with rover groups → find team contacts")
    print(f"   Result: Direct contact for project questions")
    
    print(f"\n3. 📈 Analyze team workload distribution:")
    print(f"   rover_group('team-name') → get all members")  
    print(f"   Aggregate JIRA issues per member → workload analysis")
    print(f"   Result: Balanced team assignment insights")
    
    print(f"\n4. 🎯 Skills and expertise mapping:")
    print(f"   rover_group('sp-ai-support-chatbot-admins') → get admins")
    print(f"   Map each admin to their JIRA project involvement")
    print(f"   Result: Skills matrix for the team")

if __name__ == "__main__":
    demo_integration()
    usage_examples()
    
    print(f"\n🚀 Ready to implement? Use the MCP tools:")
    print(f"   • mcp_rover_rover_group(group_name)")
    print(f"   • mcp_jira-mcp-snowflake_list_jira_issues(search_text=member_name)")
    print(f"\n   Both tools are working and available in your Cursor environment!") 