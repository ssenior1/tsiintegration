# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json
import time
import randomdata

# api endpoint
EVENT_SEND_URL = "https://api.truesight.bmc.com/v1/events"
HEADERS = {'Content-Type': 'application/json'}
APP_NAME = "Bike Dealership"

def sendEvent(userName, apiToken):
    currentTime = round(time.time())
    postEvent(currentTime, APP_NAME, userName, apiToken)

def postEvent(timeStamp, applicationName, userName, apiToken):
    eventDict = randomdata.getEventInfo(timeStamp, applicationName)

    response = requests.post(EVENT_SEND_URL,
        auth=(userName, apiToken), data=json.dumps(eventDict), headers=HEADERS)
    if response.status_code == requests.codes.ok or response.status_code == requests.codes.accepted:
        print("Successfully sent event " + eventDict["title"] +
            " for source " + eventDict["source"]["ref"] + " @ time:" +
            str(eventDict["createdAt"]))
    else:
        print("Unable to send event " + eventDict["title"] +
            " for source " + eventDict["source"]["ref"] + " @ time:" +
            str(eventDict["createdAt"]) + " Error code:" + str(response.status_code))
