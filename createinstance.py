from turtle import end_fill
import googlemaps
import numpy as np
from datetime import datetime
from calcSavings import calcSavings
from instance.Area import Area  
from instance.Circle import Circle  
from instance.Square import Square  
from instance.writetodat import writetodat
from instance.Graph import Graph


nlocations = 9
milano = np.array([45.46849353081034, 9.182678872770355])
resta = Circle('instance1',nlocations,milano,10,10)

graph = Graph(milano,resta.geocoord)

writetodat('tsp2.dat',[(graph.times,'times'),(graph.distances,'distances')])






