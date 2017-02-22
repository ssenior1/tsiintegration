# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json
import time
import randomdata

import random

# api endpoint
EVENT_SEND_URL = "https://api.truesight.bmc.com/v1/events"
HEADERS = {'Content-Type': 'application/json'}
APP_NAME = "Banking portal"


def postEvent(applicationName, userName, apiToken, createError):

    while True:
        errorType = 0
        eventDict = randomdata.getEventInfo(applicationName, errorType)
        print("Successfully sent event " + eventDict["title"])

        if createError:
            errorType = random.randint(1,3)
            # make bigger for demo
            numberOfSameErrors = random.randint(3, 5)
            for i in range(numberOfSameErrors):
                eventDict = randomdata.getEventInfo(applicationName, errorType)
                print("Successfully sent event " + eventDict["title"])


    # Whilst not connected to the internet - remove comment tags when back online

    # print("Successfully sent event " + eventDict["title"] + " for source " + eventDict["source"]["ref"] + " @ time:" +
    #     str(eventDict["createdAt"]))

    # response = requests.post(EVENT_SEND_URL,
    #     auth=(userName, apiToken), data=json.dumps(eventDict), headers=HEADERS)
    # if response.status_code == requests.codes.ok or response.status_code == requests.codes.accepted:
    #     print("Successfully sent event " + eventDict["title"] +
    #         " for source " + eventDict["source"]["ref"] + " @ time:" +
    #         str(eventDict["createdAt"]))
    # else:
    #     print("Unable to send event " + eventDict["title"] +
    #         " for source " + eventDict["source"]["ref"] + " @ time:" +
    #         str(eventDict["createdAt"]) + " Error code:" + str(response.status_code))
