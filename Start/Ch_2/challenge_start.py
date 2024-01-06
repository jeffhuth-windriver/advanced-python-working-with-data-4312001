# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter
from collections import defaultdict

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# First attempt using Counter
def array_of_key(lst, key1, key2):
    arr = []
    for itm in lst:
        if itm[key1][key2] is None:
            val = 'NONE'
        else:
            val = itm[key1][key2]
        arr.append(val)
    return arr

features = data.get("features", {})
type_arr = array_of_key(features, key1='properties', key2='type')

type_counter = Counter(type_arr)

print('METHOD 1')
for key, val in type_counter.items():
    print(f'{key}: {val}')


# Second attempt using defaultdict
totals = defaultdict(int)

for event in data['features']:
    totals[event['properties']['type']] += 1

print('METHOD 2')
for key, val in totals.items():
    print(f'{key}: {val}')