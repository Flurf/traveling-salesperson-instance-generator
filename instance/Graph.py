from ctypes import sizeof
import numpy as np
import googlemaps
class Graph:
    gmaps = googlemaps.Client(key='AIzaSyCu-ipThu3ZSWXvPT_e0NaS4Bp5dsJnzOQ')
    def __init__(self,depotcoords,coords,*morecoords) -> None:
        self.nodes = [(0,depotcoords)]
        for i in range(coords.shape[0]):
            self.nodes.append([i + 1,coords[i]])
        n = coords.shape[0] + 2;
        self.nodes = [(n,depotcoords)]

        self.coords = np.vstack((depotcoords,coords))
        print(self.coords)
        self.dist_matrix = self.gmaps.distance_matrix(self.coords,self.coords)
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


        

        