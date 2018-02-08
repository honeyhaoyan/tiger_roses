import matplotlib.pyplot as plot
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plot.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plot.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plot.text(x , y , '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plot.text(x , -y , '%.2f' % y, ha='center', va='top')

plot.xlim(-1, n)
plot.xticks(())
plot.ylim(-1.25, 1.25)
plot.yticks(())

plot.show()