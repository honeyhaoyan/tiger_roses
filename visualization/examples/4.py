import matplotlib.pyplot as plot
import numpy as np

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

plot.figure()
# use plot.contourf to filling contours
# X, Y and value for (X,Y) point
plot.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plot.cm.hot)

# use plot.contour to add contour lines
C = plot.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

plot.clabel(C, inline=True, fontsize=10)
plot.xticks(())
plot.yticks(())

plot.show()