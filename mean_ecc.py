from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd_data = pd.read_csv("exoplanet.eu_catalog.csv")

meane=pd_data.groupby('star_name')['eccentricity'].mean().values

mina = pd_data.groupby('star_name')['semi_major_axis'].min().values 

s = pd_data.groupby('star_name')['# name'].count().values
#print(s)
mod_meane = []
mod_mina = []
mod_s = []
# i=np.where((meane>0) & (mina>0))
# mod_meane=meane[i]
# mod_mina=mina[i]
# s=s[i]

mina_sol = [0.387]
meane_sol = [0.0812]

for i in range(0,len(meane)):
    if meane[i] > 0 and mina[i] > 0 and s[i]>0:
        mod_meane.append(meane[i])
        mod_mina.append(mina[i]) #mod indicates 'modified'.
        mod_s.append(s[i])

print('n = ',len(mod_meane))
print('n = ',len(mod_mina))
print('n = ',len(mod_s))
#color= ['blue' if i == 1  'red' elif i==2  'purple' elif i==3  'green' elif i==4  else 'orange' for i in mod_s]
color = []
for i in mod_s:
	if i==1:
		color.append('blue')
	elif i==2:
		color.append('red')
	elif i==3:
		color.append('purple')
	elif i==4:
		color.append('green')
	else:
		color.append('orange')
#size = [3*i for i in mod_s]
#print(mod_s)
plt.scatter(mod_mina,mod_meane,s=3*s**2,marker='o',color= color)
plt.scatter(mina_sol,meane_sol,s=3*8**2,marker='o',color= '#c712ea')
#plt.semilogx(mod_mina,mod_meane,"o")
plt.xlabel('Minimum Semi-Major Axis/AU')
plt.ylabel('Average Eccentricity')
ax=plt.gca()
ax.set_xscale('log')
plt.show()
