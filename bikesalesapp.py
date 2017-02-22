import sendmeasurements as sm
import sendevents as se
import definemetrics as dm
import time
import random
import argparse

# Help for the CLI
parser = argparse.ArgumentParser(description='Sample integration with TrueSight Intelligence')
parser.add_argument('--email', help='Your TrueSight Intelligence account email', required=True)
parser.add_argument('--api', help='Your TrueSight Intelligence API token', required=True)
parser.add_argument('--freq', help='Polling frequency, defaults to 10 secs', default=10)

# get the values passed via CLI
args = parser.parse_args()
userName = args.email
apiToken = args.api
pollingFrequency = args.freq

# Metadata definition for the metrics, this will create the metric definitions
# if they do not exist

# remove comment once connected to API
# dm.defineAllMetrics(userName, apiToken)

# Loop based on the polling Frequency
while True:
    # Measurement data for the 3 locations

    # create metrics to send later once good with events

    # sm.sendMeasurements("San Jose Dealership", userName, apiToken)
    # sm.sendMeasurements("Houston Dealership", userName, apiToken)
    # sm.sendMeasurements("Las Vegas Dealership", userName, apiToken)

    # Event data to indicate login issues

    createConsistentError = False
    sleepTime = random.randint(10, 30)
    se.postEvent(userName, apiToken, createConsistentError)
    time.sleep(sleepTime)

    # random interval needs to increase
    if random.randint(1, 2) is 1:
        createConsistentError = True
        numberOfConsistentErrors = random.randint(50, 150)
        sleepTime = random.randint(3, 10)
        time.sleep(sleepTime)
        se.postEvent(userName, apiToken, createConsistentError)

# Live action - push random errors in an ongoing basis of between 2 per minute and 6 per minute
#               at random intervals, also start sending consistent error messages (still with the random errors at the same speed)