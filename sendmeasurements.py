# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json
import time
import randomdata

# api endpoint
MEASURES_ADD_URL = "https://api.truesight.bmc.com/v1/measurements"
HEADERS = {'Content-Type': 'application/json'}
APP_NAME = "Banking portal"

def sendMeasurements(sourceName, userName, apiToken):
    currentTime = round(time.time())

    sales_dict = getMeasureDict("Bike.Sales", sourceName, currentTime)
    postMeasures(sales_dict, userName, apiToken)

    customers_dict = getMeasureDict("Visiting.Customers", sourceName, currentTime)
    postMeasures(customers_dict, userName, apiToken)

    wait_dict = getMeasureDict("Customer.Wait", sourceName, currentTime)
    postMeasures(wait_dict, userName, apiToken)


def getMeasureDict(metricName, sourceName, timeStamp):
    measurement_dict = {
        "source" : sourceName,
        "metric" : metricName,
        "measure" : randomdata.getMetricValue(metricName),
        "timestamp" : timeStamp,
        "metadata" : {
            "app_id" : APP_NAME
        }
    }
    return measurement_dict

def postMeasures(measureDict, userName, apiToken):
    response = requests.post(MEASURES_ADD_URL,
        auth=(userName, apiToken), data=json.dumps(measureDict), headers=HEADERS)
    if response.status_code == requests.codes.ok:
        print("Successfully sent measurement " + measureDict["metric"] +
            " for source " + measureDict["source"] + " @ time:" +
            str(measureDict["timestamp"]))
    else:
        print("Unable to send measurement " + measureDict["metric"] +
            " for source " + measureDict["source"] + " @ time:" +
            str(measureDict["timestamp"]) + " Error code:" + str(response.status_code))
