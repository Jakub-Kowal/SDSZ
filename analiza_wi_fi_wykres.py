import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import math
#L=10*4*log(d)+C

def oblicz_sile(d,C,tlumienie):
    return (10*4*math.log10(d)+C)+tlumienie

def odleglosc(x,y):
    suma=x*x
    suma+=y*y
    return math.sqrt(suma)

#A = np.random.rand(50, 68)
A=[]
for i in range(51):
    A.append([0 for i in range(68)])


#10 Kuchania
for i in range(25):
    for j in range(29):
        d=odleglosc(i,j)
        if d<=0:
            A[i][j]=0
        else:
            A[i][j]=(oblicz_sile(odleglosc(i,j),4,0))


#11 Pokoj
for i in range(25,51):
    for j in range(25):
        A[i][j] = (oblicz_sile(odleglosc(i, j), 4,9))


#12 Lazienka
for i in range(25,35):
    for j in range(32,51):
        A[j][i] = (oblicz_sile(odleglosc(i, j), 4, 16))


#9 Pokoj
for i in range(29,48):
    for j in range(25):
        A[j][i] = (oblicz_sile(odleglosc(i, j), 4, 7))

#8 Pojoj
for i in range(24,51):
    for j in range(49,68):
        A[i][j] = (oblicz_sile(odleglosc(i, j), 4, 23))

#korytarz
for i in range(25,33):
    for j in range(25,49):
        A[i][j] = (oblicz_sile(odleglosc(i, j), 4, 8))


#schody
for i in range(33,51):
    for j in range(35,49):
        A[i][j] = (oblicz_sile(odleglosc(i, j), 4, 20))

# for i in range(51):
#     for j in range(68):
#         A[i][j]/=1000

for i in A:
    print(i)

extent = (0, 68, 0, 50)
fig, axs = plt.subplots()
axs.imshow(A, interpolation='bilinear', cmap='hsv',origin='upper',extent=extent)

plt.show()
