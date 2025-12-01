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
        CD --> CTE["Contro]()
