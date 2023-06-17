from API_test import *

# API KEYS
stops_key = '61a7ab0881674755a394a6a2ae1b75d6'
realtinfo_key = 'eeefd0b16e0c4288b2e72275f70ef640'

search_input = input("search: ")
stop_data = call_stops(stops_key, search_input)
selected_stop = select_stop(stop_data['ResponseData'])

print("Hur vill du resa? [Metros, Buses, Trains, Trams, Ships]")
methods = list()

while True:
    method_input = input("method (n to finish): ")
    if method_input == "n":
        break
    methods.append(method_input)

stop_id = selected_stop['SiteId']
stop_data = call_realtinfo(realtinfo_key, stop_id, 30)
departures = stop_data['ResponseData']

# print departures


for method in methods:
    for departure in departures[method]:
        print(departure)