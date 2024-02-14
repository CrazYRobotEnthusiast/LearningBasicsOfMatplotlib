import matplotlib.pyplot as plt
#Keep checking matplotlib documentation; very helpful
plt.plot([1,2,3],[1,4,9]) 
plt.title("Our First Graph")
#1st argument is array of x coord and 2nd argument is array of corresponding y points
plt.show() #Will immediately show graph, further functions will work on separate graph
plt.title('Our Second Graph',fontdict={'fontname':'Comic Sans MS','fontsize':20}) #Adds Title
plt.xlabel('X AXIS!!',fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.ylabel('Y AXIS!!')
plt.show() #Empty Graph
plt.plot([1,2,3],[2,4,6],label='2x', color='red',linewidth=12,marker='.',markersize=20,markeredgecolor='yellow',linestyle='--')
#Putting label in above is important for legend. Also value in colour can be passed as hexadecimal (ex '#ababab') or a common colour name
plt.xticks([1,2,3,7,7.5,10]) #Only show us these points on x axis; that too perfectly spaced
plt.yticks([2,4,6,8,50])
plt.legend() #Used to show the 2x label
plt.show() #Note how in this graph, the line does not extend after x=3
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y,'r^--',label='2x' ) #Shortcut [color][marker][style]
plt.show()