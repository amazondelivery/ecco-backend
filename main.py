#reminder: link back to "https://simplemaps.com/data/us-cities"
import csv
import eiapy


def readCSVDetails(location):
    location = location.lower().split(", ")
    with open("uscities.csv", 'r') as citiesCSV:
        cities = csv.reader(citiesCSV)
        for city in cities:
            if city[0].lower() == location[0]:
                if city[3].lower() == location[1]:
                    userCityDetails = city
    return userCityDetails

location = input("Enter location as City, State")
cityStats = readCSVDetails(location)
print(cityStats)
cityName = cityStats[0]
state = cityStats[3]
county = cityStats[5]

print(cityName, state, county)
