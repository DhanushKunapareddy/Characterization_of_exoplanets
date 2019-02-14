from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis
df = pd.read_csv("exoplanet.eu_catalog.csv")
ecc = df.eccentricity.tolist()
e = 0.0167
j = 0.048
pos_ecc=[i for i in ecc if i>0]    #To filter out positive eccentricities
print(len(pos_ecc))
print('avg = ',np.mean(pos_ecc))
pos_ecc.append(e)
pos_ecc.append(j)
ecct, _ = stats.boxcox(pos_ecc)  # Transformed eccentricities
et = ecct[pos_ecc.index(e)]
jt = ecct[pos_ecc.index(j)]
s = skew(ecct)
k = kurtosis(ecct)
m = np.mean(ecct)
sig = np.std(ecct)

sig_e = (et-m)/sig
print(sig_e)
sig_j = (jt-m)/sig
print(sig_j)

print('mean is ',m)
print('Skewness of the Distribution is ',s)
print('kurtosis of the Distribution is ',k)
print('standard deviation is ',sig)
plt.title('Distribution of eccentricities(Box-cox Transformed)')
range = (-3.4,0.0)
bins = 20
plt.hist(ecct, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)
plt.annotate('mean = -1.4879', xy=(m,103), xytext=(m-0.2, 113),arrowprops=dict(arrowstyle="->"))
plt.annotate('Earth(-1.6σ)', xy=(et,46), xytext=(et-0.145, 56),arrowprops=dict(arrowstyle="->"))
plt.annotate('Jupiter(-0.97σ)', xy=(jt,80), xytext=(jt-0.175,90),arrowprops=dict(arrowstyle="->"))
#plt.text(-3.5, 94, 'Skewness = -0.0576\nKurtosis = -0.5797\nStandard deviation = 0.6376',size = 15,bbox={'facecolor':'white','alpha':0.5, 'pad':10})
plt.text(-3.5, 94, 'Skewness = %.5f\nKurtosis = %.5f\nStandard deviation = %.5f'%(s,k,sig),size = 15,bbox={'facecolor':'white','alpha':0.5, 'pad':10})
plt.show()