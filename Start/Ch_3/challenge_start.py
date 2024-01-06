# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0

# get top 40 significant events
sigevents_top40 = sorted(data["features"], key=getsig, reverse=True)[0:40]


def gettime(q):
    time = q["properties"]["time"]
    if (time is None):
        time = 0
    return time

# sort by date desc
sigevents_dt_sorted = sorted(sigevents_top40, key=gettime, reverse=True)
# Another way, with lambda
sigevents_dt_sorted_v2 = sorted(sigevents_top40, key=lambda e: e["properties"]["time"], reverse=True)

# create header & rows
header = ["Magnitude", "Place", "Felt", "Date", "MapURL"]
rows = []
for quake in sigevents_dt_sorted:
    thedate = datetime.date.fromtimestamp(int(quake["properties"]["time"]/1000))
    lat = quake["geometry"]["coordinates"][1]
    lng = quake["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com?q={lat},{lng}"
    
    rows.append([
        quake["properties"]["mag"],
        quake["properties"]["place"],
        quake["properties"]["felt"],
        thedate,
        gmaplink
    ])

# TODO: write the results to the CSV file
with open("sigevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
