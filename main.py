import os
import requests
webhook = input('webhook url >:')
wise = '"Invalid Webhook Token"'
oak = webhook
try:
 tree = requests.get(oak)
 if wise in tree.text:
   os.system('cls')
   print('invaild webhook fr')
 else:
   os.system('cls')
   print('vaild webhook fr')
except:
 os.system('cls')
 print('invaild webhook')
os. system("pause")
