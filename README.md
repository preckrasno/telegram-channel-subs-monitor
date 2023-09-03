project to monitor statistic of the telegram channel using telethon library

## Installation
### create virtual environment
```bash
python3 -m venv venv
```

### activate virtual environment
mac/linux
```bash
source venv/bin/activate
```
windows
```bash
venv\Scripts\activate.bat
```

if new package is needed, install it using pip
```bash
pip install <package_name>
```

freeze the packages
```bash
pip freeze > requirements.txt
```

### deactivate virtual environment
```bash
deactivate
```

### install packages from requirements.txt
```bash
pip install -r requirements.txt
```

## requirements
- firebase firestore json file renamed to `serviceAccountKey.json` and placed in the root directory
- create .env file in the root directory and add variables using .env.example file as a template

## systemctl service setup
- edit `telegram-stats-monitor.service` file and change `ExecStart` to the correct path
- move `telegram-stats-monitor.service` to `/etc/systemd/system/`
```bash
sudo cp telegram-stats-monitor.service /etc/systemd/system/
```
- reload systemctl daemon
```bash
sudo systemctl daemon-reload
```
- enable the service
```bash
sudo systemctl enable telegram-stats-monitor.service
```
- start the service
```bash
sudo systemctl start telegram-stats-monitor.service
```
- check the status of the service
```bash
sudo systemctl status telegram-stats-monitor.service
```
- to view the logs
```bash
sudo journalctl -u telegram-stats-monitor.service
```
- stopping and restarting the service
```bash
sudo systemctl stop telegram-stats-monitor.service
sudo systemctl restart telegram-stats-monitor.service
```
- disable the service
```bash
sudo systemctl disable telegram-stats-monitor.service
```