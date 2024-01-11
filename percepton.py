import numpy as np
import matplotlib.pyplot as plt

a = -1
b= 4
c=0.4

def plotline(a, b, c):
    #ax +bx +c = 0
    x = np.linspace(-2,4,50)

    #y = (-a*x -c)/b
    y = (-a*x -c)/b
    print(x)

    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.plot(x,y)
    plt.grid(True)

plotline(a,b,c)

p1 = (2, 0.4)
p2 = (1, 0.6)
p3 = (3, -0.4)

plotline(a,b,c)
plt.plot(p1[0], p1[1], 'bo')
plt.plot(p2[0], p2[1], 'ro')
plt.plot(p3[0], p3[1], 'go')

plt.savefig('imagem_resultado.png')

ret1 = a*p1[0] + b*p1[1] + c
print('%.2f' % ret1)

ret2 = a*p2[0] + b*p2[1] + c
print('%.2f' % ret2)

ret3 = a*p3[0] + b*p3[1] + c
print('%.2f' % ret3)