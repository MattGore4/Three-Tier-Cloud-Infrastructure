<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Three-Tier Cloud Infrastructure README</title>
    <style>
        :root {
            --primary-color: #1e293b;
            --secondary-color: #3b82f6;
            --text-color: #334155;
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --success-bg: #dcfce7;
            --success-text: #166534;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 40px 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.05);
            border: 1px solid var(--border-color);
        }

        h1 {
            color: var(--primary-color);
            font-size: 2.5rem;
            margin-top: 0;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 15px;
        }

        h2 {
            color: var(--primary-color);
            font-size: 1.75rem;
            margin-top: 35px;
            margin-bottom: 15px;
            border-left: 4px solid var(--secondary-color);
            padding-left: 12px;
        }

        h3 {
            color: var(--primary-color);
            font-size: 1.25rem;
            margin-top: 20px;
        }

        p {
            margin-bottom: 20px;
            text-align: justify;
        }

        ul, ol {
            padding-left: 25px;
            margin-bottom: 25px;
        }

        li {
            margin-bottom: 10px;
        }

        strong {
            color: #0f172a;
        }

        /* Video Demo Button */
        .video-btn {
            display: inline-flex;
            align-items: center;
            background-color: #ef4444;
            color: white;
            text-decoration: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: 6px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 25px;
            transition: background-color 0.2s ease;
        }

        .video-btn:hover {
            background-color: #dc2626;
        }

        .video-btn svg {
            margin-right: 8px;
            fill: currentColor;
        }

        /* Note Callout Box */
        .note-box {
            background-color: #f0fdf4;
            border-left: 4px solid #22c55e;
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 0 6px 6px 0;
            font-size: 0.95rem;
        }

        /* Tech Stack Grid/List */
        .tech-stack-list {
            list-style: none;
            padding: 0;
        }

        .tech-stack-list li {
            padding: 10px 15px;
            background: #f1f5f9;
            margin-bottom: 8px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
        }

        /* Verification Table styling */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            margin-bottom: 30px;
            font-size: 0.95rem;
        }

        th {
            background-color: var(--primary-color);
            color: white;
            text-align: left;
            padding: 12px 16px;
            font-weight: 600;
        }

        td {
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-color);
            vertical-align: top;
        }

        tr:nth-child(even) {
            background-color: #f8fafc;
        }

        .status-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .status-success {
            background-color: var(--success-bg);
            color: var(--success-text);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            body {
                padding: 20px 10px;
            }
            .container {
                padding: 20px;
            }
            th, td {
                padding: 10px;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Three-Tier Cloud Infrastructure</h1>
    
    <h2>Project Overview</h2>
    <p>For this project, I designed and implemented AWS infrastructure to support a Three-Tier Knowledge Base application, with a significant emphasis on establishing a scalable and secure cloud environment. The architecture enforces strict separation of concerns across independent web, app, and database layers, with the web layer distributed across multiple Availability Zones for high availability. Adhering to the principle of zero-trust, the backend application and data tiers are entirely isolated within private subnets, using tightly scoped Security Groups to prevent lateral movement and eliminate public exposure.</p>
    
    <h2>Key Highlights</h2>
    <ul>
        <li><strong>Three-Tier Architecture:</strong> Complete separation of concerns across a web layer (Apache reverse proxy), application layer (FastAPI/Uvicorn), and data layer (Amazon OpenSearch).</li>
        <li><strong>High Availability:</strong> Integrated an Application Load Balancer (ALB) and dual Auto Scaling Groups (ASG) to ensure traffic distribution and automatic failover.</li>
        <li><strong>Zero-Trust Network Isolation:</strong> Tight Security Group configurations that block lateral movement between servers and eliminate direct public exposure of backend resources.</li>
        <li><strong>Secure Remote Administration:</strong> Hardened remote access via a dedicated Bastion Host using ED25519 key pairs and SSH Agent Forwarding.</li>
    </ul>

    <h2>Video Demo</h2>
    <a href="https://www.youtube.com/watch?v=xJTUMeXwDw0" target="_blank" class="video-btn">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 4-8 4z"/></svg>
        Watch Video Demo
    </a>

    <h2>Architecture Diagram</h2>
    <div class="note-box">
        <strong>Note:</strong> Update your <code>.drawio</code> file to fix the OpenSearch location (ensuring it sits inside the Private Subnet, with the arrow pointing from the App Server to OpenSearch) before uploading your final diagram image here.
    </div>

    <h2>Architectural Flow</h2>
    <ol>
        <li><strong>Ingress:</strong> Public web traffic enters through the Internet Gateway and is received by the Public Application Load Balancer (ALB).</li>
        <li><strong>Web Tier:</strong> The ALB distributes traffic across an Auto Scaling Group of Web Servers running Apache as a reverse proxy.</li>
        <li><strong>Application Tier:</strong> Web servers forward requests to the Private Subnet Application layer, where custom Python business logic runs via FastAPI and Uvicorn.</li>
        <li><strong>Data Tier:</strong> The App Tier securely queries an Amazon OpenSearch cluster protected by Fine-Grained Access Control (FGAC) and IAM.</li>
        <li><strong>Egress and Administration:</strong> Private instances route outbound traffic securely via a custom Linux NAT instance. Administrators access internal nodes via a Bastion Host utilizing separate ED25519 key pairs.</li>
    </ol>

    <h2>Technology Stack</h2>
    <ul class="tech-stack-list">
        <li><strong>Cloud Provider:</strong> Amazon Web Services (VPC, EC2, ALB, ASG, OpenSearch, CloudTrail, CloudWatch, S3, IAM)</li>
        <li><strong>Web Server / Proxy:</strong> Apache</li>
        <li><strong>Application Backend:</strong> Python, FastAPI, Uvicorn</li>
        <li><strong>Database Engine:</strong> Amazon OpenSearch (with FGAC)</li>
        <li><strong>NAT Instance:</strong> fck-NAT (open-source NAT Gateway software)</li>
    </ul>

    <h2>Verification Testing</h2>
    <p>The following verification tests prove the efficiency, security, and scalability of the infrastructure.</p>
    
    <table>
        <thead>
            <tr>
                <th>Test Component / Scenario</th>
                <th>Expected Behavior</th>
                <th>Verification Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Bastion Host:</strong> Remote Access Tunneling</td>
                <td>Secure traffic entering internal subnets via SSH from an external PC.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
            <tr>
                <td><strong>Subnet Isolation:</strong> Direct public connection to App Server</td>
                <td>Immediate connection timeout message.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
            <tr>
                <td><strong>Web Tier Direct Access:</strong> Direct HTTP connection bypass to Web Server</td>
                <td>Request dropped; Web servers only accept traffic from the ALB.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
            <tr>
                <td><strong>Lateral Movement:</strong> Compromised Web Server SSH attempt to App Server</td>
                <td>Connection timeout; App server strictly limits SSH ingress to the Bastion.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
            <tr>
                <td><strong>Database Access:</strong> Web Server to OpenSearch isolation check</td>
                <td>Web server direct queries fail; OpenSearch only permits authenticated App Server traffic.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
            <tr>
                <td><strong>Application Load Balancer:</strong> Traffic distribution check</td>
                <td>ALB balances web traffic to both web servers.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
            <tr>
                <td><strong>Instance Self-Healing:</strong> EC2 instance health detection and automated recovery</td>
                <td>After terminating an instance, the ALB detects an unhealthy instance, and the ASG automatically deploys a replacement instance.</td>
                <td><span class="status-badge status-success">Success</span></td>
            </tr>
        </tbody>
    </table>
</div>

</body>
</html>
