# flyingTravelingSalesman
Code developed in order to create instances for a Traveling Salesman problem.
The user can either choose to generate random geographical coordinates inside a reference area or define them by hand. The code will then calculate the distance matrix and the times matrix using the Google Maps API. The coordinates and the matrixes will then be printed to text ready to be employed in whatever solver or custom code; since the outputs of this code were required to be implemented in AMPL, another file is printed in an AMPL .dat format. The random positions inside the reference area are additionaly plotted as a png image.

## Requirements
- Python 3.10 
- package installer for Python (pip)
- A Google Maps API key (for more details refer to [google-maps-services-python](https://console.cloud.google.com/apis/credentials))

## Installation
The Google Maps client needs to be installed as an external package
    $ pip install -U googlemaps

## Usage

This example uses the Geocoding API and the Directions API with an API key:

```python
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
```