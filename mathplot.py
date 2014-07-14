import random as rand
import matplotlib.pyplot as plt
import os
import csv


x = range(1,10)
# a 3rd number in the range would give number of steps 
y = [(i+rand.random())**2 for i in x]
z = [(i+rand.random()*2)**2 for i in x]
print x
print y

plt.figure()

font = {'family': 'Times New Roman', 'size':20}

plt.rc('font', **font)
plt.plot(x,y,'.', label='y values')
plt.plot(x,z,'x', label='x values')
# 3rd number in range will pick your markers for a plot
plt.title('x**2 with noise')
plt.ylabel('y (height)')
plt.xlabel('x (sec)')
plt.legend(loc='best')
plt.xlim(0,10)
plt.ylim(0,110)
plt.show()

dirName = 'C:\Users\Owner\Documents\Git\gettingstarted'
fileName = 'sampledata.dat'

if not os.path.exists(dirName):
    os.makedirt(dirName)
# makes the folder if it does not exist

dataList = list()
[dataList.append([x[i],y[i],z[i]]) for i in range(len(x))]

print dataList

with open(os.path.join(dirName,fileName), 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['x','y','z'])
    writer.writerows(dataList)
    
# file saved as a .dat file in selected folder as given file name