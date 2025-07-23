# 🎯 Test Queries for Integrated MCP Servers (Rover + JIRA)

## Overview
These 15 queries demonstrate the analytical capabilities of your **dual MCP server setup** - combining rover group data with real JIRA project data from Snowflake. This integration provides powerful insights across team structure, project activity, and organizational intelligence.

## 🔧 **MCP Server Configuration**
- **Rover MCP**: Red Hat internal groups, team structure, access management
- **JIRA MCP Snowflake**: Real JIRA project data, issue tracking, project analytics
- **Integration Power**: Cross-correlate team membership with actual project work

---

# 🏢 **ROVER-ONLY QUERIES** (Team Structure & Access)

## 1. 👥 **Team Structure Discovery**
```
"Who are the members of the sp-ai-support-chatbot team and what are their roles?"
```
**MCP Server**: Rover  
**Tools Used**: `rover_group`  
**Expected Output**: Team member list, group description, admin vs regular member distinction  
**Business Value**: Quick team discovery for new projects or escalations

---

## 2. 🔗 **Multi-Group Member Analysis**
```
"Show me detailed profiles for ggeorgie and mboy, including their group memberships and risk levels"
```
**MCP Server**: Rover  
**Tools Used**: `get_detailed_person_profile`, `get_comprehensive_member_profile`  
**Expected Output**: Comprehensive profiles with rover groups, access levels, recommendations  
**Business Value**: Access review and security assessment

---

## 3. 📈 **Team Comparison Analysis**
```
"Compare the team structure and access patterns between sp-ai-support-chatbot and sp-resilience-team groups"
```
**MCP Server**: Rover  
**Tools Used**: `rover_group` + comparison analysis  
**Expected Output**: Side-by-side team comparison, access pattern analysis  
**Business Value**: Organizational structure optimization

---

# 📊 **JIRA-ONLY QUERIES** (Project & Issue Analysis)

## 4. 🎯 **Project Portfolio Analysis**
```
"Show me all JIRA projects and give me a summary of their current status and activity levels"
```
**MCP Server**: JIRA Snowflake  
**Tools Used**: `get_jira_project_summary`  
**Expected Output**: Complete project landscape with metrics and activity indicators  
**Business Value**: Executive overview of all active initiatives

---

## 5. 🔍 **Issue Search & Analysis**
```
"Find all JIRA issues related to 'AI' or 'chatbot' and analyze their current status"
```
**MCP Server**: JIRA Snowflake  
**Tools Used**: `list_jira_issues`  
**Expected Output**: Filtered issue list with status analysis and trends  
**Business Value**: Technology-specific work tracking and progress monitoring

---

## 6. 📋 **Component Analysis**
```
"List all JIRA components and identify which ones might be related to platform engineering"
```
**MCP Server**: JIRA Snowflake  
**Tools Used**: `list_jira_components`  
**Expected Output**: Component inventory with platform engineering categorization  
**Business Value**: Technical architecture understanding and component ownership

---

# 🤝 **INTEGRATED QUERIES** (Rover + JIRA Combined Power)

## 7. 🔍 **Individual Expertise with Real Project Data**
```
"Give me a comprehensive profile of ggeorgie including their rover group memberships AND their actual JIRA project involvement"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `get_comprehensive_member_profile` + `list_jira_issues(search_text='ggeorgie')`  
**Expected Output**: Complete individual analysis with group access and real project work  
**Business Value**: True understanding of individual capabilities and current contributions

---

## 8. 🏢 **Team Activity with Real Data**
```
"Analyze the sp-ai-support-chatbot team structure and correlate it with actual JIRA issues they're working on"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `rover_group` + `list_jira_issues` for each member  
**Expected Output**: Team structure mapped to real project activity and workload distribution  
**Business Value**: Accurate team effectiveness assessment with real work data

---

## 9. 🎯 **Expert Discovery with Project Context**
```
"Who should I contact for AI/ML platform questions? Show me both their rover group roles AND their recent JIRA work"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `rover_group` + `get_comprehensive_member_profile` + `list_jira_issues`  
**Expected Output**: Expert recommendations with both access rights and proven project experience  
**Business Value**: Rapid expert identification with verified current involvement

---

## 10. 📊 **Cross-Team Project Collaboration**
```
"Find all JIRA projects that involve members from both sp-ai-support-chatbot and sp-resilience-team groups"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `rover_group` for both teams + `list_jira_issues` cross-referenced  
**Expected Output**: Cross-team collaboration analysis with shared project identification  
**Business Value**: Understanding inter-team dependencies and collaboration patterns

---

# 🔬 **ADVANCED INTEGRATED ANALYSIS**

## 11. 📊 **Comprehensive Team Audit with Real Activity**
```
"Perform a complete audit of the sp-ai-support-chatbot team: group structure, member access levels, and current JIRA project involvement"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `rover_group` + `get_detailed_person_profile` + `list_jira_issues` for all members  
**Expected Output**: Complete team audit with security assessment and real work verification  
**Business Value**: Comprehensive team review for compliance and optimization

---

## 12. 🎪 **Executive Dashboard with Real Data**
```
"Create an executive summary combining team structures from rover groups with current project portfolio from JIRA"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `rover_group` + `get_jira_project_summary` + cross-correlation analysis  
**Expected Output**: Executive dashboard with organizational structure and active project status  
**Business Value**: Leadership visibility into team organization and project health

---

## 13. 🔍 **Issue Escalation Path Analysis**
```
"For critical JIRA issues, show me the escalation path through rover group ownership and admin structures"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `list_jira_issues` (high priority) + `rover_group` ownership mapping  
**Expected Output**: Clear escalation matrix with contact paths for critical issues  
**Business Value**: Incident response optimization and accountability clarity

---

## 14. 📈 **Organizational Health Assessment**
```
"Analyze both rover group activity and JIRA project health to identify teams that need attention or support"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `correlate_rover_groups_with_jira` + `list_jira_issues` trend analysis  
**Expected Output**: Health score for teams with recommendations for intervention or support  
**Business Value**: Proactive organizational management and resource allocation

---

## 15. 🚀 **Strategic Planning Intelligence**
```
"Identify emerging project themes in JIRA and correlate them with current team capabilities in rover groups"
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `list_jira_issues` pattern analysis + `rover_group` capability mapping  
**Expected Output**: Strategic insights on project trends vs. current organizational capabilities  
**Business Value**: Strategic planning and capability gap identification

---

## 16. **Hackathot Team Collaboration**
```
Corelate between rover and jira for following people dgregor, dhshah, ggeorgie, rajkumar, npotluri, and show us the extensive information about them
```
**MCP Servers**: Rover + JIRA Snowflake  
**Tools Used**: `list_jira_issues` pattern analysis + `get_detailed_person_profile` capability mapping  
**Expected Output**: Strategic insights on team collaboration vs. current organizational capabilities  
**Business Value**: Strategic planning and capability gap identification

---

## 🚀 How to Use These Integrated Queries

### In Cursor Environment (Recommended):
1. **Natural Language**: Ask these questions directly to Claude in Cursor
2. **Automatic Integration**: Claude intelligently combines data from both MCP servers
3. **Rich Analysis**: Get comprehensive insights combining team structure + real project data
4. **Professional Output**: Receive management-ready reports and analysis

### MCP Server Auto-Selection:
Claude automatically determines which MCP servers to use based on your query:
- **Rover queries** → Uses local rover MCP server
- **JIRA queries** → Uses JIRA Snowflake MCP server  
- **Integrated queries** → Uses both servers and correlates data

### Command Line Testing:
```bash
# Test rover server
python demo_analytical_showcase.py

# Test individual rover tools
python -c "
import asyncio
from mcp_server import rover_group
result = asyncio.run(rover_group('sp-ai-support-chatbot'))
print(result)
"

# JIRA server testing happens automatically through Claude in Cursor
```

### Example Integrated Query Flow:
```
You: "Give me dhshah's profile including both rover groups AND actual JIRA work"

Claude: 
1. Calls rover MCP: get_comprehensive_member_profile('dhshah')
2. Calls JIRA MCP: list_jira_issues(search_text='dhshah')  
3. Correlates the data to show group access + real project involvement
4. Provides unified analysis with actionable insights
```

---

## 🎯 Query Categories & Complexity Levels

| **Category** | **Queries** | **MCP Servers** | **Business Impact** |
|--------------|-------------|----------------|-------------------|
| 🏢 **Rover Structure** | 1, 2, 3 | Rover only | Team organization, access control |
| 📊 **JIRA Projects** | 4, 5, 6 | JIRA only | Project visibility, issue tracking |
| 🤝 **Basic Integration** | 7, 8, 9, 10 | Both servers | Real team-project correlation |
| 🔬 **Advanced Analysis** | 11, 12, 13, 14, 15 | Both + complex logic | Strategic intelligence, executive insights |

### **Complexity Progression:**
- **🟢 Beginner (1-6)**: Single server queries for specific data
- **🟡 Intermediate (7-10)**: Cross-server correlation and basic integration  
- **🔴 Advanced (11-15)**: Multi-server analysis with strategic insights

---

## 💡 Pro Tips for Integrated Analysis

1. **🟢 Start Simple**: Begin with queries 1-6 to understand each MCP server's capabilities
2. **🟡 Progress to Integration**: Try queries 7-10 to see the power of combined data
3. **🔴 Advanced Insights**: Use queries 11-15 for strategic analysis and executive reporting
4. **🔄 Natural Language**: Ask conversationally - Claude handles all MCP server coordination
5. **📊 Real Data Advantage**: Rover provides team structure, JIRA provides actual work - combined they show the complete picture
6. **🔍 Follow-up Deep Dives**: After getting overview results, ask for specific member or project details
7. **⚡ Auto-Detection**: Claude automatically determines which servers to use based on your question
8. **🎯 Context Matters**: Mention both "team structure" and "project work" to trigger integrated analysis

### **Example Escalation Pattern:**
```
1. Start: "Who's in the AI chatbot team?" (Rover only)
2. Expand: "What projects are they working on?" (JIRA only)  
3. Integrate: "Show me their team structure AND current project work" (Both servers)
4. Analyze: "Give me a complete team effectiveness assessment" (Advanced integration)
```

These 15 queries demonstrate the **revolutionary power** of combining organizational intelligence with real project data - transforming how you understand and manage teams! 

