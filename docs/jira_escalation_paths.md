
### PROMPT: For critical JIRA issues, show me the escalation path through rover group ownership and admin structures

---

# Critical JIRA Issue Escalation Path Through Rover Group Structures

Based on analysis of critical (Priority 1) JIRA issues and rover group ownership hierarchies, here's the comprehensive escalation framework:

## Escalation Flow Diagram

The escalation follows a structured path from individual issues through team ownership to executive leadership:

```
Critical JIRA Issues (Priority 1 & 2)
    ↓
Issue Triage & Classification
    ↓
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ Installation    │ Security        │ Platform        │ Infrastructure  │
│ Issues          │ Issues          │ Issues          │ Issues          │
│ INSTALLER/      │ OSIDB/OSIM      │ CNV/RHAIENG/    │ LOG/KFLUXSPRT   │
│ AITRIAGE        │                 │ HMS             │                 │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
    ↓                   ↓               ↓                   ↓
L1: Team Level     L1: Security    L1: Platform     L1: SP Resilience
    EXD Distribution   Teams           Engineering      Team
    Guild                              Teams            
    ↓                   ↓               ↓                   ↓
L2: Guild/Domain   L2: Security    L2: EXD-SP-All   L2: EXD-SP-All
    EXD-SP-All         Leadership      (8 owners)       (8 owners)
    ↓                   ↓               ↓                   ↓
L3: Executive      L3: CISO Chain  L3: Executive    L3: Executive
    Leadership                         Leadership       Leadership
```

## Detailed Escalation Matrix by Issue Type

| Issue Type | Example Projects | L1 Team (Rover Group) | L1 Owners | L2 Escalation | L3 Executive |
|------------|------------------|------------------------|-----------|---------------|--------------|
| **🔧 Installation/Provisioning** | INSTALLER, AITRIAGE | `exd-guild-distribution` | rbikar | `exd-sp-all` (8 owners) | rpotts (Manager) |
| **🔒 Security/CVE** | OSIDB, OSIM | Security Teams | Project-specific | Security Leadership | CISO Chain |
| **🏗️ Platform Engineering** | CNV, RHAIENG, HMS | Platform Teams | Team leads | `exd-sp-all` | dgregor, mikeb |
| **⚙️ Infrastructure/SRE** | LOG, KFLUXSPRT | `sp-resilience-team` | jcasey, jkriz, amarchuk, mboy | `exd-sp-all` | maherber, efrench |
| **🤖 AI/ML Platform** | AIML, SPAI | `sp-ai-support-chatbot` | jcasey, mboy, ggeorgie | `exd-sp-all` | okopacek, cfreitas |

## Key Rover Groups in Escalation Chain

### **Primary Escalation Groups**

**1. exd-sp-all (Enterprise Experience & Delivery - Software Production)**
- **Role**: L2/L3 escalation point for most critical issues
- **Owners (8)**: maherber, dgregor, mikeb, rpotts, anuagarw, efrench, okopacek, cfreitas
- **Size**: 220+ members
- **Scope**: Cross-functional coordination and executive escalation

**2. sp-resilience-team**
- **Role**: L1 for infrastructure and site reliability issues
- **Owners (4)**: jcasey, jkriz, amarchuk, mboy
- **Size**: 19 members
- **Scope**: Platform stability, performance, incident response

**3. exd-guild-distribution**
- **Role**: L1 for installation and distribution issues
- **Owner**: rbikar
- **Size**: 22 members
- **Scope**: Product installation, provisioning, delivery pipeline

**4. sp-ai-support-chatbot**
- **Role**: L1 for AI/ML platform issues
- **Owners (3)**: jcasey, mboy, ggeorgie
- **Size**: 12 members
- **Scope**: AI platform operations, chatbot infrastructure

## Escalation Triggers & SLA Guidelines

### **Automatic Escalation Criteria**
- **Priority 1 Issues**: Immediate L1 team notification + L2 awareness
- **Priority 2 Issues**: L1 team owns, L2 informed within 2 hours
- **Customer-Impacting**: Direct L2 escalation if customer-facing
- **Security Issues**: Parallel escalation to security teams

### **Time-Based Escalation**
- **0-2 hours**: L1 team response required
- **2-4 hours**: L2 involvement if no resolution path
- **4-8 hours**: L3 executive awareness
- **8+ hours**: Executive incident management

### **Cross-Team Dependencies**
- **Multiple Project Impact**: Direct `exd-sp-all` coordination
- **Infrastructure Dependencies**: `sp-resilience-team` consultation
- **Security Implications**: Security team parallel engagement
- **Customer Communication**: Executive chain notification

## Emergency Contact Chain

### **L1 Response Teams**
- **Installation Issues**: rbikar (exd-guild-distribution)
- **Infrastructure Issues**: jcasey, jkriz, amarchuk, mboy (sp-resilience-team)
- **AI Platform Issues**: jcasey, mboy, ggeorgie (sp-ai-support-chatbot)

### **L2 Coordination (exd-sp-all owners)**
- **Technical Escalation**: dgregor, mikeb
- **Program Management**: maherber, efrench
- **Executive Communication**: rpotts, anuagarw
- **International Coordination**: okopacek, cfreitas

### **L3 Executive Chain**
- **Immediate Managers**: rpotts, maherber
- **Directors**: efrench, dgregor
- **VP Level**: mikeb (when required)

## Special Escalation Scenarios

### **Multi-Team Critical Issues**
1. **Cross-Platform Impact**: Direct `exd-sp-all` war room
2. **Customer-Facing Outages**: Parallel customer success team notification
3. **Security Incidents**: Independent security escalation chain
4. **Compliance Issues**: Legal and compliance team engagement

### **International Considerations**
- **EMEA Hours**: okopacek coordination
- **APAC Hours**: cfreitas coordination
- **24/7 Coverage**: Rotating on-call through `sp-resilience-team`

---
*Last Updated: Based on rover group analysis and JIRA priority issue patterns*
*Contact: Generated from rover-mcp analysis tools* 