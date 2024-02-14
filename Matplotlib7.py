#Plotting multiple graphs on single bar chart
import csv
import matplotlib.pyplot as plt
import numpy as np
with open('Data.csv') as csvfile:
    f=csv.reader(csvfile)
    print(f)
    data=[] 
    for r in f:
        data.append(r)
data.pop(0)
states=[]
for i in data:
    states.append(i[0])
areaSlope=[]
for i in data:
    areaSlope.append(float(i[4]))
road=[]
for i in data:
    road.append(float(i[5]))
x=list(range(1,13))
x2=[]
for i in x:
    x2.append(i+0.2)
plt.bar(x2,road,label='Road density',width=0.4)
x1=[]
for i in x:
    x1.append(i-0.2)
plt.yticks(np.arange(0,80,5))
plt.bar(x1,areaSlope,label='Percentage area with slope>30%',width=0.4)
plt.xlabel('States')
plt.legend()
plt.xticks(x,states)
plt.title('Problem 1 part b')

plt.show()