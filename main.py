import matplotlib.pyplot as plt
import numpy as np
import math

r = float(input("Enter a value for r bigger than 1: "))
xint = float(input("Enter a starting x value between 0 and 1 : "))
#r = 2
#xint = 0.2

x_L = ["true", "False"]
Condition = xint

xIsHotx = []
xIsHoty = []

Count = 0
xIsHotx.append(xint)
xIsHoty.append(0)
while x_L[Count] != x_L[Count - 1]:
    x_L.append(xint)
    xIsHotx.append(xint)
    xIsHoty.append(r * (1 - xint) * xint)
    xint = r * (1 - xint) * xint
    xIsHotx.append(xint)
    xIsHoty.append(xint)
    Count = Count + 1
    if Count > 9999999:
        break

x = np.linspace(-4, 4, 1000)
y = r * (1 - x) * x
x1 = np.linspace(-4, 4, 1000)
y1 = x

if Condition < 1:
    if xIsHotx[len(xIsHotx) - 1] == xIsHotx[len(xIsHotx) - 3]:
        plt.plot(xIsHotx, xIsHoty, 'k')
        plt.plot(x, y, 'r',
                 x1, y1, 'b')
        plt.plot(xIsHotx[len(xIsHotx) - 1], xIsHoty[len(xIsHoty) - 1], '.g')
        plt.axis([0, 1.5, 0, 1.5])
        plt.show()
    else:
        plt.plot(xIsHotx, xIsHoty, 'k')
        plt.plot(x, y, 'r',
                 x1, y1, 'b')
        plt.plot(xIsHotx[len(xIsHotx) - 1], xIsHoty[len(xIsHoty) - 1], '.g',
                 xIsHotx[len(xIsHotx) - 2], xIsHoty[len(xIsHoty) - 2], '.g',
                 xIsHotx[len(xIsHotx) - 3], xIsHoty[len(xIsHoty) - 3], '.g',
                 xIsHotx[len(xIsHotx) - 4], xIsHoty[len(xIsHoty) - 4], '.g')
        plt.axis([0, 1.5, 0, 1.5])
        plt.show()
else:
    print("Enter a starting number withinn the parameters")
