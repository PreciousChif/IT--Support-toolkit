# IT Support Toolkit 🛠️

A collection of lightweight automation scripts and diagnostic utilities designed to help IT support professionals quickly troubleshoot system health, network connectivity, and resource utilization.

## 🚀 Included Tools

### 1. System Diagnostic Utility (`sys_diagnostic.py`)
A Python command-line utility that checks critical endpoint health metrics.
* **Disk Space Check:** Analyzes root storage and warns if disk space drops below critical thresholds.
* **Memory Usage Check:** Reports total, available, and percentage of RAM currently in use.
* **Network Connectivity Check:** Tests live internet connection and DNS response via reliable external endpoints.

### 2. User Management Utility (`user_manager.sh`)
A Bash script designed to streamline user onboarding on Linux environments.
* **Provisioning:** Creates local user accounts with home directories and bash shells.
* **Security:** Securely prompts for temporary passwords and applies them via `chpasswd`.
* **Privilege Assignment:** Optionally adds newly created accounts to the sudo group.

### 3. System Log Monitor Utility (`log_monitor.py`)
A Python tool for scanning authentication and system logs.
* **Log Discovery:** Automatically checks traditional flat log files (`/var/log/auth.log`, `/var/log/secure`) or falls back to systemd journal logs (`journalctl`).
* **Security Inspection:** Flags failed login attempts or security events to help spot potential unauthorized access.

## 💻 Requirements
* Python 3.x
* Required Python modules: `psutil`
* Bash (for user management script)

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/PreciousChif/it-support-toolkit.git](https://github.com/PreciousChif/it-support-toolkit.git)
