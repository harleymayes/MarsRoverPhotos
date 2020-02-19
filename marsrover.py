import requests
import json
from pyshorteners import Shortener
import time

short = Shortener('Isgd')

year = int(input("Enter year (YYYY): "))
month = int(input("Enter month (MM): "))
day = int(input("Enter day (DD): "))
date = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)

def englishdate(date):
    year = date[0:4]
    month = date[5:7]
    day = date[-2:]
    englishdate = day + '/' + month + '/' + year
    return(englishdate)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

imagestore = open("images.txt", "a")

parameters = {
    "earth_date": date,
    "api_key": "CbSqjyfnKECX7WWkRUg5ux4hLwUkMbh0svWuxMfr"
    }

response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", params=parameters)
jresponse = response.json()

photos = jresponse["photos"]

for i in photos:
    url = i["img_src"]
    url = short.short(url)

    camera = i["camera"]["full_name"]
    roverid = i["rover"]["id"]
    rovername = i["rover"]["name"]
    landed = i["rover"]["landing_date"]
    landed = englishdate(landed)
    
    output = "The image can be found at {0} it was taken on the {1} camera of the rover id {2} '{3}' which landed on {4}".format(url, camera, roverid, rovername, landed) 
    time.sleep(1)

    print(output)

    imagestore.write(str(output))
    imagestore.write("\n")
imagestore.close()
