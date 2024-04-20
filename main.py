#reminder: link back to "https://simplemaps.com/data/us-cities"
import csv, json
import requests
import pandas as pd

eia, api = ("https://api.eia.gov/v2/",
                 "?api_key=SdV1Kbye1BXVeF1SA5cJfiet9kBMzzjqsewbxs2W")
ercotId = 0
regions = {
    "California": "CAL",
    "Carolinas" : "CAR",
    "Central" : "CENT",
    "Texas" : "TEX",
    "Florida" : "FLA",
    "Mid-Atlantic" : "MIDA",
    "Midwest" : "MIDW",
    "New England" : "NE",
    "New York" : "NY",
    "Northwest" : "NW",
    "Southeast" : "SE",
    "Tennessee" : "TEN"
}
location = input("Enter location as City, State\n")

def readCSVDetails(location):
    location = location.lower().split(", ")
    with open("uscities.csv", 'r') as citiesCSV:
        cities = csv.reader(citiesCSV)
        for city in cities:
            if city[0].lower() == location[0]:
                if city[3].lower() == location[1]:
                    userCityDetails = city
    return userCityDetails

def getJson(dataPoints):
    response = requests.get(eia + dataPoints + api)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        raise Exception("Error getting data from api")

def refreshErcotId():
    url = 'https://ercotb2c.b2clogin.com/ercotb2c.onmicrosoft.com/B2C_1_PUBAPI-ROPC-FLOW/oauth2/v2.0/token'
    parameters = {
        "grant_type" : password,
        "username" : "",
        "password" : "",
        "response_type" : "",
        "scope" : "",
        "client_id" : ""
    }
def ercot():
    response = requests.get("https://api.ercot.com/api/public-reports/np3-910-er/2d_agg_out_sched[?SCEDTimestampFrom][&SCEDTimestampTo][&repeatHourFlag][&sumLSLOutputSchedFrom][&sumLSLOutputSchedTo][&sumHSLOutputSchedFrom][&sumHSLOutputSchedTo][&sumOutputSchedFrom][&sumOutputSchedTo][&page][&size][&sort][&dir]")
cityStats = readCSVDetails(location)
