from turtle import end_fill
import googlemaps
import numpy as np
from datetime import datetime
from calcSavings import calcSavings
from instance.Area import Area  
from instance.Circle import Circle  
from instance.Square import Square  
from instance.writetodat import *
from instance.Graph import Graph

name = 'instance3'
nlocations = 9
milano = np.array([45.46849353081034, 9.182678872770355])
bovisacampus = np.array([45.501913216243466, 9.155222881632804])

resta = Circle(name,nlocations,milano,10,10)
graph = Graph(bovisacampus,resta.geocoord)

data = [(graph.times,'times'),(graph.distances,'distances')]
writetodat('tsp3',data)

nlocations = np.array(nlocations)
data.append((graph.coords,'coordinates'))
writetotxt(name,data)

print(graph.coords[0])
print(graph.coords[1].ndim)






