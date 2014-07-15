import os
import csv
import numpy as np
import matplotlib.pyplot as plt

# Helper functions below
def ourFit(x,y,deg,xi=None):
    if xi == None:
# double equal sign is used for conditions like "if" so that we don't accidentally set a new value with a single sign
        xi = x
    FitCoeff = np.polyfit(x, y, deg)
    FitPoly = np.poly1d(FitCoeff)
    return FitPoly(xi)
    

dirName = 'C:\Users\Owner\Documents\Git\gettingstarted'
fileName = 'sampledata.dat'
#reading the data in from our file
with open(os.path.join(dirName,fileName), 'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',')
    data = list()
    for row in dataReader:
        data.append(row)
   
data.pop(0)
# an open colon at end of 0 would mean mean take data from 0, until very end
     
print data

x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]
#casting from string to integer/float
print x

q = [y[i]*z[i] for i in range(len(y))]
print q

deg = 2
#means second order function

yFitValues = ourFit(x,y,deg)
xRandom = [4.5,6.5,8.5]
yFitRandom = ourFit(x,y,deg,xRandom)

zFitValues = ourFit(x,z,deg)

#yFitCoeff = np.polyfit(x, y, deg)
#yFitPoly = np.poly1d(yFitCoeff)
#yFitValues = yFitPoly(x)

#print yFitCoeff
#print yFitPoly
#print yFitValues
#print yFitPoly(1)

#zFitCoeff = np.polyfit(x, z, deg)
#zFitPoly = np.poly1d(zFitCoeff)
#zFitValues = zFitPoly(x)


plt.figure()
plt.plot(x,y,'o')
plt.plot(x,yFitValues)
plt.plot(xRandom,yFitRandom,'.')
plt.plot(x,z,'x')
plt.plot(x,zFitValues)
plt.xlim(0,10)
plt.show()
