from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

df = pd.read_csv("exoplanet.eu_catalog.csv")
semi = df.semi_major_axis.tolist()
print('length = ',len(semi))
#mer = 0.387
e = 1
j = 5.2
pos_semi=[i for i in semi if i>0]    #To filter out positive semi major axes
#pos_semi.append(mer)
pos_semi.append(e)
pos_semi.append(j)
semit, _ = stats.boxcox(pos_semi)  # Transformed semi major axes

#mert = semit[pos_semi.index(mer)]
et = semit[pos_semi.index(e)]
jt = semit[pos_semi.index(j)]
s = skew(semit)
k = kurtosis(semit)
m = np.mean(semit)
sig = np.std(semit)

# sig_mer = (mert-m)/sig
# print(sig_mer)
sig_e = (et-m)/sig
print('sig_e = ', sig_e)
sig_j = (jt-m)/sig
print(sig_j)

fig = plt.figure()
ax = fig.add_subplot(111)
print('mean is ',m)
print('Skewness of the Distribution is ',s)
print('kurtosis of the Distribution is ',k)
print('standard deviation is ',sig)
plt.title('Distribution of semi_major_axes(Box-cox Transformed) of confirmed exoplanets')
ax.set_xlabel('y_$\lambda$(a/AU)')
ax.set_ylabel('NP')
range = (-9.5,3.5)
bins = 15
plt.hist(semit, bins, range, color = '#21618C', histtype = 'bar', rwidth = 0.9)
# plt.annotate('Mercury(0.71σ)', xy=(mert,470), xytext=(mert-0.72, 620),arrowprops=dict(arrowstyle="->"))
plt.annotate('Earth(0.966σ)', xy=(et,290), xytext=(et-0.65, 330),arrowprops=dict(arrowstyle="->"))
plt.annotate('Jupiter(1.529σ)', xy=(jt,300), xytext=(jt-0.7,350),arrowprops=dict(arrowstyle="->"))
plt.text(-9.8,310,'Skewness = 0.1297\nKurtosis = -0.4998\nStandard deviation = 2.3897',size = 15,bbox={'facecolor':'white','alpha':0.5, 'pad':10})
plt.show()