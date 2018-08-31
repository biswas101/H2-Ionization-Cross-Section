# This script will plot Hydrogen Ionization cross section. based on Electron Energy
# Detailed calculation can be found on M. Resiser, P 245

'''
Created on July 25, 2018
@author:  Jyoti Biswas
'''

from matplotlib import cm

from pylab import figure
import matplotlib.pyplot as plt
import numpy as np
import math

m_e=0.511e6 # Mass of Electron

Uz = np.logspace(np.log10(1.542E1) , np.log10(1E6) , num=500)

Gz = 1 + (Uz/m_e)   # Gamma_Z

Bz = (1 - (1/(Gz**2)))**0.5   # Beta_Z


b_2 = Bz**2
g_2 = Gz**2

f = (6.027E-5)*(1.659E4*b_2 -1)/b_2

sigma = (1.301E-24)*f*(np.log(1.177E5*b_2*g_2) - b_2)/b_2

##print("len(Uz):", Uz[395])  # 350 --> 452

f= open("ionization_H2.txt","w")

for i in range(395):   # for 350 Kev change it to 452
    f.write("%e %e\n" %(Uz[i], sigma[i]))
f.close()

plt.plot(Uz, sigma)
plt.xlabel('Beam Energy [eV]')
plt.ylabel(r'Ionization Cross Section $[m^{2}]$')

plt.xscale('log')
plt.yscale('log')
plt.tick_params(top='on', right='on', which='both', direction="in")

plt.ylim((1E-23,5E-20))

#plt.savefig('ionization_cross_section_Reiser_1.png', dpi = 300)   # save the figure to file
plt.show()
