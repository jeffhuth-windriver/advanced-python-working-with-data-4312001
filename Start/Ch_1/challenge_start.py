# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?
print(f'total quakes: {len(data["features"])}')

# 2: How many quakes were felt by at least 100 people?
def filterFelt(dataitem):
    felt = dataitem["properties"]["felt"]
    if (felt is None):
        felt = 0
    return (felt >= 100)

felt = list(filter(filterFelt, data["features"]))
print(f"Total quakes felt by atleast 100 (using filter): {len(felt)}")

felt2 = sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
          for quake in data["features"])
print(f"Total quakes felt by atleast 100 (using sum): {len(felt)}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getFelt(dataitem):
    felt = dataitem["properties"]["felt"]
    if (felt is None):
        felt = 0
    return (felt)

most_felt = max(data["features"], key=getFelt)["properties"]
print(f'Most felt reports: M {most_felt["mag"]} - {most_felt["place"]}, reports: {most_felt["felt"]}')

# 4: Print the top 10 most significant events, with the significance value of each
def getSig(dataitem):
    sig = dataitem["properties"]["sig"]
    if (sig is None):
        sig = 0
    return (sig)

print('The 10 most significant events were:')
most_sig = sorted(data["features"], key=getSig, reverse=True)
for i in range(0,10):
    print(f'Event: M {round(most_sig[i]["properties"]["mag"],1):.1f} - {most_sig[i]["properties"]["place"]}, Significance: most_sig[i]["properties"]["sig"]')
