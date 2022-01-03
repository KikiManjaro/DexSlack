from pydexcom import Dexcom
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
slack_token = 'YOU_SLACK_TOKEN'

def changeStatus():
    dexcom = Dexcom(username, password, True) # add ous=True if outside of US
    bg = dexcom.get_latest_glucose_reading()
    if(bg != None):
        print(bg.value , bg.trend_arrow)
        status_txt = 'Glycemie' + ' a ' + str(bg.time.hour) +'h'+str(bg.time.minute) +'m' + ': ' + str(bg.value) + str(bg.trend_arrow)
        client = WebClient(token=slack_token)
        client.api_call(
            api_method="users.profile.set",
            json={
                "profile": {
                "status_text": status_txt,
                "status_emoji": getIcon(bg.value)
                }
            }
        )

def getIcon(gly):
    if (gly <= 60):
        return ':skull:'
    elif (gly <= 72):
        return ':worried:'
    elif (gly <= 130):
        return ':smile:'
    elif (gly >= 200):
        return ':hot_face:'
    else :
        return ':slightly_smiling_face:'
        
changeStatus()