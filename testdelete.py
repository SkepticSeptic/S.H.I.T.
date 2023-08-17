#!/usr/bin/env python
#
# shodan_ips.py
# Search SHODAN and print a list of IPs matching the query
#
# Author: achillean
# Mr. Achillean, you suck royally at comments.

import shodan
import color
from APIKeys import shodanAPIKey

# Configuration
API_KEY = shodanAPIKey()

def shodanSearch():
    while True:
        try:
            # Setup the API
            api = shodan.Shodan(API_KEY)

            # Perform the search
            query = input(color.warning("Search term: "))
            if query == "..":
                break
            result = api.search(query)

            # Loop through the matches and print each IP
            for service in result['matches']:
                print(color.OKBLUE(service['ip_str']))
        except Exception as e:
            raise

shodanSearch()
