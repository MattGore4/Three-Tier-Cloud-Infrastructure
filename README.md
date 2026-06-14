# Secure Multi-Tier Cloud Infrastructure & IT Knowledge Base

## 📌 Project Overview
[cite_start]This repository showcases a highly secure, multi-tier cloud infrastructure built on AWS to host an AI-driven IT Knowledge Base application[cite: 1, 10]. [cite_start]The environment features rigorous network isolation, high availability, and strict zero-trust access controls to protect data integrity and prevent unauthorized system access[cite: 9, 15, 16, 17].

[cite_start]Originally designed with key-value lookups in mind, the database tier was pivoted from DynamoDB to an **Amazon OpenSearch** cluster[cite: 94, 95, 96]. [cite_start]This architectural shift enables full natural language processing and advanced document retrieval capabilities, delivering search query results in an impressive **22ms**[cite: 74, 96, 83].

### Key Highlights:
* [cite_start]**Multi-Tier Architecture:** Complete separation of concerns across a web tier (Apache reverse proxy), application tier (FastAPI/Uvicorn), and data tier (Amazon OpenSearch)[cite: 10, 12, 13, 14].
* [cite_start]**High Availability:** Integrated an Application Load Balancer (ALB) and dual Auto Scaling Groups (ASG) across multiple Availability Zones to ensure automatic failover and traffic distribution[cite: 15, 16, 62].
* [cite_start]**Zero-Trust Network Isolation:** Tight Security Group configurations that block lateral movement between servers and eliminate direct public exposure of backend resources[cite: 19, 34, 47].
* [cite_start]**Secure Remote Administration:** Hardened remote access via a dedicated Bastion Host using custom ED25519 key pairs and SSH Agent Forwarding[cite: 18, 118, 119].

---

## 📐 Architecture Diagram

> ⚠️ *Note: Update your .drawio file to fix the OpenSearch location (ensuring it sits inside the Private Subnet, with the arrow pointing from the App Server to OpenSearch) before uploading your final diagram image here.*

![AWS Cloud Architecture](images/architecture-diagram.png)

### Architectural Flow:
1. [cite_start]**Ingress:** Public web traffic enters through the Internet Gateway and is received by the Public Application Load Balancer (ALB)[cite: 9, 15, 60].
2. [cite_start]**Web Tier:** The ALB distributes traffic across an Auto Scaling Group of Web Servers running Apache as a reverse proxy[cite: 12, 15, 16].
3. [cite_start]**Application Tier:** Web servers forward requests to the Private Subnet Application Tier, where custom Python business logic runs via FastAPI and Uvicorn[cite: 9, 13, 50, 109].
4. [cite_start]**Data Tier:** The App Tier securely queries an Amazon OpenSearch cluster protected by Fine-Grained Access Control (FGAC) and IAM[cite: 14, 54, 116].
5. [cite_start]**Egress & Management:** Private instances route outbound traffic securely via a custom Linux NAT instance[cite: 9, 104, 105]. [cite_start]Administrators access internal nodes via a hardened Bastion Host utilizing separate ED25519 key pairs[cite: 18, 118].

---

## 🛠️ Technology Stack
* [cite_start]**Cloud Provider:** Amazon Web Services (VPC, EC2, ALB, ASG, OpenSearch, CloudTrail, CloudWatch, S3, IAM) [cite: 9, 14, 15, 16, 20, 90]
* [cite_start]**Web Server / Proxy:** Apache [cite: 12, 108]
* [cite_start]**Application Backend:** Python, FastAPI, Uvicorn [cite: 13, 109]
* [cite_start]**Database Engine:** Amazon OpenSearch (with FGAC) [cite: 14, 116]

---

## 🔒 Security Hardening & Verification Testing

[cite_start]Security was integrated as a structural requirement from day one[cite: 17]. The following verification tests prove the efficacy of the infrastructure's protective layers:

| Target Component | Test Undertaken | Expected Behavior | Verification Status |
| :--- | :--- | :--- | :--- |
| **Bastion Host** | [cite_start]Remote Access Tunneling [cite: 23] | [cite_start]Secure traffic proxying to internal subnets via `ProxyCommand`[cite: 25, 26]. | [cite_start]**SUCCESS** [cite: 24] |
| **Subnet Isolation** | [cite_start]Direct public connection to App Server [cite: 27, 29] | [cite_start]Immediate connection timeout from external IPs[cite: 30]. | [cite_start]**SUCCESS** [cite: 28] |
| **Web Tier Direct Access** | [cite_start]Direct HTTP connection bypass to Web Server [cite: 31, 33] | Request dropped; [cite_start]Web servers only accept traffic from the ALB[cite: 34]. | [cite_start]**SUCCESS** [cite: 32] |
| **Lateral Movement** | [cite_start]Compromised Web Server SSH attempt to App Server [cite: 43, 45] | Connection timeout; [cite_start]App server strictly limits SSH ingress to the Bastion[cite: 46, 47]. | [cite_start]**SUCCESS** [cite: 44] |
| **Database Access** | [cite_start]Deep Web-to-Database isolation check [cite: 56, 58] | Web server direct queries fail; [cite_start]OpenSearch only permits authenticated App Server traffic[cite: 55, 58]. | [cite_start]**SUCCESS** [cite: 57] |

---

## 📈 Engineering Reflection & Evolution
* [cite_start]**The DynamoDB to OpenSearch Pivot:** Initial architectural drafts planned for AWS DynamoDB[cite: 95]. [cite_start]However, production constraints revealed that DynamoDB's key-value structure is suboptimal for fuzzy, natural language document lookups[cite: 95, 96]. [cite_start]Pivoting to Amazon OpenSearch allowed the application to index rich text documents smoothly, lowering document query retrieval speeds to **22ms** (well under the initial 300ms design goal)[cite: 74, 83, 96].
* [cite_start]**Rule Tightening Post-Deployment:** During the building phase, Security Group rules were intentionally left relaxed to facilitate straightforward testing and rapid iterative debugging[cite: 97]. [cite_start]Moving into the formal validation phase, a security hardening pass was executed to tighten ingress rules, ensuring that instances reject any traffic not explicitly authorized by the multi-tier communications model[cite: 93, 98, 99].
