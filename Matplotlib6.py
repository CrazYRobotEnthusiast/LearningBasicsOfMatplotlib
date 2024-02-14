#Some of the numpy being used in matplotlib:-
import numpy as np
bins=np.arange(120,150,0.5) #Used for Histogram intervals
print(bins)
l1=np.random.randint(157,163,size=1000) #Used for histogram data
xValues=[]
scatteredness=0.2
for i in range(40):
    for j in range(40-i):
        xValues.append(i+(i)*np.random.normal(0,scatteredness)) #Used for noise in scatter graphs
xValues.append(100)
#xValues is for input of scattered graph!!