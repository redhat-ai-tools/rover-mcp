#!/usr/bin/env python3
"""
Demo script for the new rover_member_summary MCP tool.
This showcases comprehensive member profiles including group roles and JIRA involvement.
"""

import json
from datetime import datetime

def simulate_member_summary(member_id: str, include_jira_details: bool = True):
    """
    Simulate the rover_member_summary tool output with realistic data.
    This demonstrates what the tool would return with real data integration.
    """
    
    # Realistic member data based on actual Red Hat context
    member_data = {
        "dhshah": {
            "projects": ["SPAI", "KONFLUX", "PVO11Y", "OSIM", "SPRE"],
            "groups": [
                {"name": "sp-ai-support-chatbot", "role": "member"},
                {"name": "sp-ai-support-chatbot-admins", "role": "member"},
                {"name": "konflux-users", "role": "member"}
            ],
            "expertise": ["AI/ML Platform Development", "Software Engineering", "Platform Integration"],
            "recent_issues": [
                {
                    "key": "SPAI-213",
                    "project": "SPAI", 
                    "summary": "onboarding first users (feedback and testing)",
                    "status": "Open",
                    "role": "assignee"
                },
                {
                    "key": "KONFLUX-8901",
                    "project": "KONFLUX",
                    "summary": "Integrate AI chatbot with Konflux platform",
                    "status": "In Progress", 
                    "role": "reporter"
                },
                {
                    "key": "PVO11Y-1701",
                    "project": "PVO11Y",
                    "summary": "Observability metrics for AI services",
                    "status": "Open",
                    "role": "mentioned"
                }
            ]
        },
        "mboy": {
            "projects": ["H2R", "HPUX", "SPAI", "MTV", "PVO11Y"],
            "groups": [
                {"name": "sp-ai-support-chatbot-admins", "role": "owner"},
                {"name": "pv-observability-team", "role": "member"},
                {"name": "ux-research-guild", "role": "member"}
            ],
            "expertise": ["User Experience Research", "CI/CD Pipeline Development", "Process Optimization"],
            "recent_issues": [
                {
                    "key": "H2R-1075",
                    "project": "H2R",
                    "summary": "Review of notifications that create no action tickets for GSS coordinators",
                    "status": "Open",
                    "role": "assignee"
                },
                {
                    "key": "SPAI-129", 
                    "project": "SPAI",
                    "summary": "Define a gitlab ci pipeline for the frontend service",
                    "status": "Resolved",
                    "role": "assignee"
                }
            ]
        }
    }
    
    # Get member-specific data or use default
    data = member_data.get(member_id, {
        "projects": ["PLACEHOLDER"],
        "groups": [{"name": "unknown-group", "role": "member"}],
        "expertise": ["To be determined"],
        "recent_issues": [
            {
                "key": "EXAMPLE-123",
                "project": "PLACEHOLDER",
                "summary": f"Sample issue for {member_id}",
                "status": "Open",
                "role": "mentioned"
            }
        ]
    })
    
    # Build comprehensive member summary
    member_summary = {
        "member_profile": {
            "member_id": member_id,
            "type": "user",
            "total_groups": len(data["groups"]),
            "roles": [f"{group['role']} in {group['name']}" for group in data["groups"]]
        },
        "group_memberships": {
            "discovered_groups": data["groups"],
            "leadership_roles": [group for group in data["groups"] if group["role"] in ["owner", "admin"]],
            "membership_diversity": "high" if len(data["groups"]) > 2 else "moderate"
        },
        "jira_involvement": {
            "projects": data["projects"],
            "total_issues": len(data["recent_issues"]),
            "is_active": len(data["recent_issues"]) > 0,
            "expertise_areas": data["expertise"],
            "activity_level": "high" if len(data["recent_issues"]) > 3 else "moderate" if len(data["recent_issues"]) > 0 else "low"
        },
        "professional_profile": {
            "primary_expertise": data["expertise"][:3],
            "collaboration_score": "high" if len(data["projects"]) > 3 else "moderate",
            "project_diversity": len(set(data["projects"]))
        }
    }
    
    if include_jira_details:
        member_summary["jira_involvement"]["recent_issues"] = data["recent_issues"]
        
        # Add project breakdown
        project_breakdown = {}
        for project in data["projects"]:
            project_issues = [issue for issue in data["recent_issues"] if issue.get("project") == project]
            project_breakdown[project] = {
                "issue_count": len(project_issues),
                "recent_activity": len(project_issues) > 0,
                "primary_role": project_issues[0]["role"] if project_issues else "contributor"
            }
        member_summary["jira_involvement"]["project_breakdown"] = project_breakdown
    
    # Add insights based on activity
    activity_insights = []
    if member_summary["jira_involvement"]["is_active"]:
        activity_insights.append("Active contributor with recent JIRA involvement")
    if member_summary["professional_profile"]["project_diversity"] > 3:
        activity_insights.append("Cross-functional expertise across multiple projects")
    if member_summary["jira_involvement"]["activity_level"] == "high":
        activity_insights.append("High-volume contributor")
    if len(member_summary["group_memberships"]["leadership_roles"]) > 0:
        activity_insights.append("Leadership experience in Red Hat groups")
    
    member_summary["insights"] = {
        "activity_insights": activity_insights,
        "recommended_for": [
            "Technical consultation", 
            "Project collaboration",
            "Cross-team initiatives"
        ] if member_summary["jira_involvement"]["is_active"] else ["Future opportunities"],
        "expertise_summary": f"Specialist in {', '.join(data['expertise'][:2])}" if data['expertise'] else "Expertise to be determined",
        "leadership_potential": "High" if len(member_summary["group_memberships"]["leadership_roles"]) > 0 else "Emerging"
    }
    
    return member_summary

def main():
    """Demonstrate the rover_member_summary tool functionality."""
    
    print("🔍 ROVER MEMBER SUMMARY TOOL DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Example 1: dhshah profile
    print("📋 EXAMPLE 1: Member Profile - dhshah")
    print("-" * 40)
    dhshah_summary = simulate_member_summary("dhshah", include_jira_details=True)
    
    print(f"👤 Member: {dhshah_summary['member_profile']['member_id']}")
    print(f"📊 Group Memberships: {dhshah_summary['member_profile']['total_groups']} groups")
    print(f"🎯 Activity Level: {dhshah_summary['jira_involvement']['activity_level']}")
    print(f"🔬 Expertise: {', '.join(dhshah_summary['professional_profile']['primary_expertise'])}")
    print()
    
    print("🏢 GROUP INVOLVEMENT:")
    for group in dhshah_summary["group_memberships"]["discovered_groups"]:
        role_emoji = "👑" if group["role"] == "owner" else "⚙️" if group["role"] == "admin" else "👥"
        print(f"  {role_emoji} {group['role']} in {group['name']}")
    print()
    
    print("🎯 JIRA PROJECT INVOLVEMENT:")
    for project, details in dhshah_summary["jira_involvement"]["project_breakdown"].items():
        status_emoji = "🟢" if details["recent_activity"] else "⚪"
        print(f"  {status_emoji} {project}: {details['issue_count']} issues ({details['primary_role']})")
    print()
    
    print("💡 INSIGHTS:")
    for insight in dhshah_summary["insights"]["activity_insights"]:
        print(f"  ✨ {insight}")
    print(f"  🎯 {dhshah_summary['insights']['expertise_summary']}")
    print(f"  🚀 Leadership Potential: {dhshah_summary['insights']['leadership_potential']}")
    print()
    
    # Example 2: mboy profile (admin)
    print("📋 EXAMPLE 2: Admin Profile - mboy")
    print("-" * 40)
    mboy_summary = simulate_member_summary("mboy", include_jira_details=True)
    
    print(f"👤 Member: {mboy_summary['member_profile']['member_id']}")
    print(f"👑 Leadership Roles: {len(mboy_summary['group_memberships']['leadership_roles'])}")
    print(f"📊 Projects: {len(mboy_summary['jira_involvement']['projects'])}")
    print(f"🔥 Recent Issues: {mboy_summary['jira_involvement']['total_issues']}")
    print()
    
    print("🏆 LEADERSHIP POSITIONS:")
    for role in mboy_summary["group_memberships"]["leadership_roles"]:
        print(f"  👑 {role['role']} in {role['name']}")
    print()
    
    print("🔬 EXPERTISE AREAS:")
    for expertise in mboy_summary["professional_profile"]["primary_expertise"]:
        print(f"  🎯 {expertise}")
    print()
    
    print("🚀 RECENT ACTIVITY:")
    for issue in mboy_summary["jira_involvement"]["recent_issues"][:3]:
        status_emoji = "🟢" if issue["status"] == "Resolved" else "🟡" if issue["status"] == "In Progress" else "🔴"
        print(f"  {status_emoji} {issue['key']}: {issue['summary'][:50]}...")
    print()
    
    # Example 3: JSON output for integration
    print("📋 EXAMPLE 3: JSON Output Structure")
    print("-" * 40)
    sample_summary = simulate_member_summary("sample-user", include_jira_details=False)
    print("Sample JSON structure (abbreviated):")
    print(json.dumps({
        "member_profile": sample_summary["member_profile"],
        "insights": sample_summary["insights"]
    }, indent=2))
    print()
    
    print("🔧 TOOL USAGE EXAMPLES")
    print("-" * 40)
    print("# Get full member summary with JIRA details")
    print("rover_member_summary('dhshah', include_jira_details=True)")
    print()
    print("# Get basic member profile without detailed JIRA data")
    print("rover_member_summary('mboy', include_jira_details=False)")
    print()
    print("# For any Red Hat member ID")
    print("rover_member_summary('your-redhat-id')")
    print()
    
    print("💡 INTEGRATION NOTES")
    print("-" * 40)
    print("✅ Tool added to rover MCP server")
    print("✅ Integrates with existing JIRA analysis functions")
    print("✅ Provides comprehensive member profiles")
    print("✅ Supports both detailed and summary views")
    print("🔄 Ready for real JIRA data integration via jira-mcp-snowflake")
    print("🔄 Can be enhanced with actual group discovery APIs")

if __name__ == "__main__":
    main() 