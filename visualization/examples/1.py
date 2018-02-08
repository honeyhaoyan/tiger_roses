import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(-1, 1, 50)
y = x * 2 + 1

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plot.figure()
l1, = plot.plot(x, y2, label="linear line")
l2, = plot.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label="square line")
# plot.legend(handles = [l1,l2], labels = ["upper", "down"], loc='best')
plot.legend(handles = [l1,l2], labels = ["upper", "down"], loc='upper right')
plot.xlim((-1, 2))
plot.ylim((-2, 3))

new_ticks = np.linspace(-1, 2, 5)
plot.xticks(new_ticks)
plot.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

ax = plot.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('both')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))

x0 = 0.5
y0 = int(2*x0 + 1)
plot.plot([x0, x0], [0, y0], 'k--', linewidth=1.5)
# set dot styles
plot.scatter([x0], [y0], s=50, color='b')

plot.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+15, -15),
             textcoords='offset points', fontsize=10,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plot.text(-1, 2, r'$Beautiful\ images!$',
         fontdict={'size': 10, 'color': 'b'})

# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(12)
#     # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
#     label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))

plot.show()