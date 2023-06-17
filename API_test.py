import requests
import json

def call_stops(key: str, search: str, max_results: int = 10, format: str = 'json', type: str = 'S'):
    """
    ### Required ###
    key
    SearchString: search string. (max 20)
    
    ### Optional ###
    format: data format (def json)
    max_results: quantaty of results (def 10)
    type: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv (def S)
        S: sök efter endast stationer
        P: Sök efter endast POI
        A: Sök endast efter adresser
        SP: Sök efter stationer och POI
        SA: Sök endas efter stationer och Adresser
        AP: Sök endast på adresser och POI
        ALL: adresser, stationer och POI
    """
    stops_url = f"https://api.sl.se/api2/typeahead.{format}?key={key}&searchstring={search}&maxresults={max_results}&type={type}"
        
    # Send an HTTP request to the API url and get the response object
    response = requests.get(stops_url)
    # Parse the JSON data from the response text into a dictionary object
    data: dict = json.loads(response.text)
    return data
    

def call_realtinfo(key: str, site_id: str, time_window: str, bus: bool = True, 
                   metro: bool = True, train: bool = True, tram: bool = True, 
                   ship: bool = True,format: str = 'json') -> dict:
    """real-time departure information for a given site ID and time window using the SL API
    
    ### Required ###
    key
    site_id: identification number for station
    time_window:  departures within a desired time window (max 60)
    
    ### Optional ###
    format: data format (def json)
    transport methods: bus, metro, train, tram, ship (def True)
    """
    transportation_methods = {'bus' : bus, 
                              'metro' : metro,
                              'train' : train,
                              'tram' : tram,
                              'ship' : ship}

    departures_url = f'https://api.sl.se/api2/realtimedeparturesV4.{format}?key={key}&siteid={site_id}&timewindow={time_window}'
        
    # Loop through transportation methods to disble
    for key in transportation_methods:
        if transportation_methods[key] == False:
            departures_url += f'&{key}=false'
    
    # Send an HTTP request to the API url and get the response object
    response = requests.get(departures_url)
    # Parse the JSON data from the response text into a dictionary object
    data = json.loads(response.text)
    return data

def select_stop(response_data):
    for i, stop in enumerate(response_data):
        if i == 5:
            break
        
        print(stop['Name'])
        
    while True:
        iuser_input = input("Select the number of the stop from where you are traveling: ")
        
        if iuser_input.isnumeric == False:
            print("input must be an integer")
            continue
        
        try:
            selected_stop = response_data[int(iuser_input)-1]
        except KeyError:
            print("stop does not exist")
        else:
            print(f"selected stop: {selected_stop['Name']}")
            return selected_stop
