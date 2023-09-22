# main.py

import asyncio
from datetime import datetime

from telethon_methods import setup_telethon, get_admin_actions
from firebase_methods import store_action_to_firebase

client = None

async def job():
    global client
    print("Fetching new admin actions...")
    if client is None:
        client = await setup_telethon()
    actions = await get_admin_actions(client)
    for action in actions:
        store_action_to_firebase(action.to_dict())

async def wait_for_five_minutes():
    await asyncio.sleep(300)  # Sleep for 300 seconds (5 minutes)

async def scheduler():
    while True:
        await job()
        await wait_for_five_minutes()

if __name__ == "__main__":
    asyncio.run(scheduler())
