# Telegram Channel Subscription Monitor

This is a Python-based automation tool utilizing Telethon to emulate and automate Telegram client activities, specifically monitoring channel subscriptions.

## Key Features:

- **Automated Monitoring**: Regularly checks for user subscription and unsubscription events on a Telegram channel.
- **Service-Oriented**: Runs as a continuous service on Linux, fetching admin actions every 5 minutes.
- **Efficient Storage**: Actions are hashed based on the date and user ID. Only unique actions are saved to the Firebase Firestore database, preventing duplicates.
- **Real-time Notifications**: Sends detailed alerts of each action to another Telegram channel or group. These alerts include user ID, nickname, first and last name, action date, and the corresponding hash.
- **Sentry Integration (Optional)**: Monitor application health and track potential issues with Sentry. 

## Requirements

### System:
- **OS**: Linux-based machine.
- **Permissions**: User with `sudo` access.
- **Runtime**: Python 3.x installed.

### Firebase Firestore:
1. **Database Setup**: 
    - Create a collection named `admin_actions`.
    - Insert an empty document with a random name within this collection.
2. **Private Key Configuration**: 
    - Download your Firebase private key file from the [Firebase console](https://console.firebase.google.com/).
    - Rename the key file to `serviceAccountKey.json`.
    - Place it in the root directory of the project (where `main.py` is located).

### Telegram:
1. **API Credentials**: 
    - Register on [my.telegram.org](https://my.telegram.org/) to obtain `api_id` and `api_hash`.
2. **Channel to Monitor**: 
    - Ensure you have a Telegram channel nickname you want to monitor (e.g., `@channel_name`).
3. **Bot Token**: 
    - Create a Telegram bot via [t.me/BotFather](https://t.me/BotFather) and note down the token.
4. **Notification Receiver ID**: 
    - Decide on a Telegram channel or group to receive notifications.
    - Obtain the chat id for this destination (e.g., `-1001234567890`). 
    - If you're unfamiliar with this process, follow this [guide](https://gist.github.com/mraaroncruz/e76d19f7d61d59419002db54030ebe35) to get the chat ID.
5. **Notification Receiver Invite Link**: 
    - Create an invite link for the notification receiver channel or group.
    - This will be used to check if all events were successfully sent to the notification receiver.
    - Example for private channel: `https://t.me/+IybSNCg_1a2b3c4d5e`
6. **Add bot to notification receiver**: 
    - Add the bot to the notification receiver channel or group.
    - Give the bot admin privileges to allow it to send messages.

### Sentry (Optional):
- **DSN**: Obtain a DSN (Data Source Name) from your Sentry account. This will be used to send error logs and tracking info to Sentry for monitoring the application's health.


## Installation

### 1. Create a new directory for the project using the terminal
```bash
mkdir telegram-stats-monitor
```

### 2. Navigate to the project directory
```bash
cd telegram-stats-monitor
```

### 3. Clone the repository to machine that will run the service
```bash
git clone git@github.com:preckrasno/telegram-channel-subs-monitor.git .
```

### 4. Set Up a virtual environment
```bash
python3 -m venv venv
```

### 5. Activate virtual environment
mac/linux
```bash
source venv/bin/activate
```

### 6. Install required packages from requirements.txt
```bash
pip install -r requirements.txt
```

### 7. Create Configuration
Create .env file in the root directory and add variables using .env.example file as a template

### 8. Firebase Firestore Setup
Ensure the Firebase private key file `serviceAccountKey.json` is in the root directory from [step 2](#firebase-firestore) on Firebase Firestore setup. Execute the following command and find the file in the root directory
```bash
ls
```

### 9. Initial Run to Setup Telegram Session
Run the script manually for the first time to login into telegram and create session file
```bash
python3 main.py
```

### 10. Deactivate the Virtual Environment
After logging in, stop the script `(ctrl+c)` and deactivate the virtual environment
```bash
deactivate
```

### 11. Set up systemd service
- Edit `telegram-stats-monitor.service` file and change `ExecStart` and `WorkingDirectory` to the correct path
- Move the service file to the systemd directory:
 (`telegram-stats-monitor.service` to `/etc/systemd/system/`)
```bash
sudo cp telegram-stats-monitor.service /etc/systemd/system/
```
- Reload the systemd daemon to recognize your service:
```bash
sudo systemctl daemon-reload
```
- Enable the service to start on boot:
```bash
sudo systemctl enable telegram-stats-monitor.service
```
- Start the service:
```bash
sudo systemctl start telegram-stats-monitor.service
```
- Check the status of the service (optional):
```bash
sudo systemctl status telegram-stats-monitor.service
```
- To view logs, use the following command. Add the `-e` flag for real-time logs (optional):
```bash
sudo journalctl -u telegram-stats-monitor.service
```
or 
```bash
sudo journalctl -u telegram-stats-monitor.service -e
```
- Stopping and restarting the service (optional)
```bash
sudo systemctl stop telegram-stats-monitor.service
sudo systemctl restart telegram-stats-monitor.service
```
- To disable the service from starting on boot (optional):
```bash
sudo systemctl disable telegram-stats-monitor.service
```