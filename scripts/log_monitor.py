#!/usr/bin/env python3
import os
import sys
import subprocess

LOG_PATHS = [
    "/var/log/auth.log",
    "/var/log/secure",
]

def find_auth_log():
    for path in LOG_PATHS:
        if os.path.exists(path):
            return path
    return None

def get_journal_logs():
    """Fetches authentication-related logs using systemd journalctl"""
    try:
        # Query systemd journal for priority logs or auth messages
        result = subprocess.run(
            ["journalctl", "-p", "notice", "-n", "50", "--no-pager"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.splitlines()
    except Exception as e:
        print(f"[-] Could not read from journalctl: {e}")
        return []

def parse_logs(log_source, is_journal=False):
    failed_attempts = []
    
    if is_journal:
        for line in log_source:
            if any(keyword in line.lower() for keyword in ["failed", "invalid", "auth failure", "error"]):
                failed_attempts.append(line.strip())
    else:
        try:
            with open(log_source, "r") as file:
                for line in file:
                    if "Failed password" in line or "authentication failure" in line:
                        failed_attempts.append(line.strip())
        except PermissionError:
            print(f"[-] Permission denied accessing {log_source}.")
            print("[!] Please run the script with sudo privileges.")
            sys.exit(1)
        except Exception as e:
            print(f"[-] Error reading log file: {e}")
            sys.exit(1)
            
    return failed_attempts

def main():
    print("==========================================")
    print("      IT Support Log Monitor Utility      ")
    print("==========================================")
    
    log_path = find_auth_log()
    is_journal = False
    
    if log_path:
        print(f"[+] Scanning log file: {log_path}\n")
        logs = log_path
    else:
        print("[*] No flat log files found. Falling back to systemd journal...")
        is_journal = True
        logs = get_journal_logs()
        if not logs:
            print("[-] Error: Unable to retrieve logs from journalctl.")
            sys.exit(1)
        print("[+] Successfully queried system journal.\n")
        
    failed_logins = parse_logs(logs, is_journal=is_journal)
    
    if not failed_logins:
        print("[+] No failed login or suspicious security events found in recent logs!")
    else:
        print(f"[!] Total relevant events detected: {len(failed_logins)}")
        print("\n--- Recent Events (Last 5) ---")
        for entry in failed_logins[-5:]:
            print(f"  • {entry}")
            
    print("\n==========================================")
    print("[+] Log inspection complete.")
    print("==========================================")

if __name__ == "__main__":
    main()
