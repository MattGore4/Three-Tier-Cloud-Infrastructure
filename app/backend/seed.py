import os
import sys
from opensearchpy import OpenSearch, RequestsHttpConnection

#Load in the OpenSearch credentials for environment variables
OPENSEARCH_HOST = os.environ.get("OPENSEARCH_HOST")
OPENSEARCH_USER = os.environ.get("OPENSEARCH_USER")
OPENSEARCH_PASS = os.environ.get("OPENSEARCH_PASS")
DOCS_INDEX = os.environ.get("DOCS_INDEX", "acme-docs")

# Initialize OpenSearch Client connection
client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST, 'port': 443}],
    http_auth=(OPENSEARCH_USER, OPENSEARCH_PASS),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# Define the OpenSearch Index structure
index_body = {
    'settings': {
        'index': {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }
    },
    'mappings': {
        'properties': {
            'title': {'type': 'text', 'analyzer': 'standard'},
            'category': {'type': 'keyword'},
            'content': {'type': 'text', 'analyzer': 'standard'}
        }
    }
}

# 20 Deep technical documents with Markdown formatting pre-baked inside
twenty_tech_docs = [
    {
        "title": "Resolving Git Merge Conflicts",
        "category": "Troubleshooting Guides",
        "content": """### Overview
Merge conflicts occur when competing alterations are executed on the identical line of a tracking file.

### Step-by-Step Resolution
1. **Identify Conflict Files:** Run `git status` to locate unmerged paths.
2. **Isolate Code Flags:** Open target files and inspect conflict boundaries highlighted between `<<<<<<< HEAD` and `>>>>>>>` strings.
3. **Reconcile Text:** Manually select or combine lines to form correct code blocks.
4. **Commit Changes:** Execute `git add .` followed by `git commit -m 'Resolved merge conflict'` to lock in fix states."""
    },
    {
        "title": "Docker Container DNS Resolution Failures",
        "category": "Troubleshooting Guides",
        "content": """### Symptom
Containers fail to communicate out to external internet APIs or local internal cluster endpoints.

### Root Causes
* Corrupted system `resolv.conf` inherited network loops.
* Tailored container network configurations dropped by host system firewalls.

### Fix Actions
* **Step 1:** Force static external resolvers during container initialization via execution switches:
  `docker run --dns=8.8.8.8 target_image`.
* **Step 2:** Inspect host forwarding interfaces using Linux systems properties command lines `sysctl net.ipv4.ip_forward`."""
    },
    {
        "title": "SSH Connection Timeout Diagnostics",
        "category": "Troubleshooting Guides",
        "content": """### Problem Description
Attempts to connect remotely to hosted cloud compute instances stall out with a `Connection timed out` string feedback.

### Triage Matrix
* **Check 1: Security Groups:** Confirm public ports configurations for TCP **Port 22** accept entries matching current local public source IP metrics.
* **Check 2: Network Paths:** Ensure server placements fall cleanly into public routing contexts bound to attached Internet Gateways.

### Verification Test
Run network connectivity evaluation utilities on terminal inputs: `nc -zv <TARGET_IP> 22`."""
    },
    {
        "title": "Linux Disk Space Exhaustion via Inodes",
        "category": "Troubleshooting Guides",
        "content": """### Phenomenon
Storage calls drop write signals reporting `No space left on device`, but standard file utilities like `df -h` show ample gigabytes remaining.

### Explanation
The storage environment has exhausted its allocation of **Inodes** (index pointers) due to a surplus of tiny log files or execution caches.

### Fix Commands
* Find Inode distribution matrix mapping: `df -i`.
* Locate directory blocks hoarding immense item counts via parsing loops:
  `find / -xdev -type d -size +100k`."""
    },
    {
        "title": "Fixing Nginx 502 Bad Gateway Blocks",
        "category": "Troubleshooting Guides",
        "content": """### Context
Nginx proxy borders successfully listen to internet visits but reject forwarding calls by returning explicit HTTP status errors.

### Diagnostics Path
* **Review Backend Services:** Ensure your core application runtime engines (like Uvicorn, Gunicorn, or PHP-FPM) are actively execution-ready.
* **Examine Configuration Blocks:** Verify upstream proxy lines match processing sockets precisely:
  `proxy_pass http://127.0.0.1:8000;`."""
    },
    {
        "title": "Database Connection Pool Exhaustion Recovery",
        "category": "Troubleshooting Guides",
        "content": """### Failure Mode
Applications freeze or throw fatal database connectivity exceptions under sudden multi-user scaling stress.

### Root Cause Analysis
Backend worker threads open transaction channels without executing mandatory `.close()` cleanups, leaving channels locked down indefinitely.

### Corrective Steps
1. **Modify Context Closures:** Ensure code calls deploy contextual context tools like `with` parameters to wrap queries.
2. **Scale DB Capacity:** Bump parameters governing max transactional concurrency inside active engine configurations (`max_connections = 200`)."""
    },
    {
        "title": "Cron Job Task Execution Failures",
        "category": "Troubleshooting Guides",
        "content": """### Symptoms
Configured automated background cron configurations display proper entry structures inside task scheduling files but refuse to execute.

### Solutions
* **Use Absolute System Paths:** Cron layouts run inside highly bare environments. Commands must write out total pathways (e.g., `/usr/bin/python3` instead of simply `python3`).
* **Capture Error Logs:** Redirect outputs to active text logs to catch debug statements: `* * * * * /path/script.sh >> /var/log/cron_err.log 2>&1`."""
    },
    {
        "title": "Kubernetes Pod CrashLoopBackOff Errors",
        "category": "Troubleshooting Guides",
        "content": """### Definition
Kubernetes schedules a pod environment deployment, but the internal application container exits immediately upon initialization, causing endless boot loops.

### Isolation Steps
1. **Fetch Container Metrics:** Run `kubectl describe pod <pod_name>` to extract lifecycle error indicators.
2. **Inspect Runtime Trace output:** Execute `kubectl logs <pod_name> --previous` to analyze application crash logs before the last container termination event."""
    },
    {
        "title": "Redis Cache Eviction Inefficiencies",
        "category": "Troubleshooting Guides",
        "content": """### Issue
Memory utilization metrics on target caching servers max out, degrading latency performance.

### Corrections Plan
* **Set Explicit TTL Limits:** Ensure write parameters specify strict expiry values.
* **Adjust Eviction Policies:** Update system instance flags inside configuration files:
  `maxmemory-policy volatile-lru` (Evicts least-recently-used records holding expirations)."""
    },
    {
        "title": "Application Memory Management and OOM Killer",
        "category": "Troubleshooting Guides",
        "content": """### Scenario
Heavy execution workers suddenly stop entirely with system termination labels pointing to error exit codes `137`.

### Explanation
The host system kernel triggered its **OOM (Out Of Memory) Killer** program to terminate the backend process to prevent complete OS instability.

### Mitigation
* Review log timelines inside tracking blocks: `dmesg -T | grep -i oom`.
* Adjust memory constraints inside runtime engines or add dedicated swap space allocations to buffer processing spikes."""
    },
    {
        "title": "SSL/TLS Certificate Renewal Process",
        "category": "Process Documentation",
        "content": """### Objective
Standard operating procedure for performing automated updates on web tier SSL encryption certificates.

### Prerequisites
* Root access permissions on edge servers.
* Fully resolved active DNS routing records.

### Execution Protocol
1. Run the generation script command: `sudo certbot --nginx`.
2. Verify automation task validity by calling structural testing paths: `sudo certbot renew --dry-run`.
3. Restart underlying routing software components to reload certificate tracking paths."""
    },
    {
        "title": "AWS IAM Least Privilege Hardening Flow",
        "category": "Process Documentation",
        "content": """### Scope
Defines validation standards to isolate cloud environment configuration roles away from insecure root privilege mappings.

### Operational Rules
* **Rule A:** No engineering credentials may assign wildcard rights (`*`) to open permissions fields.
* **Rule B:** Multi-Factor Authentication (MFA) enforcement policies must wrap all administrative policy keys.

### Audit Routine
Execute identity reporting evaluations monthly via AWS CLI: `aws iam generate-credential-report`."""
    },
    {
        "title": "Production Deployment Safety Protocol",
        "category": "Process Documentation",
        "content": """### Scope
Pre-flight checks mandatory for all engineers pushing changes out to live system architectures.

### Phase Alpha: Isolation Check
* Run automated regression suites against staging deployments.
* Validate database migration scripts support safe backward-compatibility states.

### Phase Beta: Execution Control
* Deploy components via **Canary updates**, routing only **10%** of live volume to new code blocks initially.
* Keep roll-back command scripts open in terminal screens for rapid reversal if telemetry displays error increases."""
    },
    {
        "title": "Data Breach Incident Response Workflow",
        "category": "Process Documentation",
        "content": """### Purpose
Defines the step-by-step action plan to execute the second an unverified or adversarial entity gains access to data stores.

### Phase 1: Containment
* Isolate affected database assets by revoking compromised network routes.
* Terminate leaked credential keys instantly inside IAM structures.

### Phase 2: Analysis
* Extract connection logs and data tables access footprints to trace compromised parameters.
* Map impacted records to comply with regulatory notification reporting timelines."""
    },
    {
        "title": "Server Decommissioning Standard Operating Procedure",
        "category": "Process Documentation",
        "content": """### Summary
Safely deprecate obsolete compute infrastructure blocks without causing dependency fragmentation loops across shared networks.

### Process Flow
1. **Backup Volumes:** Capture system structural snapshots (`AMIs` or block device backups).
2. **Audit Telemetry:** Confirm instance ingress-egress charts read zero active traffic signals for **7 consecutive days**.
3. **De-allocate Resources:** Terminate instances and detach corresponding Elastic IP assets to eliminate idle usage charges."""
    },
    {
        "title": "API Lifecycle Control and Versioning Standards",
        "category": "Process Documentation",
        "content": """### Goal
Maintain continuous software system compatibility across API consumers via structured path management workflows.

### Code Standards
* Major API modifications require path version prefix increments: `/api/v2/search`.
* Keep deprecated routes functional for a minimum window of **180 days** post-deprecation logging.

### Messaging Policy
Include clear `Warning: Deprecated` attributes inside outgoing HTTP processing headers for older routes."""
    },
    {
        "title": "Setting Up Python Virtual Environments",
        "category": "General Tech Information",
        "content": """### Overview
Virtual environments separate external coding packages safely away from global OS system paths.

### Core Architecture
When activated, the current shell overrides its `PATH` environment mapping, forcing local script calls to look inside custom repository folders instead of system root targets.

### Base Lifecycle Controls
* Build local virtual spaces: `python3 -m venv target_env`.
* Inject tracking hooks: `source target_env/bin/activate`.
* Leave environment bounds: `deactivate`."""
    },
    {
        "title": "Understanding HTTP Strict Transport Security (HSTS)",
        "category": "General Tech Information",
        "content": """### Functional Concept
**HSTS** is a web security optimization protocol sent inside HTTP headers that instructs web browsers to only interact with the target domain using secure HTTPS links.

### Technical Values
```text
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

### Security Value
This preventively neutralizes SSL-stripping attack vectors by forcing clients to construct encryption links locally before data touches public network switches."""
    },
    {
        "title": "Cross-Origin Resource Sharing (CORS) Mechanics",
        "category": "General Tech Information",
        "content": """### Core Logic
**CORS** is an integrated browser security sandbox mechanism that prevents malicious web code running inside a user's browser from making unauthorized requests back to a separate backend domain.

### Execution Flow
When a frontend running on `Domain-A` tries to reach an API on `Domain-B`, the browser automatically fires an HTTP **OPTIONS pre-flight request** to ask the backend if the connection is permitted.

### Essential Response Headers
* `Access-Control-Allow-Origin`
* `Access-Control-Allow-Methods`"""
    },
    {
        "title": "JSON Web Token (JWT) Verification Framework",
        "category": "General Tech Information",
        "content": """### Structure Breakdown
JWT assets serialize client session claims inside structured, base64-encoded strings split into three component parts:
1. **Header:** Identifies signature verification hashing parameters.
2. **Payload:** Contains authorization roles, expirations, and user descriptors.
3. **Signature:** Cryptographically verifies that the token payload was not modified in transit.

### System Security Rule
Backend services do not query database structures to validate JWTs. Instead, they run the incoming token against a local cryptographic secret key to verify data integrity instantly."""
    }
]
#This block avoids accidentally stacking duplicate documents
try:
    # 1. Delete index if it already exists
    if client.indices.exists(index=DOCS_INDEX):
        print(f"Index '{DOCS_INDEX}' found. Dropping it to remove all old documents...")
        client.indices.delete(index=DOCS_INDEX)

    # 2. Recreate index using the mapping settings
    print(f"Rebuilding empty '{DOCS_INDEX}' index...")
    client.indices.create(index=DOCS_INDEX, body=index_body)

    # 3. Stream-ingest all 20 rich documents
    print(f"Ingesting {len(twenty_tech_docs)} fresh records with markdown formatting...")
    for doc in twenty_tech_docs:
        response = client.index(index=DOCS_INDEX, body=doc, refresh=True)
        print(f"Loaded successfully: '{doc['title']}' -> Generated Database ID: {response['_id']}")

    print(f"\n[SUCCESS] OpenSearch cluster now holds only your 20 technology and process docs.")

except Exception as e:
    print(f"Seeding process aborted due to error: {e}")
