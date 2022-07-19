import numpy as np
from .Area import Area
import matplotlib.pyplot as plt

class Square(Area):
    def __init__(self, seed, ncoords, origin, scale_factor, L):
        super().__init__(seed, ncoords, origin, scale_factor, L)
        x,y = self.positions[0,:], self.positions[1,:]
        x,y = self.scale(x,y,2*scale_factor)
        squarecenter = np.array([-L,-L])
        x,y = self.translate(x,y,squarecenter)
        self.positions[0,:], self.positions[1,:] = x,y

        self.geocoord = self.latlongfromdistance(self.positions[0,:],
                                                self.positions[1,:], 
                                                origin[0],origin[1])

        #self.plot(self.positions[0,:],self.positions[1,:], 2*L)


    def plot(self, x, y, L):
        super().plot(x, y)
        rectangle = plt.Rectangle((-L/2,-L/2), L, L, fc="none",ec="black", linewidth=3)
        plt.gca().add_patch(rectangle)
        plt.show()