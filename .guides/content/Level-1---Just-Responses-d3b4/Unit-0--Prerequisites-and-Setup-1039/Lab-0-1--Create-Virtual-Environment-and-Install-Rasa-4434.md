
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Create a virtual environment in the **project root**, install Rasa at version `3.16.3`, configure `RASA_LICENSE`, and confirm everything works. Complete this before any other lab.
 

---
 
**1. Check Python and pip**
 
```bash
python --version
pip --version
```
 
Expect Python 3.10+ and pip. If Python is missing:
 
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```
 
If pip is missing but Python is present:
 
```bash
python3.11 -m ensurepip --upgrade
```
 
**2. Create and activate the virtual environment**
 
Confirm you are in the project root (`pwd` should not end in `level1`), then:
 
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```
 
Your prompt should show `(.venv)`.
 
**3. Install Rasa**
 
```bash
pip install --no-cache-dir rasa-pro==3.16.3
```
 
Grab a coffee ☕ - it takes 2–5 minutes.
 
**4. Create `.env` with your license key**
 
Stay in the project root. Replace `YOUR_LICENSE_KEY` with your actual key:
 
```bash
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```
 
This creates `.env` next to `level1/`. The Check It! grader reads this file and never prints your key.
 
**5. Verify installation**
 
```bash
set -a
source .env
set +a
rasa --version
```
 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#fff9ed;border:1px solid #ffd594;border-left:3px solid #f59e0b;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;">The Check It! grader reads <code>.env</code> from the project root and never prints your key. Make sure the file exists before clicking Check It!.</td></tr></table>

{Check It!|assessment}(code-output-compare-3333363688)
