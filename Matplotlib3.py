import matplotlib.pyplot as plt
#Bar Charts
labels=['a','b','c']
values=[1,4,2]
plt.bar(labels,values)
plt.show()
#Bar charts with designs
a=plt.bar(labels,values)
a[0].set_hatch('/')
a[1].set_hatch('o')
a[2].set_hatch('*')
'''Rather than above 3, we could have done;-
patterns=['\','o','*']
for i in a:
   i.set_hatch(patterns.pop())
'''
plt.show()
