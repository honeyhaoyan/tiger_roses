import matplotlib.pyplot as plot
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # for color value

plot.scatter(X, Y, s=75, c=T, alpha=.5)

plot.xlim(-1.5, 1.5)
plot.xticks(())  # ignore xticks
plot.ylim(-1.5, 1.5)
plot.yticks(())  # ignore yticks

plot.show()