import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [0.206,0.007,0.017,0.093,0.048,0.056,0.047,0.009,0.248]
n = ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=5)
m = [np.sum(y)/9]*9
plt.plot(x,m,label = "mean = 0.0812")
plt.ylim(-0.05,0.26)
plt.xlim(0.9,9.5)
plt.title('eccentricities of planets in solar system')
plt.xticks(x,n)
plt.legend()
plt.show()