import numpy as np
import matplotlib.pyplot as plt

class Area:
    def __init__(self, seed, ncoords, origin, scale_factor, L):
        self.seed = seed    
        #number of coordinates to be displaced in the area with the given seed
        self.ncoords = ncoords    
        self.origin = origin    #center of the area 
        self.scale_factor = scale_factor      #scale factor
        self.L = L              #characteristic length, L/2 for square, R for circle
        self.positions = self.create_positions(self.ncoords)

    def create_positions(self,n):
        p = np.random.uniform(low=0, high=1, size=2*n) 
        p = p.reshape(2,n)
        return p

    def plot(self,x,y):
        fg, ax = plt.subplots(1, 1)
        ax.plot(x, y, '.') # plot random points
        ax.axis('equal')
        ax.grid(False)

    def scale(self,x,y,scale):
        return x*scale,y*scale

    def translate(self,x,y,origin):
        return x + origin[0], y + origin[1]

    

    