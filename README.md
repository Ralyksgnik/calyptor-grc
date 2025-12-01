# Calyptor – GRC & Compliance Automation Platform

Calyptor is a modern compliance and security workflow platform designed to simplify CMMC, NIST 800-171, and enterprise evidence management. This repository contains architecture documentation, automation prototypes, schemas, diagrams, and early-stage tooling that define the Calyptor ecosystem.

---

## 📌 Features & Components

### **Core GRC Engine**
- Control Dashboard  
- Evidence Management System  
- Control Test Evaluator  
- Gap Analysis Engine  
- POA&M Engine  
- Compliance Score Engine  

### **Automation Layer**
- Automated evidence ingestion  
- Continuous compliance checks  
- License & user inventory automation  
- Device compliance automation (Intune / API)  
- Daily risk snapshots  

### **Reporting & Audit**
- Auditor mode  
- Customer portal mode  
- CSV/PDF reporting  
- Compliance roadmap generator  

### **AI Assistance Layer**
- AI Evidence Classifier  
- AI Gap Explanation Generator  
- AI Auditor Assistant  
- Automated SSP Builder  
- Internal Audit Checklist System  

---

## 🧱 Architecture Diagram

```mermaid
flowchart LR
    U["User / Admin"] --> A["Auth Service (Entra ID / SSO)"]
    A --> P1["Admin Portal"]
    A --> P2["Customer Portal"]

    subgraph CORE["Core GRC Engine"]
        CD["Control Dashboard"] --> EM["Evidence Management System"]
        CD --> CTE["Control Test Evaluator"]
        CD --> GA["Gap Analysis Engine"]
        EM --> PE["POA&M Engine"]
        EM --> CDOC["Compliance Documentation Store"]
        CTE --> CS["Compliance Score Engine"]
        GA --> CS
        PE --> CS
    end

    P1 --> CD
    P2 --> CD

    subgraph AUTO["Automation & Ingestion"]
        AEI["Automated Evidence Ingestion (API / CSV / Scripts)"]
        CCC["Continuous Compliance Checks"]
        LIA["License & User Inventory Automation"]
        DCA["Device Compliance Automation (Intune / Scripts)"]
        DRS["Daily Risk Snapshot Generator"]
    end

    AEI --> EM
    CCC --> GA
    LIA --> CD
    DCA --> EM
    DRS --> CS

    subgraph INTEG["Security & Platform Integrations"]
        M365["M365 / Entra ID Inventory"]
        INTUNE["Intune Device Compliance"]
        S1["SentinelOne / Huntress"]
        QUP["Qualys / Umbrella / Proofpoint"]
        NOTIF["Slack / Email Notifications"]
    end

    M365 --> AEI
    INTUNE --> DCA
    S1 --> CCC
    QUP --> CCC
    CS --> NOTIF

    subgraph REPORT["Reporting & Audit Modes"]
        RPT["PDF / CSV Report Builder"]
        AUD["Auditor Mode"]
        CP["Customer Portal Mode"]
        CRG["Compliance Roadmap Generator"]
    end

    CS --> RPT
    CS --> AUD
    CS --> CRG
    P2 --> CP

    subgraph AI["AI Assistance Layer"]
        AIEC["AI Evidence Classifier"]
        AIGE["AI Gap Explanation Generator"]
        AIAA["AI Auditor Assistant"]
        ASSP["Automated SSP Builder"]
        IAC["Internal Audit Checklist System"]
    end

    EM --> AIEC
    GA --> AIGE
    AUD --> AIAA
    CDOC --> ASSP
    CD --> IAC

    subgraph INFRA["Platform Infrastructure"]
        DB["Compliance Database"]
        FS["File Storage (Evidence Uploads)"]
        API["REST API Layer"]
        LOGS["Audit Log System"]
    end

    EM --> DB
    PE --> DB
    CS --> DB
    EM --> FS
    CORE --> API
    AUTO --> API
    INTEG --> API
    REPORT --> API
    AI --> API
    API --> LOGS
```
---

📁 Repository Structure

/docs        → Detailed design documents, workflows, SSA/POA&M logic  
/diagrams    → Mermaid and Figma architecture diagrams  
/src         → Demo scripts, prototypes, schema examples  
---

## 🧪 Control Test Evaluator API Demo  

A minimal API schema and demo implementation for submitting compliance control tests and receiving evaluation status.

- **Schema**: see `/docs/control-evaluator-schema.yaml`  
- **Demo API**: see `/src/python/control_evaluator_demo.py`  
- **Run locally**:
```bash
cd src/python
pip install fastapi[all]
python control_evaluator_demo.py
```

- **Example request**:
```json
POST /evaluate-control
{
  "controlId": "AC.1.001",
  "evidenceIds": ["EVID-001","EVID-002"],
  "testResult": "pass",
  "testedAt": "2025-12-01T09:00:00Z",
  "comments": "All devices compliant"
}
```

- **Example response**:
```json
{
  "controlId": "AC.1.001",
  "status": "compliant",
  "evaluatedAt": "2025-12-01T09:05:00Z",
  "details": {
    "evidenceIds": ["EVID-001","EVID-002"],
    "comments": "All devices compliant"
  }
}
```

🚀 Status

Calyptor is currently in R&D phase, with architecture, workflows, and prototypes being documented for future development.

Stay tuned for further updates — or reach out to collaborate.
