import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
import time
import math

start_time = time.clock()

df = pd.read_csv("exoplanet.eu_catalog.csv")

mass = df.mass.tolist()
radius = df.radius.tolist()
mod_mass = []
mod_radius = []

for i in range(0,len(mass)):
	if mass[i] > 0 and radius[i] > 0:
		mod_mass.append(mass[i])
		mod_radius.append(radius[i]) #mod indicates 'modified'.
print('n = ',len(mod_radius))

volume = [4*np.pi*(i**3)/3 for i in mod_radius]
density = []
for i in range(0,len(mod_mass)):
	density.append(5.55469*mod_mass[i]/volume[i])

solar_mass = [0.00017,0.00256,0.00315,0.00034,1,0.299,0.046,0.054]
solar_density = [5.4,5.2,5.5,3.9,1.3,0.7,1.3,1.6]

# log_mass = [math.log(i) for i in solar_mass]
# log_density = [math.log(i) for i in solar_density]
xset = [0.00315]*2
x1set = [0.0315]*2
yset = [0,10000]

plt.loglog(mod_mass,density, 'o')
plt.loglog(solar_mass,solar_density,'s')
plt.plot(xset,yset,'--k')
plt.plot(x1set,yset,'--k')
plt.text(10**(-2.3),10**(3.5),'Super-Earths')
plt.text(10**(-1),10**(3.5),'Giant planets')
plt.xlabel('M/M_ J')
plt.ylabel('density(g/$cm^{3})$')
plt.title('Density vs Mass')
plt.show()
print(time.clock() - start_time, "seconds")