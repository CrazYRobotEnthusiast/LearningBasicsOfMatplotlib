'''The scatter() function plots one dot for each observation.
 It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis'''
import matplotlib.pyplot as plt
import numpy as np
plt.scatter([5,7,8,7,2,17,2,9,4,11,12,9,6],[99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.xlabel("How old the car is? (in yrs)")
plt.ylabel("Speed at which car was passing(km/hr)")
plt.show()
#Rohit Saluja's code:-
xValues,yValues=[],[]
scatteredness=0.2
for i in range(40):
    for j in range(40-i):
        xValues.append(i+i*np.random.normal(0,scatteredness))
        yValues.append(i+i*np.random.normal(0,scatteredness))
'''In above code, we are creating points with noise around the line y=x. As the value of x increases,
the no of points decrease but their scatteredness increases.'''
xValues.append(100);
yValues.append(100);
plt.scatter(xValues,yValues)
plt.xlim(0,40)
plt.ylim(0,40)
plt.xlabel("Random x values",fontsize=24)
plt.ylabel("Random y values",fontsize=24)
plt.title('Increasingly random gaussian noise added to x and y in y=x',\
          fontsize=35)
plt.show()