from turtle import end_fill
import googlemaps
import numpy as np
from datetime import datetime
from calcSavings import calcSavings
from instance.Area import Area  
from instance.Circle import Circle  
from instance.Square import Square  
from instance.writetodat import writetodat


#returns a matrix from a googlemaps distance_matrix dictionary 
def getmatrix(dict,key,n):
    m = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            m[i,j] = dict["rows"][i]["elements"][j][key]["value"]

    return m


gmaps = googlemaps.Client(key='AIzaSyCu-ipThu3ZSWXvPT_e0NaS4Bp5dsJnzOQ')


nlocations = 10
milano = np.array([45.46849353081034, 9.182678872770355])
resta = Circle('instance1',nlocations,milano,10,10)

dist_matrix = gmaps.distance_matrix(resta.geocoord,resta.geocoord)
times,distances =   [getmatrix(dist_matrix,"duration",nlocations),
                    getmatrix(dist_matrix,"distance",nlocations)]
#print(dist_matrix)
#print(times)
#print(distances)

#trial = np.array([0.1, 0.3, 0.18, 0.24, 0.11])
#trial2 = 10 * trial
#trial3 = 3.4 * np.zeros((4,4))
#trial4 = np.array(5)
writetodat('tsp.dat',[(times,'times'),(distances,'distances')])






