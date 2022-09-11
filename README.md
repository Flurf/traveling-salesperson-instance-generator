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

This example generates random locations in the Milan city area, the depot location is set to Bovisa's campus:

```python
from turtle import end_fill
import numpy as np
from datetime import datetime
from instance.Area import Area  
from instance.Circle import Circle  
from instance.Square import Square  
from instance.writetodat import *
from instance.Graph import Graph
from datetime import datetime

# name of the .txt, .dat and .png outputs
name = 'test'

#key of gmaps API
key = 'insert_key_here'

#optional: future date and time  of departure
firstdayoflessons = datetime(2022,8,8,8)

# 9 customer + 1 deposit is the limit for the gmaps distance matrix query,
#however this constraint can be overcomed by inquiring gmaps multiple times,
#to do this the Graph class has to be modified
nlocations = 9
milano = np.array([45.46849353081034, 9.182678872770355])
bovisacampus = np.array([45.501913216243466, 9.155222881632804])

area = Square(name,nlocations,milano,7,7)
# in alternative to random generation, coordinates can be passed to the Graph class 
#coords = np.array(  [
#                    [45.413149379990955,	9.13102880553654],	
#                    [45.52193684380405,	    9.25895923951282],	
#                    [45.48130281094056,	    9.264593427685938],	
#                    [45.46015219293106,	    9.250173237436732],	
#                    [45.514980154058655,	9.122147903431854],	
#                    [45.42412063949612,	    9.205127171173423],	
#                    [45.41191649326344,	    9.232036984811892],	
#                    [45.484108039820775,	9.208482454165662],	
#                    [45.519310780983155,	9.237730721196524]])

graph = Graph(key,'none',bovisacampus,area.geocoord)

data = [(graph.times,'times'),(graph.distances,'distances')]


data.append((graph.coords,'coordinates'))

writetodat(name,data)
writetotxt(name,data)

print(graph.coords[0])
print(graph.coords[1].ndim)
```