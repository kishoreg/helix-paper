#!/usr/bin/python

from pylab import *

rcParams['font.size'] = 16
rcParams['figure.figsize'] = 8, 4

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True

xlabels = open("xlabel").read().split("\n")
plt150 = [int(x)/1000.0 for x in open("150").read().split("\n")]
plt750 = [int(x)/1000.0 for x in open("750").read().split("\n")]
plt3600 = [int(x)/1000.0 for x in open("3600").read().split("\n")]

plot(plt150, 'o-', label="150", linewidth=2, ms=10)
plot(plt750, 's--', label="750", linewidth=2, ms=10)
plot([2,3], plt3600, 'v-', label="3600", linewidth=2, ms=10)
xlim(xmax=3.04)
legend(title="# Partitions")

xticks(range(0, len(xlabels)), xlabels)



ax=gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.xaxis.grid(False)
ax.set_axisbelow(True)


xlabel("Parallellism")
ylabel("Failover Time (s)")


savefig("failure.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)

