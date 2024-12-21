import re
import socket
import requests

def validate_ip(ip):
    """Validate whether the given string is a valid IPv4 or IPv6 address."""
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv6_pattern = r"^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|::)$"

    if re.match(ipv4_pattern, ip):
        # Check if each octet is between 0 and 255
        if all(0 <= int(octet) <= 255 for octet in ip.split('.')):
            return "Valid IPv4 address"
    elif re.match(ipv6_pattern, ip):
        return "Valid IPv6 address"
    return "Invalid IP address"

def get_public_ip():
    """Fetch the public IP address of the device."""
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json()["ip"]
    except requests.RequestException as e:
        return f"Error fetching public IP: {e}"

def get_local_ip():
    """Fetch the local IP address of the device."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.gaierror as e:
        return f"Error fetching local IP: {e}"

if __name__ == "__main__":
    print("Welcome to the IP Address Finder and Validator!")
    
    # IP Validation
    ip = input("Enter an IP address to validate: ")
    print(validate_ip(ip))
    
    # Fetch Public IP
    print(f"Your public IP address is: {get_public_ip()}")
    
    # Fetch Local IP
    print(f"Your local IP address is: {get_local_ip()}")
