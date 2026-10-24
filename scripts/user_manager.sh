#!/bin/bash

# Ensure script is run with root/sudo privileges
if [ "$EUID" -ne 0 ]; then
  echo "[-] Error: Please run this script using sudo (e.g., sudo ./scripts/user_manager.sh)"
  exit 1
fi

echo "=========================================="
echo "    IT Support User Management Utility    "
echo "=========================================="

# Prompt for username
read -p "Enter the new username to create: " username

# Check if user already exists
if id "$username" &>/dev/null; then
    echo "[-] User '$username' already exists on this system."
    exit 1
fi

# Create the user with a home directory and bash shell
useradd -m -s /bin/bash "$username"
echo "[+] User '$username' created successfully."

# Prompt for password securely
read -s -p "Enter a temporary password for $username: " password
echo
echo "$username:$password" | chpasswd
echo "[+] Password successfully configured."

# Optional group assignment
read -p "Do you want to add $username to the sudo group? (y/n): " add_sudo
if [ "$add_sudo" = "y" ] || [ "$add_sudo" = "Y" ]; then
    usermod -aG sudo "$username"
    echo "[+] User '$username' has been granted sudo privileges."
fi

echo "=========================================="
echo "[+] User provisioning complete for: $username"
echo "=========================================="

