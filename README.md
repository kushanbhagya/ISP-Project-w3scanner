# w3scanner

> A unified desktop GUI for web reconnaissance and vulnerability assessment — powered by WhatWeb, Nmap, and Nikto.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=flat-square)
![License](https://img.shields.io/badge/Use-Educational%20Only-red?style=flat-square)

---

## Overview

**w3scanner** is a Python-based desktop application that brings three industry-standard security tools into a single, easy-to-use graphical interface. Whether you're fingerprinting a website's tech stack, mapping open ports, or scanning a web server for misconfigurations — w3scanner lets you do it all without touching the command line.

Built with **Tkinter** and designed for students, security learners, and authorized testers.

---

## Features

### 🔍 WhatWeb — Technology Fingerprinting
- Detect frameworks, CMS platforms, server software, and more
- Verbose, quiet, and plugin-listing modes
- Clean output displayed directly in the GUI

### 🗺️ Nmap — Network Scanning
- Scan domains or IP addresses for open ports and services
- Select from common scan profiles via dropdown menus
- Customize ports, hosts, and exclusion lists

### 🛡️ Nikto — Web Server Assessment
- Identify common vulnerabilities and misconfigurations
- SSL scanning support
- Configurable port and scan settings

### 🖥️ Desktop GUI
- Built entirely with Tkinter — no browser required
- Tab-based navigation between scanning modules
- Input → Run → Output workflow in one window

---

## Project Structure

```
ISP-Project-w3scanner/
├── 2022_S2_G57/
│   └── ISP-w3scanner/
│       ├── logo.png               # Application logo
│       ├── project3.py            # WhatWeb module
│       ├── project4.py            # Nmap module
│       ├── project5.py            # Nikto module
│       └── tempCodeRunnerFile.py
└── README.md
```

---

## Prerequisites

Make sure the following are installed on your system before running w3scanner:

| Requirement | Notes |
|---|---|
| Python 3 | [python.org](https://www.python.org/) |
| pip | Comes with Python 3.4+ |
| WhatWeb | [github.com/urbanadventurer/WhatWeb](https://github.com/urbanadventurer/WhatWeb) |
| Nmap | [nmap.org](https://nmap.org/) |
| Nikto | [github.com/sullo/nikto](https://github.com/sullo/nikto) |
| Pillow | Install via pip (see below) |

> **Note:** Tkinter is bundled with most Python installations. On some Linux systems, install it separately with `sudo apt install python3-tk`.

---

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/kushanbhagya/ISP-Project-w3scanner.git
cd ISP-Project-w3scanner/2022_S2_G57/ISP-w3scanner
```

**2. Install the Python dependency:**

```bash
pip install pillow
```

---

## Usage

Launch the application with:

```bash
python3 project3.py
```

This opens the main GUI window. From there you can switch between:

- **WhatWeb** — enter a URL and select scan options
- **Nmap** — enter a target and choose your scan type
- **Nikto** — configure and run a web server scan

Scan output is displayed directly within the application window.

---

## Example Use Cases

- Identify the CMS, server, and JavaScript libraries used by a website
- Discover open ports and running services on a host
- Check a web server for outdated software or common misconfigurations
- Learn how security tools can be integrated into a single Python application

---

## Tech Stack

- **Python 3** — Core language
- **Tkinter** — GUI framework
- **Pillow** — Image handling for the GUI
- **WhatWeb** — Web technology fingerprinting
- **Nmap** — Network discovery and port scanning
- **Nikto** — Web server vulnerability scanning

---

## Roadmap

- [ ] Better output formatting and syntax highlighting
- [ ] Export scan results to `.txt` or `.pdf`
- [ ] Input validation and improved error handling
- [ ] Enhanced GUI with theming support
- [ ] Package as a standalone cross-platform desktop app

---

## ⚠️ Disclaimer

This tool is intended **strictly for educational purposes and authorized security testing only**.

Do **not** scan systems, networks, or websites without explicit written permission from the owner. Unauthorized scanning may be illegal and unethical.

---

## Author

**Kushan Bhagya**

If you found this project useful, consider ⭐ starring the repository on GitHub.
