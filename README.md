# DRYRUN – Red Team Attack Simulator

**DRYRUN** is an interactive, CTF-style **red team attack simulation framework** designed for learning, practice, and demonstration of **adversary tradecraft** across **endpoint, Active Directory, and cloud environments** — **without executing real attacks**.

The project emphasizes **attack-chain logic, detection mapping, and defensive understanding**, rather than exploitation or payload delivery.

---

## Key Objectives

- Simulate real-world red team attack paths safely
- Map offensive actions to **MITRE ATT&CK**
- Improve **blue team detection visibility**
- Support **CTF labs, SOC training, interviews, and demos**

---

## Key Features

- Interactive, menu-driven attack chain selection
- CTF-style simulations (logic-only, no payloads)
- MITRE ATT&CK–aligned techniques
- Full attack-chain coverage:
  - Initial Access
  - Lateral Movement
  - Exfiltration
  - Active Directory
  - Cloud
- MITRE Navigator layer export
- NIST-style risk scoring
- Windows Event ID mapping for detection context
- Persistent execution (tool does not exit after one run)
- Clean red-team themed **DRYRUN** banner

---

## Attack Chain Coverage

### 1. Initial Access
- **MITRE Techniques:** `T1059`, `T1566`, `T1204`
- **Example Windows Events:** `4688`, `4624`
- OPSEC-aware risk scoring

---

### 2. Lateral Movement
- **MITRE Techniques:** `T1021`, `T1080`
- **Example Windows Events:** `4624`, `4672`

---

### 3. Exfiltration
- **MITRE Techniques:** `T1041`, `T1567`
- **Example Windows Events:** `5156`, `4663`

---

### 4. Active Directory Attack Path
- Kerberoasting
- DCSync
- Golden Ticket logic
- **Windows Events:** `4769`, `4662`, `4673`

---

### 5. Cloud Attack Path
- IAM privilege escalation
- Token abuse
- Storage exfiltration
- Cloud audit log mapping

---

## Project Structure

dryrun/
├── dryrun.py # Main interactive launcher
├── core/
│ ├── initial_access.py
│ ├── lateral.py
│ ├── exfil.py
│ ├── ad_attack.py
│ └── cloud_attack.py
├── mitre/
│ └── navigator.py # MITRE Navigator export
├── scoring/
│ └── nist.py # Risk scoring engine
├── output/
│ ├── report.txt
│ └── navigator_layer.json
├── README.md
└── .gitignore



---

## Installation

### Requirements
- Python **3.8+**
- Linux / macOS / Windows  
  *(Tested on Linux)*

### Clone the Repository
```bash
git clone https://github.com/<your-username>/DRYRUN.git
cd DRYRUN
```
### How to run
```bash
python3 dryrun.py
```
You will see the DRYRUN banner followed by an interactive menu.

### Interactive Menu
Select Attack Chain:

1. Initial Access
2. Lateral Movement
3. Exfiltration
4. Active Directory Attack Path
5. Cloud Attack Path
0. Exit
   
- Select any option to simulate that attack chain

- After execution, the tool returns to the menu

- Use 0 to exit cleanly

  ### Example Output

  [+] Executing: Initial Access
[+] T1059 | Risk: 0.8 | OPSEC: LOW – Stealthy

[✓] Simulation Complete
[✓] Report saved → output/report.txt
[✓] MITRE Navigator → output/navigator_layer.json

### Generated Artifacts
## Report

**Location:** output/report.txt

Includes:

- Attack chain summary

- MITRE techniques

- Risk score

- Windows Event IDs

- Detection notes

### MITRE Navigator

**File:** output/navigator_layer.json

Import directly into **MITRE ATT&CK Navigator**

### Intended Use

- Red team learning and practice

- Blue team detection training

- SOC analyst education

- CTF-style labs

- Demonstrations and seminars

- Interview preparation (attack-chain reasoning)

### Safety & Ethics

- No real attacks

- No exploitation

- No persistence mechanisms

- No payload delivery

**DRYRUN simulates logic only. Use responsibly.**

### Roadmap (Planned)

- Persistent scoring system

- Blue-team detection simulator

- YAML-based attack plans

- ATT&CK heatmap scoring

- CI testing

- CALDERA-style extensions

### License

MIT License

### Author

**RameshKannan**
Red Team | Networking | Security Research
  
---
