import random
from datetime import datetime


class Customer:
    location = ['San Francisco', 'San Jose', 'Los Angeles', 'Portland', 'Las Vegas', 'Houston', 'Santa Clara',
                'New York']
    priorityCustomerStatus = ['Bronze', 'Silver', 'Gold', 'Platinum']


class UsageDetails:
    webPortalName = ['Bank West', 'BankToGo', 'National Bank', 'Point Bank']
    operatingSystem = ['Windows', 'Linux', 'MacOSX', 'iOS', 'Android', 'Other OS']
    browser = ['Internet Explorer', 'Google Chrome', 'Safari', 'Mozilla Firefox', 'Opera', 'Other browser']


class TicketDetails:
    timeOfIssue = datetime.now()
    timeOfResolution = datetime.now()


# def getMetricValue(metricName):
#     if(metricName == "Bike.Sales"):
#         return random.randint(0,5)
#     elif (metricName == "Visiting.Customers"):
#         return random.randint(5,25)
#     elif (metricName == "Customer.Wait"):
#         return random.randint(10,30)
#     else:
#         return 0


def setCustomerAttributes(errorType):

    customer = Customer()

    if errorType == 1:
        customer.location = Customer.location[1]
    else:
        customer.location =  Customer.location[random.randint(0, len(Customer.location)-1)]
    customer.priorityCustomerStatus = Customer.priorityCustomerStatus[random.randint(0, len(Customer.priorityCustomerStatus)-1)]

    return customer


def setUsageAttributes(errorType):

    usageDetails = UsageDetails()

    if errorType == 2:
        usageDetails.webPortalName = UsageDetails.webPortalName [3]
    else:
        usageDetails.webPortalName = UsageDetails.webPortalName[random.randint(0, len(UsageDetails.webPortalName) - 1)]
    if errorType == 3:
        usageDetails.browser = UsageDetails.browser[4]
    else:
        usageDetails.browser = UsageDetails.browser[random.randint(0, len(UsageDetails.browser) - 1)]

    usageDetails.operatingSystem = UsageDetails.operatingSystem[random.randint(0, len(UsageDetails.operatingSystem)-1)]

    return usageDetails


def getEventInfo(applicationName, errorType):

    customer = setCustomerAttributes(errorType)
    usageDetails = setUsageAttributes(errorType)

    eventvalues = {
         "fingerprintFields": [
            "@title", "@createdAt"
        ],
        "source": {
            # "ref": ,
            "type": "APPLICATION"
        },
        # This line is good
        "title": "Login issue for " + usageDetails.webPortalName + " by customer using " +
                 usageDetails.operatingSystem + " running " + usageDetails.browser + " located in "
            + customer.location,

            #time logic to be added on this line
        # "createdAt": datetime.now() * 1000,
        "createdAt": datetime.now(),

        "eventClass": "LOGIN_ISSUE",
        "properties" : {
            "app_id": applicationName,
            "web_portal_name" : UsageDetails.webPortalName,
            "operating_system" : UsageDetails.operatingSystem,
            "browser" : UsageDetails.browser,
            "customer_location" : Customer.location,
            "customer priority" : Customer.priorityCustomerStatus
        }
    }

    return eventvalues
