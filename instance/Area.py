import numpy as np
import matplotlib.pyplot as plt

class Area:
    R = 6371.0        #earth radius [km], may vary, very high accuracy not important 
    def __init__(self, name, ncoords, origin, scale_factor, L):
        self.name = name    
        #number of coordinates to be displaced in the area with the given seed
        self.ncoords = ncoords    
        self.origin = origin    #center of the area 
        self.scale_factor = scale_factor      #scale factor
        self.L = L              #characteristic length, L/2 for square, R for circle
        self.positions = self.create_positions(self.ncoords)
        self.geocoord = self.positions.transpose()  #turn positions into geocoordinates in child classes

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

    #distance between 2 points with given latitude and longitude coords
    def archaversine(self,lat0,long0,lat,long):
        d = 2*self.R*np.arcsin(np.sqrt(np.square(np.sin((lat-lat0)/2)) 
            + np.cos(lat0) * np.cos(lat) * np.square((long - long0)/2) ))
        return d    #kilometers

    def latlongfromdistance(self,x,y,lat0,long0):
        scalefactor = 1/np.cos(np.deg2rad(lat0))
        x,y = [x*scalefactor,y*scalefactor]
        y0 = self.R*np.log(np.tan(np.pi/4 + np.deg2rad(lat0)/2))
        long  = long0 + np.rad2deg(x/self.R)  #degrees
        lat   = np.rad2deg(2*np.arctan(np.exp((y0 + y) / self.R)) - np.pi/2)   #degrees
        coords = np.array([lat,long]).transpose()
        return coords


    

    