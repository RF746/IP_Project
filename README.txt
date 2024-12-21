# IP Address Finder and Validator

## Overview

The **IP Address Finder and Validator** is a Python-based tool that:
- Validates IPv4 and IPv6 addresses using regex.
- Retrieves the public IP address of the device using an external API.
- Displays the local IP address of the device.

This project demonstrates fundamental networking concepts, including IP address formats and network communication.

---

## Features

- **IPv4 and IPv6 Validation**: Ensures entered IP addresses conform to standard formats.
- **Public IP Retrieval**: Uses an external API (`ipify`) to fetch the device's public IP address.
- **Local IP Display**: Retrieves the local IP address of the device using system commands.

---

## Prerequisites

- Python 3.x installed on your system.
- Required Python library:
  - `requests` (Install using: `pip install requests`)

---

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ip-finder-validator.git
   cd ip-finder-validator
