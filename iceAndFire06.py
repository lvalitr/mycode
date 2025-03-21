#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR )
        ## Decode the response
        got_dj = gotresp.json()
        for got_char in got_dj:
            if got_char['name']:
                print (f"{got_char['name']}")

          
if __name__ == "__main__":
        main()

