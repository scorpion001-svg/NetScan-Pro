# NetScan-Pro

A lightweight TCP Port Scanner built with Python.

NetScan Pro is a modular networking tool that validates targets, resolves domains, scans TCP ports, and displays results in a clean terminal interface.

---

## Features

- ASCII Banner
- IP / Domain Validation
- DNS Resolution
- Configurable Port Range
- TCP Connect Port Scanning
- Clean Result Display
- Modular Project Structure

---

## Project Structure

```
NetScan-Pro/
│
├── main.py
├── utils.py
├── scanner.py
├── display.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/NetScan-Pro.git
cd NetScan-Pro
```

Run the project:

```bash
python main.py
```

---

## Usage

Example:

```
Target (IP / Domain): scanme.nmap.org

Start port: 20
End port: 100
```

Example Output:

```
==================================================
              NetScan Pro Results
==================================================

Target      : scanme.nmap.org
Resolved IP : xxx.xxx.xxx.xxx

Open Ports
------------------------------
[+] Port 22 OPEN
[+] Port 80 OPEN

==================================================
Scan Completed.
```

---

## Technologies Used

- Python 3
- socket
- ipaddress
- Git
- GitHub

---

## Roadmap

### Version 1.0
- [x] Banner
- [x] Target Validation
- [x] DNS Resolution
- [x] TCP Port Scanner
- [x] Result Display

### Version 1.1
- [ ] Service Detection
- [ ] Colored Output
- [ ] Scan Time
- [ ] Better Error Handling

### Version 2.0
- [ ] Multi-threading
- [ ] Export Scan Results
- [ ] CLI Arguments
- [ ] Progress Indicator

### Version 3.0
- [ ] Banner Grabbing
- [ ] UDP Scan
- [ ] Advanced Scan Modes

---

## Author

Hussien Mohamad

Computer Science Student

---

## License

This project is licensed under the MIT License.
