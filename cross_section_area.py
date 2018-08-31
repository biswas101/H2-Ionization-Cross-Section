#This script is specially designed to find  int(sigma .dE)
# after running cross_section_reiser.py, one can use it to get sigma.dE
# sigma.dE is needed to calculate the Flux of Trapped ions in DC gun
# More info can be found on https://journals.aps.org/prab/pdf/10.1103/PhysRevSTAB.10.083501

'''
Created on July 25, 2018
@author:  Jyoti Biswas
'''


from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
from numpy import genfromtxt
#from traitlets.traitlets import add_article


fig = plt.figure()
ax1 = fig.add_subplot(111)

D_mag= genfromtxt('ionization_H2.txt',delimiter='',dtype=None, names=True)

print("Please check the header of the txt file if you get any error, if Not, just disregard this message!! ")

X=np.array(D_mag['U'])
Y=np.array(D_mag['s'])


# finding the max and min point
Yo_neg=Y.min()
Yo_pos=Y.max()
Ycut_neg= abs(Yo_neg/1000)   # Value lower that Cut off, is not considered in calculation


print("number of Energy points:",len(X))
print("Sigma min: ", Yo_neg)
print("Sigma Max: ", Yo_pos)

print("Cut off Sigma(abs.):", Ycut_neg)

val_neg = 0.0

for i in range(len(X)-1):
    if abs(Y[i] - X[i])>Ycut_neg:
        val_neg = val_neg + (X[i+1]-X[i])*Y[i] + 0.5*(X[i+1]-X[i])*(Y[i+1] - Y[i])


print("Area (vector sum):", val_neg)

ax1.scatter(X,Y, s=10, c='b', marker="o", label='B-field')

plt.xscale('log')
plt.yscale('log')
plt.tick_params(top='on', right='on', which='both', direction="in")

plt.ylim((1E-23,5E-20))
plt.show()


