from ctypes import sizeof
import numpy as np
import googlemaps
from datetime import datetime
class Graph:
    firstdayoflessons = datetime(2022,8,8,8)
    gmaps = googlemaps.Client(key='AIzaSyCu-ipThu3ZSWXvPT_e0NaS4Bp5dsJnzOQ')
    def __init__(self,depotcoords,coords,*morecoords) -> None:
        if morecoords :
            self.coords = np.concatenate((coords, morecoords), axis=0)
        else:
            self.coords = coords
        self.nodes = [(0,depotcoords)]    

        for i in range(self.coords.shape[0]):
            self.nodes.append([i + 1,coords[i]])
        n = self.coords.shape[0] + 2;

        self.nodes = [(n,depotcoords)]

        depotcoords = np.expand_dims(depotcoords, axis=0)
        self.coords = np.concatenate((depotcoords, self.coords), axis=0)
        print(self.coords)
        self.dist_matrix = self.gmaps.distance_matrix(self.coords,self.coords,mode="driving",
                                                        departure_time = self.firstdayoflessons)
        self.times,self.distances =   [self.getmatrix(self.dist_matrix,"duration",n-1),
                                        self.getmatrix(self.dist_matrix,"distance",n-1)]
        print(self.dist_matrix)


    #returns a matrix from a googlemaps distance_matrix dictionary 
    def getmatrix(self,dict,key,n):
        m = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                m[i,j] = dict["rows"][i]["elements"][j][key]["value"]

        return m


        

        