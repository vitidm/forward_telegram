#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")

FROM = [str(i) for i in FROM_.split()]
TO = [str(i) for i in TO_.split()]

try:

    BotzHubUser = TelegramClient('anon', APP_ID, API_HASH)
    BotzHubUser.start()
    print("Connected succesfully")

except Exception as ap:

    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(chats=FROM))

async def sender_bH(event):

    for i in TO:

        title_fromchat = event.chat.title
        
        try:

            await BotzHubUser.send_message(
                i,
                title_fromchat + ":\n" + event.message.message
            )
            
        except Exception as e:

            print(e)

print("Bot has started.")

BotzHubUser.run_until_disconnected()
