"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-25"
-------------------------------------------------------
"""
import requests
headers = {
  'Accept': 'application/json'
}
 
r = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers = headers)
 
print r.json()