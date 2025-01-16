import os
from smsapi.client import SmsApiPlClient
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

token = '<your auth token>'
client = SmsApiPlClient(access_token=token)


if Path('leftRightState.txt').is_file():
    leftRightStateFile = open('leftRightState.txt')
else:
    leftRightStateFile = open('leftRightState.txt', 'w')
    
    # We set left as default, and reopen it in read mode:
    leftRightStateFile.write('Left')
    leftRightStateFile.close()
    leftRightStateFile = open('leftRightState.txt') 


leftRightState = leftRightStateFile.read()
leftRightStateFile.close()

if leftRightState == 'Left':
    client.sms.send(to='<your phone number>', message='Left side jab')
  
    # After making a jab into left side, switch it to the right:
    leftRightStateFile = open('leftRightState.txt', 'w')
    leftRightStateFile.write('Right')
elif leftRightState == 'Right':
    client.sms.send(to='<your phone number>', message='Right side jab')
  
    # After making a jab into left side, switch it to the left:
    leftRightStateFile = open('leftRightState.txt', 'w')
    leftRightStateFile.write('Left')

leftRightStateFile.close() 
