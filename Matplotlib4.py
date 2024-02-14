import matplotlib.pyplot as plt
import numpy as np
# To study histograms: https://byjus.com/maths/histogram/
hBins=np.arange(155,165,0.5)
print(list(hBins))
ht1=np.random.randint(157,163,size=1000)
print(list(ht1))
plt.subplot(211) #Make two rows and 1 column, and assign this particular graph the first position
#To understand basic hist: https://www.w3schools.com/python/matplotlib_histograms.asp
'''
Basically what happens in hist is jab ham usme koi list pass karte hain (ex: [171,172,171,171,171,181,180,182])
then voh ek histogram banayega with class intervals 170-175, 175-180, 180-185 and the frequencies being 5,0,3
bins is used to define the class intervals; otherwise they are pre defined
'''
histD=plt.hist(ht1,label='Indian Height', bins=hBins, rwidth=0.7) 
#to Understand bins:https://www.geeksforgeeks.org/bin-size-in-matplotlib-histogram/ a
plt.xticks(hBins)
plt.legend(frameon=True) #Taaki legend grid ke upar alag se dikhe
plt.title('Heights of Indian and Dutchmen(cm)')
plt.grid(True)
histD=np.random.randint(168,173,size=1000)
hBins=np.arange(165,175,0.5)
plt.subplot(212)
plt.hist(histD,bins=hBins,rwidth=0.7,label='Dutch Height')
plt.legend(frameon=True)
plt.xticks(hBins)
plt.grid(True)
plt.show()
'''
Next time when drawing two histograms/ bar graphs in same plot, take the bins as more general and equal.Ex: check image1 in this folder
Or try to have 2 y axes!!
'''
#Histogram with designs:-
import numpy as np
val = np . random . normal ( size =(100) , scale =3 , loc =10)
bins =np. arange (0 ,20 ,0.25)
plt . hist ( val , bins =bins,edgecolor="red", color="green")
plt.xlabel('x-xis',fontdict={'fontsize':20})
plt.ylabel('y-axis',fontdict={'fontsize':20})
plt.grid()
plt . show ()