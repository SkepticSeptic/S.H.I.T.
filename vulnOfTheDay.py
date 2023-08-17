import requests
import argparse
import json
from APIKeys import vuldbAPIKey

def VulnerabilityOfTheDay():
    # Define arguments for API script
    parser = argparse.ArgumentParser()
    parser.add_argument('--recent', dest='recent', default=1, type=int, help='Show the most recent entries with the request method recent. Default: 1')
    parser.add_argument('--details', dest='details', default=0, type=int, help='Specify whether results are basic (0) or detailed (1). Default: 0')
    parser.add_argument('--id', dest='id', help='Request details for a vulnerability entry with a VulDB ID')
    args = parser.parse_args()

    # Add your personal API key here
    personalApiKey = vuldbAPIKey()

    # Set HTTP Header
    userAgent = 'VulDB API Advanced Python Demo Agent'
    headers = {'User-Agent': userAgent, 'X-VulDB-ApiKey': personalApiKey}

    # VulDB endpoint URL
    url = 'https://vuldb.com/?api'

    # Get API usage counter
    usage_counter_response = requests.get(f"{url}&counter", headers=headers)
    if usage_counter_response.status_code == 200:
        usage_counter = usage_counter_response.json().get("counter")
        if usage_counter and usage_counter.get("remaining_credits") > 40:
            # Choose the API call based on the passed arguments
            # Default call is the last 1 recent entry
            if args.recent is not None:
                postData = {'recent': int(args.recent)}
            elif args.id is not None:
                postData = {'id': int(args.id)}
            else:
                postData = {'recent': 1}

            if args.details is not None:
                postData['details'] = int(args.details)

            # Get API response
            response = requests.post(url, headers=headers, data=postData)

            # Display result if everything went OK
            if response.status_code == 200:
                # Parse HTTP body as JSON
                responseJson = json.loads(response.content)

                # Output
                for entry in responseJson['result']:
                    print(f"Vulnerability Of The Day:")
                    print(f"ID: {entry['entry']['id']}")
                    print(f"Title: {entry['entry']['title']}")
                    if args.details:
                        print(f"Details: {entry['entry']['details']}")
                    else:
                        print("Details unavailable.")
                    print("--------------------------")
            else:
                print("Error: Couldn't display vulnerability of the day.")
        else:
            print("Insufficient API credits for vulnerability of the day.")
    else:
        print("Error: Couldn't retrieve API usage counter.")

# Call the function
VulnerabilityOfTheDay()
