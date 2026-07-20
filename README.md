# NetScan Pro

A fast, multi-threaded TCP port scanner written in Python with service detection, banner grabbing, progress tracking, and export support.

---
## Features

- Multi-threaded TCP Port Scanning
- Fast / Default / Full Scan Modes
- Custom Port Range
- Domain & IP Address Support
- Automatic DNS Resolution
- Service Detection
- SSH Banner Grabbing
- HTTP Server Detection
- HTTPS Server Detection
- Real-time Progress Indicator
- Colored Terminal Output
- Scan Summary
- Export Results to Text File
- Error Handling & Validation

---

## Preview
## Preview

```text
    _   __     __  _____                     ____
   / | / /__  / /_/ ___/_________ _____     / __ \_________
  /  |/ / _ \/ __/\__ \/ ___/ __ `/ __ \   / /_/ / ___/ __ \
 / /|  /  __/ /_ ___/ / /__/ /_/ / / / /  / ____/ /  / /_/ /
/_/ |_/\___/\__//____/\___/\__,_/_/ /_/  /_/   /_/   \____/

────────────────────────────────────────────────────────────
                Scan Smart. Discover More.
────────────────────────────────────────────────────────────

Target (IP / Domain): scanme.nmap.org

Choose Scan Mode
1. Fast Scan (Ports 1–100)
2. Default Scan (Ports 1–1000)
3. Full Scan (Ports 1–65535)
4. Custom Range

Choice: 3

Scanning Ports:
[██████████████████████████████] 100.0% (65535/65535)
```

### Scan Result

```text
==================================================
              NetScan Pro Results
==================================================

Target      : scanme.nmap.org
Resolved IP : 45.33.32.156

Open Ports (2)
--------------------------------------------------
[+] Port 22
    State   : OPEN
    Service : SSH
    Server  : SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13

[+] Port 80
    State   : OPEN
    Service : HTTP
    Server  : Apache/2.4.7 (Ubuntu)

==================================================
Scan Summary
==================================================

Ports Scanned : 1 - 100
Open Ports    : 2
Scan Time     : 0.35 sec
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/NetScan-Pro.git
```

Move to the project directory:

```bash
cd NetScan-Pro
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the scanner:

```bash
python main.py
```

---

## Scan Modes

| Mode | Description |
|------|-------------|
| Fast | Scan ports 1–100 |
| Default | Scan ports 1–1000 |
| Full | Scan ports 1–65535 |
| Custom | User-defined port range |

---

## Project Structure

```text
NetScan-Pro/
│
├── analyzer.py
├── colors.py
├── display.py
├── export.py
├── main.py
├── progress.py
├── scanner.py
├── services.py
├── utils.py
└── README.md
```

---

## Technologies Used

- Python 3
- socket
- ssl
- concurrent.futures
- colorama

---

## How It Works

1. Validates the target.
2. Resolves the domain name to an IP address.
3. Scans the selected ports using multiple threads.
4. Detects common services.
5. Attempts banner grabbing for supported services.
6. Displays formatted results.
7. Exports the scan results to a text file.

---

## Future Improvements

- UDP Scanning
- CLI Arguments
- JSON Export
- CSV Export
- Operating System Fingerprinting

---

## Author

**Hussein "Scorpion01"**

Computer Science Student

Sadat Academy for Management Sciences

GitHub: https://github.com/scorpion001-svg

LinkedIn: https://www.linkedin.com/in/hussien-mohamad-4a37583b5/
