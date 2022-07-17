import numpy as np

class Area:
    def __init__(self, seed, ncoords, origin, scale):
        self.seed = seed    
        #number of coordinates to be displaced in the area with the given seed
        self.ncoords = ncoords    
        self.origin = origin    #center of the area 
        self.scale = scale      #scale factor
        #total number of positions is ncoords^2
        self.positions = self.create_positions(self.ncoords)

    def create_positions(self,n):
        p = np.random.uniform(low=0, high=1, size=2*n) 
        p = p.reshape(2,n)
        return p

    

    