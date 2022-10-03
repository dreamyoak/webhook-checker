import os
import time
import requests
webhook = input('webhook url >:')
wise = '"Invalid Webhook Token"'
haha = '"Unknown Webhook"'
oak = webhook
try:
 tree = requests.get(oak)
 if wise in tree.text or haha in tree.text or 'discord.com/api/webhooks' not in webhook:
    os.system('cls')
    print('invaild webhook fr')
    input("Press Enter to continue...")
    exit() 
 else:
    os.system('cls')
    print('vaild webhook fr')
    input("Press Enter to continue...")
    exit() 
except Exception as e:
 os.system('cls')
 print('invaild webhook')
 input("Press Enter to continue...")
 exit() 
