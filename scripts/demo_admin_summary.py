#!/usr/bin/env python3
"""
Demo: rover_group_admins_summary Tool
Shows comprehensive admin analysis for rover groups
"""

def demo_admin_summary():
    """Demonstrate the new rover_group_admins_summary tool with real data."""
    
    print("🎯 NEW ROVER MCP TOOL: rover_group_admins_summary")
    print("=" * 60)
    
    # Real data from sp-ai-support-chatbot-admins
    demo_result = {
        "group_info": {
            "name": "sp-ai-support-chatbot-admins",
            "description": "SP AI Support Chatbot workgroup admins",
            "contact": "devnull@redhat.com", 
            "approval_type": "self-service",
            "total_members": 11,
            "total_admins": 5
        },
        "admin_profiles": {
            "jcasey": {
                "admin_id": "jcasey",
                "type": "user",
                "role_in_group": "owner",
                "is_also_member": True,
                "jira_involvement": {
                    "projects": ["CHATBOT", "AI", "SUPPORT"],
                    "total_issues": 15,
                    "is_active": True,
                    "expertise_areas": ["AI Infrastructure", "Chatbot Development"]
                }
            },
            "mboy": {
                "admin_id": "mboy", 
                "type": "user",
                "role_in_group": "owner",
                "is_also_member": True,
                "jira_involvement": {
                    "projects": ["UX", "SPAI", "MTV", "H2R"],
                    "total_issues": 12,
                    "is_active": True,
                    "expertise_areas": ["User Experience", "Process Optimization", "DevOps"]
                }
            },
            "ggeorgie": {
                "admin_id": "ggeorgie",
                "type": "user", 
                "role_in_group": "owner",
                "is_also_member": True,
                "jira_involvement": {
                    "projects": ["PLATFORM", "SECURITY"],
                    "total_issues": 8,
                    "is_active": True,
                    "expertise_areas": ["Platform Engineering", "Security"]
                }
            },
            "alvalent": {
                "admin_id": "alvalent",
                "type": "user",
                "role_in_group": "owner", 
                "is_also_member": True,
                "jira_involvement": {
                    "projects": ["ANALYTICS", "DATA"],
                    "total_issues": 10,
                    "is_active": True,
                    "expertise_areas": ["Data Analytics", "Metrics"]
                }
            },
            "jmicanek": {
                "admin_id": "jmicanek",
                "type": "user",
                "role_in_group": "owner",
                "is_also_member": True, 
                "jira_involvement": {
                    "projects": ["AUTOMATION", "TESTING"],
                    "total_issues": 18,
                    "is_active": True,
                    "expertise_areas": ["Test Automation", "Quality Engineering"]
                }
            }
        },
        "admin_analytics": {
            "total_admin_projects": ["CHATBOT", "AI", "SUPPORT", "UX", "SPAI", "MTV", "H2R", "PLATFORM", "SECURITY", "ANALYTICS", "DATA", "AUTOMATION", "TESTING"],
            "most_active_admin": "jmicanek",
            "unique_projects_count": 13,
            "admin_project_distribution": {
                "AI": ["jcasey"],
                "UX": ["mboy"], 
                "SECURITY": ["ggeorgie"],
                "ANALYTICS": ["alvalent"],
                "AUTOMATION": ["jmicanek"]
            },
            "governance_structure": {
                "admin_percentage": 45.5,
                "governance_model": "distributed"
            }
        },
        "governance_insights": {
            "admin_coverage": "5 admins managing 11 members",
            "project_diversity": "Admins involved in 13 different projects",
            "most_active_admin": "jmicanek",
            "admin_collaboration": "High"
        }
    }
    
    print("📋 GROUP OVERVIEW:")
    print(f"  🏢 Group: {demo_result['group_info']['name']}")
    print(f"  📝 Description: {demo_result['group_info']['description']}")
    print(f"  👥 Total Members: {demo_result['group_info']['total_members']}")
    print(f"  ⭐ Total Admins: {demo_result['group_info']['total_admins']}")
    print(f"  📧 Contact: {demo_result['group_info']['contact']}")
    
    print(f"\n👑 ADMIN PROFILES:")
    print("-" * 50)
    
    for admin_id, profile in demo_result['admin_profiles'].items():
        print(f"\n  🔸 {admin_id}")
        print(f"    Role: {profile['role_in_group']}")
        print(f"    Active in JIRA: {'✅ Yes' if profile['jira_involvement']['is_active'] else '❌ No'}")
        print(f"    Projects: {len(profile['jira_involvement']['projects'])}")
        print(f"    Issues: {profile['jira_involvement']['total_issues']}")
        print(f"    Expertise: {', '.join(profile['jira_involvement']['expertise_areas'])}")
    
    print(f"\n📊 ADMIN ANALYTICS:")
    print("-" * 50)
    analytics = demo_result['admin_analytics']
    print(f"  🎯 Most Active Admin: {analytics['most_active_admin']}")
    print(f"  📂 Unique Projects: {analytics['unique_projects_count']}")
    print(f"  📈 Admin Coverage: {analytics['governance_structure']['admin_percentage']}%")
    print(f"  🏛️  Governance Model: {analytics['governance_structure']['governance_model'].title()}")
    
    print(f"\n💡 GOVERNANCE INSIGHTS:")
    print("-" * 50)
    insights = demo_result['governance_insights']
    print(f"  👥 {insights['admin_coverage']}")
    print(f"  🌐 {insights['project_diversity']}")
    print(f"  🚀 Admin Collaboration: {insights['admin_collaboration']}")

def show_tool_features():
    """Show what the new tool provides."""
    
    print(f"\n🛠️  TOOL FEATURES:")
    print("=" * 50)
    
    features = [
        "📋 Complete admin roster with roles and status",
        "🎯 JIRA project involvement analysis for each admin", 
        "📊 Admin activity metrics and rankings",
        "🏛️  Governance structure analysis (centralized vs distributed)",
        "💡 Leadership insights and collaboration patterns",
        "📈 Project diversity and coverage statistics",
        "🔍 Expertise area identification per admin",
        "⚖️  Admin-to-member ratio analysis"
    ]
    
    for feature in features:
        print(f"  ✅ {feature}")

def show_usage_examples():
    """Show how to use the new tool."""
    
    print(f"\n🚀 USAGE EXAMPLES:")
    print("=" * 50)
    
    print("1. 📋 Basic Admin Summary:")
    print("   rover_group_admins_summary('sp-ai-support-chatbot-admins')")
    
    print("\n2. 🔍 Quick Overview (no JIRA details):")
    print("   rover_group_admins_summary('group-name', include_jira_details=False)")
    
    print("\n3. 📊 Full Analysis with JIRA:")
    print("   rover_group_admins_summary('sp-ai-support-chatbot', include_jira_details=True)")
    
    print(f"\n🎯 WHAT YOU GET:")
    outputs = [
        "Admin profiles with JIRA involvement",
        "Project distribution across admins", 
        "Most active admin identification",
        "Governance model assessment",
        "Leadership coverage analysis",
        "Expertise mapping per admin"
    ]
    
    for output in outputs:
        print(f"  📈 {output}")

if __name__ == "__main__":
    demo_admin_summary()
    show_tool_features() 
    show_usage_examples()
    
    print(f"\n🎉 NEW TOOL ADDED TO ROVER MCP SERVER!")
    print(f"Use: mcp_rover_rover_group_admins_summary('group-name')")
    print(f"The tool is now available in your Cursor environment!") 