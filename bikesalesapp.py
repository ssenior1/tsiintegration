import sendmeasurements as sm
import sendevents as se
import definemetrics as dm
import time
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
# if the do not exis
dm.defineAllMetrics(userName, apiToken)

# Loop based on the polling Frequency
while True:
    # Measurement data for the 3 locations
    sm.sendMeasurements("San Jose Dealership", userName, apiToken)
    sm.sendMeasurements("Houston Dealership", userName, apiToken)
    sm.sendMeasurements("Las Vegas Dealership", userName, apiToken)

    # Event data to indicate sales
    se.sendEvent(userName, apiToken)

    time.sleep(pollingFrequency)
