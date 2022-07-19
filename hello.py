import googlemaps
import numpy as np
from datetime import datetime
from calcSavings import calcSavings
from instance.Area import Area  
from instance.Circle import Circle  
from instance.Square import Square  

gmaps = googlemaps.Client(key='AIzaSyCu-ipThu3ZSWXvPT_e0NaS4Bp5dsJnzOQ')
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result)


#b = np.array([[0,0], [0,1], [1,0], [1,1] ])
#print(b[0])
#x = 1
#x = calcSavings(x)
#print(x + 68)

#ferruccio = Area(1,10,1,3)
milano = np.array([45.46849353081034, 9.182678872770355])
resta = Circle(1,3,milano,20000,20000)
print(resta.geocoord)
#ferruccio = Square(1,4,milano,20000,20000)
#reverse_geocode_result = gmaps.reverse_geocode((45.46849353081034, 9.182678872770355))
distance_matrix = gmaps.distance_matrix(resta.geocoord,resta.geocoord)
print(distance_matrix)

