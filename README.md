# Three-Tier Cloud Infrastructure

## Project Overview
For this project, I designed and implemented AWS infrastructure to support a Three-Tier Knowledge Base application, with a significant emphasis on establishing a scalable and secure cloud environment. The architecture enforces strict separation of concerns across independent web, app, and database layers, with the web layer distributed across multiple Availability Zones for high availability. Adhering to the principle of zero-trust, the backend application and data tiers are entirely isolated within private subnets, using tightly scoped Security Groups to prevent lateral movement and eliminate public exposure. 

### Key Highlights
* **Three-Tier Architecture:** Complete separation of concerns across a web layer (Apache reverse proxy), application layer (FastAPI/Uvicorn), and data layer (Amazon OpenSearch).
* **High Availability:** Integrated an Application Load Balancer (ALB) and dual Auto Scaling Groups (ASG) to ensure traffic distribution and automatic failover.
* **Zero-Trust Network Isolation:** Tight Security Group configurations that block lateral movement between servers and eliminate direct public exposure of backend resources.
* **Secure Remote Administration:** Hardened remote access via a dedicated Bastion Host using ED25519 key pairs and SSH Agent Forwarding.

---

## Video Demo
[![Watch the Video](https://img.shields.io/badge/YouTube-Video%20Demo-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=xJTUMeXwDw0)

---

## Architecture Diagram
<p align="center">
  <img src="images/Three-Tier-Cloud-Infrastructure.drawio.svg" alt="Three-Tier Cloud Infrastructure Architecture Diagram" width="1300" height="1000">
</p>

---

## Architectural Flow
1. **Ingress:** Public web traffic enters through the Internet Gateway and is received by the Public Application Load Balancer (ALB).
2. **Web Tier:** The ALB distributes traffic across an Auto Scaling Group of Web Servers running Apache as a reverse proxy.
3. **Application Tier:** Web servers forward requests to the Private Subnet Application layer, where custom Python business logic runs via FastAPI and Uvicorn.
4. **Data Tier:** The App Tier securely queries an Amazon OpenSearch cluster protected by Fine-Grained Access Control (FGAC) and IAM.
5. **Egress and Administration:** Private instances route outbound traffic securely via a custom Linux NAT instance. Administrators access internal nodes via a Bastion Host utilizing separate ED25519 key pairs.

---

## Technology Stack
* **Cloud Provider:** Amazon Web Services (VPC, EC2, ALB, ASG, OpenSearch, CloudTrail, CloudWatch, S3, IAM)
* **Web Server / Proxy:** Apache
* **Application Backend:** Python, FastAPI, Uvicorn
* **Database Engine:** Amazon OpenSearch (with FGAC)
* **NAT Instance:** fck-NAT (open-source NAT Gateway software)

---

## Verification Testing
The following verification tests prove the efficiency, security, and scalability of the infrastructure.

| Test Component / Scenario | Expected Behavior | Verification Status |
| :--- | :--- | :--- |
| **Bastion Host:** Remote Access Tunneling | Secure traffic entering internal subnets via SSH from an external PC. | **SUCCESS** |
| **Subnet Isolation:** Direct public connection to App Server | Immediate connection timeout message. | **SUCCESS** |
| **Web Tier Direct Access:** Direct HTTP connection bypass to Web Server | Request dropped; Web servers only accept traffic from the ALB. | **SUCCESS** |
| **Lateral Movement:** Compromised Web Server SSH attempt to App Server | Connection timeout; App server strictly limits SSH ingress to the Bastion. | **SUCCESS** |
| **Database Access:** Web Server to OpenSearch isolation check | Web server direct queries fail; OpenSearch only permits authenticated App Server traffic. | **SUCCESS** |
| **Application Load Balancer:** Traffic distribution check | ALB balances web traffic to both Web servers. | **SUCCESS** |
| **Instance Self-Healing:** EC2 instance health detection and recovery | After terminating an instance, the ALB detects an unhealthy instance, and the ASG automatically deploys a replacement instance. | **SUCCESS** |
