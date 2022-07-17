import googlemaps
import numpy as np
from datetime import datetime
from calcSavings import calcSavings
from instance.Circle import Circle  
# gmaps = googlemaps.Client(key='AIzaSyCu-ipThu3ZSWXvPT_e0NaS4Bp5dsJnzOQ')
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result)


#b = np.array([[0,0], [0,1], [1,0], [1,1] ])
#print(b[0])
#x = 1
#x = calcSavings(x)
#print(x + 68)

#ferruccio = Area(1,10,1,3)
resta = Circle(1,10,1,3,10)
print(resta.positions)

