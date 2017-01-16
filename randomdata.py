import random

motorcycles = ['ducati', 'yamaha', 'harley', 'honda',
    'suzuki', 'indian', 'bmw', 'aprilia', 'kawasaki', 'piaggio']
sex = ['male', 'female']
age = [ 21, 27, 35, 40, 45, 50, 49, 39, 18, 60]
state = ['CA', 'NV', 'OR', 'WA', 'TX', 'AZ', 'NM', 'UT', 'ID', 'CO']
dealership = ['San Jose Dealership', 'Las Vegas Dealership', 'Houston Dealership']

def getMetricValue(metricName):
    if(metricName == "Bike.Sales"):
        return random.randint(0,5)
    elif (metricName == "Visiting.Customers"):
        return random.randint(5,25)
    elif (metricName == "Customer.Wait"):
        return random.randint(10,30)
    else:
        return 0

def getEventInfo(timeStamp, appName):
    dealer = dealership[random.randint(0,2)]
    model = motorcycles[random.randint(0,9)]
    eventvalues = {
        "fingerprintFields": [
            "@title", "@createdAt"
        ],
        "source": {
            "ref": dealer,
            "type": "APPLICATION"
        },
        "title": "Motorcycle sold at " + dealer + " model:" + model +
            " sale price:" + str(random.randint(10000,20000)),
        "createdAt": timeStamp * 1000,
        "eventClass": "BIKE_SALE",
        "properties" : {
            "app_id": appName,
            "model_sold" : motorcycles[random.randint(0,9)],
            "buyer_age" : age[random.randint(0,9)],
            "buyer_state" : state[random.randint(0,9)],
            "buyer_sex" : sex[random.randint(0,1)]
        }
    }
    return eventvalues
