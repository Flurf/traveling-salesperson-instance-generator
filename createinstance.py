from turtle import end_fill
import googlemaps
import numpy as np
from datetime import datetime
from instance.Area import Area  
from instance.Circle import Circle  
from instance.Square import Square  
from instance.writetodat import *
from instance.Graph import Graph

name = 'instance6'
nlocations = 9
milano = np.array([45.46849353081034, 9.182678872770355])
bovisacampus = np.array([45.501913216243466, 9.155222881632804])

#resta = Square(name,nlocations,milano,10,10)
coords = np.array(  [
                    [45.413149379990955,	9.13102880553654],	
                    [45.52193684380405,	    9.25895923951282],	
                    [45.48130281094056,	    9.264593427685938],	
                    [45.46015219293106,	    9.250173237436732],	
                    [45.514980154058655,	9.122147903431854],	
                    [45.42412063949612,	    9.205127171173423],	
                    [45.41191649326344,	    9.232036984811892],	
                    [45.484108039820775,	9.208482454165662],	
                    [45.519310780983155,	9.237730721196524]])	
graph = Graph(bovisacampus,coords)

data = [(graph.times,'times'),(graph.distances,'distances')]
writetodat(name,data)

data.append((graph.coords,'coordinates'))
writetotxt(name,data)

print(graph.coords[0])
print(graph.coords[1].ndim)






