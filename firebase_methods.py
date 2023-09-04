import firebase_admin
from firebase_admin import credentials, firestore
from bot_methods import send_message_to_channel
from decouple import config


# BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
# CHAT_ID = "@YourChannelName"  # or some chat ID
BOT_API = str(config('BOT_API', default=''))
if not BOT_API:
    raise ValueError("BOT_API is not set!")
CHAT_ID = str(config('CHAT_ID', default=''))
if not CHAT_ID:
    raise ValueError("CHAT_ID is not set!")



# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/ubuntu/proj/telegram-stats-monitor/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def setup_firebase():
    """Optional method to setup Firebase, if there are additional setup steps required."""
    pass

def store_action_to_firebase(action_data: dict):
    """Stores the provided action data to Firebase Firestore."""
    
    # Reference to the Firestore collection where data will be stored
    admin_actions_ref = db.collection('admin_actions')
    
    try:
        # Check if an action with the same hash already exists
        matching_actions = admin_actions_ref.where('hash', '==', action_data['hash']).get()

        # If no matching action was found, add the new action_data
        if not matching_actions:
            # Check if the user_id exists in any previous actions
            previous_actions = admin_actions_ref.where('user_id', '==', action_data['user_id']).get()
            
            if previous_actions:
                
                # sort by date
                previous_actions = sorted(previous_actions, key=lambda doc: doc.to_dict()['date'])
                # get latest action
                latest_action = previous_actions[-1].to_dict()
                if action_data['action'] == 'Joined':
                    action_data['total_joined'] = latest_action['total_joined'] + 1
                    action_data['total_left'] = latest_action['total_left']
                elif action_data['action'] == 'Left':
                    action_data['total_joined'] = latest_action['total_joined']
                    action_data['total_left'] = latest_action['total_left'] + 1
            
            admin_actions_ref.add(action_data)
            print(f"Stored action data for user {action_data['user_id']} to Firestore")

            message = "\n".join([f"{key}: {value}" for key, value in action_data.items()])
            send_message_to_channel(BOT_API, CHAT_ID, message)
        else:
            print(f"Action data with hash {action_data['hash']} already exists. Skipping.")
           
    except Exception as e:
        print(f"Error storing data to Firestore: {e}")
