# python 3 sample to create metric definitions
# importing the requests library, run "pip3 install requests" to install
import requests
import json

# api endpoint
METRICS_CREATE_URL = "https://api.truesight.bmc.com/v1/metrics"
HEADERS = {'Content-Type': 'application/json'}

bike_sales_metric = {
    "name" : "Bike.Sales",
    "type" : "Bike_Business_Metrics",
    "description" : "Number of bikes sold during the interval",
    "displayName" : "Bike Sales",
    "displayNameShort" : "Bike Sales",
    "unit" : "number",
    "defaultAggregate" : "avg"
    }

visiting_customer_metric = {
    "name" : "Visiting.Customers",
    "type" : "Bike_Business_Metrics",
    "description" : "Number of customers visting during the interval",
    "displayName" : "Visiting Customers",
    "displayNameShort" : "Visit Customer",
    "unit" : "number",
    "defaultAggregate" : "avg"
    }

customer_wait_metric = {
    "name" : "Customer.Wait",
    "type" : "Bike_Business_Metrics",
    "description" : "Avg wait time in minutes for customers",
    "displayName" : "Wait Time",
    "displayNameShort" : "Wait Time",
    "unit" : "duration",
    "defaultAggregate" : "avg"
    }

''' Create a metric based on the dictionary passed '''
def createMetric(metricInfo, userName, apiToken):
    response = requests.post(METRICS_CREATE_URL,
        auth=(userName, apiToken), data=json.dumps(metricInfo), headers=HEADERS)
    if response.status_code == requests.codes.ok:
        print("Successfully created metric " + metricInfo["displayName"])
    else:
        print("Metric " + metricInfo["displayName"] +
            " not created, perhaps it already exists? " +
            "Error code:" + str(response.status_code))

def defineAllMetrics(userName, apiToken):
    # Create the required metrics, these can be batched in a single call
    # but using individual calls in this example
    createMetric(bike_sales_metric, userName, apiToken)
    createMetric(visiting_customer_metric, userName, apiToken)
    createMetric(customer_wait_metric, userName, apiToken)
