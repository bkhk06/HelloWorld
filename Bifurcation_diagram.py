import numpy as n
import scipy as s
import pylab as p

xa=0.252
xb=1.99

C=n.linspace(xa,xb,100)
print C
iter=1000
Y = n.ones(len(C))

for x in xrange(iter):
    Y = Y**2 - C   #get rid of early transients

for x in xrange(iter): 
    Y = Y**2 - C
    p.plot(C,Y, '.', color = 'k', markersize = 2)


p.show()
