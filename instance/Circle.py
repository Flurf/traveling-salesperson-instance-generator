import numpy as np
from .Area import Area
import matplotlib.pyplot as plt

class Circle(Area):
    def __init__(self, seed, ncoords, origin, scale_factor, L):
        super().__init__(seed, ncoords, origin, scale_factor, L)
        self.positions[1,:] *= 2*np.pi
        x = np.sqrt(self.positions[0,:]) * np.cos(self.positions[1,:])
        y = np.sqrt(self.positions[0,:]) * np.sin(self.positions[1,:])

        x,y = self.scale(x,y,scale_factor)
        x,y = self.translate(x,y,origin)

        self.positions[0,:], self.positions[1,:] = x,y
        self.plot(self.positions[0,:],self.positions[1,:], origin, L)


    def plot(self, x, y, origin, R):
        super().plot(x, y)
        circle = plt.Circle((origin[0],origin[1]), R, fc="none",ec="black", linewidth=3)
        plt.gca().add_patch(circle)
        plt.show()