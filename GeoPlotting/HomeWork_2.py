
# coding: utf-8
# Author: Mridula Maddukuri

from mpl_toolkits.basemap import Basemap
import matplotlib
import matplotlib.pyplot as plt
import pylab
import numpy as np
import pandas
import geoplotter
get_ipython().magic(u'matplotlib inline')


# Use geoplotter to create a basic plot of the world. 
# This should come up just by calling the right functions of geoplotter
# ,and you shouldn’t need to do much extra work.


WorldMap = geoplotter.GeoPlotter()
# default arguments



#print WorldMap.getAxes()

WorldMap.drawWorld()

plt.savefig('World.pdf')

plt.show()


# Write some python code to: 
#     1) read in NMC_v4_0.csv into a Pandas data set 
#     2) Given a year, and a COW Country Code, be able to pull out the CINC of the country 
#     3) Get all the unique COW Country Codes.



NMC = pandas.read_csv('NMC_v4_0.csv')


def extractCINC(Year = 1816,CountryCode = 2):
    return NMC[(NMC['year'] == Year) & (NMC['ccode'] == CountryCode)]['cinc']

NMC.ccode.unique()


# Download the world borders shape file cshapes_0.4-2.zip from: http://downloads.weidmann.ws/cshapes/Shapefiles/.
# After unzipping, use the readShapefile method on geoplotter to read in the shape file. Look through the _info variable to see what pieces of data are associated with each shape. Specifically, the COWCODE data for a shape tells you what country that shape belongs to. Use drawShapes to draw the United States in a different color be sure to 1) write a loop to collect all the shapes associated with the US 2) draw all of those shapes in the color you chose.


#readShapefile
WorldMap.readShapefile('~/Computational Optimization/cshapes_0.4-2/cshapes','shapeinfo')
# 1
# USA = [d for d in WorldMap.m.shapeinfo_info if d['COWCODE'] in [2]]
USA_shape = []
USA_index = []

for i in range(len(WorldMap.m.shapeinfo_info)):
    if WorldMap.m.shapeinfo_info[i]['COWCODE'] in [2]:
        USA_shape = USA_shape + WorldMap.m.shapeinfo[i]
        USA_index = USA_index + [i]



WorldMap.drawWorld()
WorldMap.drawShapes('shapeinfo',USA_index,facecolor = (0.82400814813704837, 0.0, 0.0, 1.0))

# matplotlib.cm.hot(0.3) gives 



class MilexPlotter(geoplotter.GeoPlotter):
    def readData(self):
        self.NMC = pandas.read_csv('NMC_v4_0.csv')
        self.readShapefile('/Users/mridulamaddukuri/Dropbox/python/Computational Optimization/cshapes_0.4-2/cshapes','shapeinfo')
    def drawWorld(self):
        """Draws oceans, continents, coastlines, countries, and states."""
        self.drawMapBoundary()
        self.fillContinents(color = 'blue')
        self.drawCoastLines(linewidth=0.7)
        self.drawCountries(linewidth=1.2)
        self.drawStates(linewidth=0.7)
    def plotCountry(self,code,**kwargs):
        self.country_shape = []
        self.country_idx = []
        for i in range(len(self.m.shapeinfo_info)):
            if self.m.shapeinfo_info[i]['COWCODE'] in [code]:
                self.country_shape = self.country_shape + self.m.shapeinfo[i]
                self.country_idx = self.country_idx + [i]
        #self.drawWorld()
        self.drawShapes('shapeinfo',self.country_idx,**kwargs)
    def setNormalize(self):
        self.normalized = matplotlib.colors.Normalize(vmin =0, vmax = self.NMC.cinc.max())
    def plotYear(self,year):
        self.clear()
        self.drawWorld()
        self.setNormalize()
        # min here is -9 not 0 
        # problem is here colors are not changing and only one country changes color to yellow at a time
        for i in self.NMC[self.NMC.year == year].ccode:
            self.cinc = self.NMC[(self.NMC['year'] == year) & (self.NMC['ccode'] == i)]['cinc']
            self.plotCountry(i,facecolor = matplotlib.cm.hot(self.normalized(self.cinc))) # enter color as a keyword argument
          
        
 
    
if __name__ == '__main__':
    
    trial = MilexPlotter()
    trial.readData()
    trial.drawWorld()
    trial.setNormalize()
    trial.plotCountry(20,facecolor = (1.0, 0.41078460453384119, 0.0, 1.0)) 

    trial.plotCountry(2,facecolor = 'white')
    #plt.text(-150, 0, 'text', color = 'black')
    trial.figureText(-160,-10,"HELLO",color = 'black',family = 'serif',size = 'large')
    #trial.Normalize()
    #trial.normalized(0.4)
    #for i in NMC.year:
    #    trail.plotYear(i)

    #matplotlib.cm.hot(trial.normalized(0.1))

    for Y in trial.NMC.year.unique():
        trial.plotYear(Y)
        trial.figureText(-160,-10,str(Y),color = 'black',family = 'serif',size = 'large')
        plt.savefig(str(Y)+ ".png")

    normalized = matplotlib.colors.Normalize(vmin =0, vmax = trial.NMC.cinc.max())
    normalized(trial.NMC.cinc)
    matplotlib.cm.hot(normalized(trial.NMC.cinc))
    normalized(0.4)
    # video starts from 1916 ?????
    # add year to the plot 
    trial.NMC.cinc.max()
    trial.NMC.cinc.min()
    #trial.readData()
    #trial.NMC
    #trial.m.shapeinfo
    # the minimum is -9 not 0





