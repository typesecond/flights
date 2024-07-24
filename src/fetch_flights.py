import requests

def get_flights():
    url = 'https://opensky-network.org/api/states/all'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        states = data['states']

        for flight in states:
            print(f"ICAO24: {flight[0]}")
            print(f" Callsign: {flight[1]}")
            print(f" Country: {flight[2]}")
            print(f" Longitude: {flight[5]}")
            print(f" Latitude: {flight[6]}")
            print(f" Altitude: {flight[7]}")
            print(f" Velocity: {flight[9]}")
            print(f" Heading: {flight[10]}")
            print("------------------------")
    else:
        print("Failed to retrieve data:", response.status_code)

get_flights()









