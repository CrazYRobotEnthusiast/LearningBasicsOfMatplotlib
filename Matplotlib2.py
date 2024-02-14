import matplotlib.pyplot as plt
import numpy as np
import math
#Resizing our graph:-
plt.figure(figsize=(5,3),dpi=300) #This will print a 5in*3in graph with 300 pixels per inchsq
x=np.arange(0,4.5,0.1) #Defines an array x such that we get following prt values:-
print(x)
print(list(x))
plt.plot(x, x**2,color='r') #x**2 worked here because x is a numpy array and not a list.
#From above code, we will get the points: (0,0) (0.1,0.01) (0.2, 0.04)....etc then we will join these using line segments
plt.show()
plt.plot(x[:20],x[:20]**2,color='r')
plt.plot(x[19:],x[19:]**2,color='r',linestyle='--')
plt.savefig('mygraph.png',dpi=400) #To save an image of our graph
plt.show()
#Above method can also be used to plot the graph of sin(x)

#Rohit Saluja Sir's method to plot sin(x) graph:-

xList=list(range(-500,500))
yList=[]
for i in range(len(xList)):
    xList[i]=xList[i]*math.pi/50
    yList.append(math.sin(xList[i]))
print(min(xList),max(xList))
plt.plot(xList,yList)
plt.xlabel('x (radians)', fontdict={'fontsize':24})
plt.ylabel('sin(x)',fontsize=24)
plt.title('Sin Wave',fontsize=36)
plt.grid(True) #Turning on grid
plt.show()

#Sin and cos graph on same page wit more designs
import numpy as np
x = np.arange(-5, 5, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(1, 2, 1)  
plt.plot(x, y1, color='green', label='sin(x)')
plt.grid()
plt.title('SINE function Wave')
plt.xlabel('Angle',fontdict={'fontsize':10})
plt.ylabel('sin(Angle)',fontdict={'fontsize':10})
plt.legend()
plt.subplot(1, 2, 2) 
plt.plot(x, y2, color='green', label='cos(x)')
plt.grid()
plt.title('COS function Wave')
plt.xlabel('Angle',fontdict={'fontsize':10})
plt.ylabel('sin(Angle)',fontdict={'fontsize':10})
plt.legend()
plt.show()