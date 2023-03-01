#!/bin/python3 

#!/bin/python3 

import requests
import argparse
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument('-w','--wordlist', type=str, required=True, help="Switch for Wordlist")
parser.add_argument('-u','--url', type=str, required=True, help="Switch for URL")
parser.add_argument('-e','--extension', type=str, required=False, help="Switch for Extension")
args = parser.parse_args()

print("[+] Wordlist: ", args.wordlist)
print("[+] URL: ", args.url)

# Request Headers
headers = {
    'User-Agent':'Macintosh Mac OS X'
}

# Sanitize wordlist input
wordlist_filename = os.path.basename(args.wordlist)
wordlist_dir = os.path.dirname(os.path.abspath(args.wordlist))

# Check if URL schema exists in the url
if ('http' in args.url) or ('https' in args.url):
    pass
else:
    print('Please enter a URL Schema')
    sys.exit()

# Parsing through each word in the wordlist
try:
    with open(os.path.join(wordlist_dir, wordlist_filename), 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n")
            if args.extension:
                line = line + '.' + args.extension.lstrip('.')
            r = requests.get(args.url+'/'+line, headers=headers)
            if(r.status_code != 404):
                print(args.url+'/'+line, ":", r.status_code)
except:
    print("Error Occurred")



# Assignment: You can add an extra argument and ask for an extension to be appended towards the end
