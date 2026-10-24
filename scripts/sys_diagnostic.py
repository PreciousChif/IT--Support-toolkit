#!/usr/bin/env python3
import shutil
import psutil
import socket
import sys

def check_disk_space():
    print("--- Disk Space Check ---")
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
    percent_free = (free / total) * 100
    if percent_free < 10:
        print("WARNING: Low disk space!")
    else:
        print("Disk space is healthy.\n")

def check_memory():
    print("--- Memory Usage Check ---")
    mem = psutil.virtual_memory()
    print(f"Total RAM: {mem.total // (2**20)} MB")
    print(f"Available RAM: {mem.available // (2**20)} MB")
    print(f"Memory Usage: {mem.percent}%\n")

def check_network():
    print("--- Network Connectivity Check ---")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet Connection: OK (Connected to 8.8.8.8)\n")
    except OSError:
        print("WARNING: No internet connection detected.\n")

if __name__ == "__main__":
    print("=== IT Support System Diagnostic Tool ===")
    check_disk_space()
    check_memory()
    check_network()
