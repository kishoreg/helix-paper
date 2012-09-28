#!/usr/bin/python

from pylab import *

rcParams['font.size'] = 16
rcParams['figure.figsize'] = 8, 4

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True


xlabels = open("xlabel").read().split("\n")
plt1 = [int(x)/1000.0 for x in open("1024").read().split("\n")]
plt2 = [int(x)/1000.0 for x in open("2400").read().split("\n")]

plot(plt1, 'o-', label="1024", linewidth=2, ms=8)
plot(plt2, 's--', label="2400", linewidth=2, ms=8)
legend(title="# Partitions")

xticks(range(0, len(xlabels)), xlabels)

xlim(xmax=len(xlabels)-.9)

#make the axes sexy

ax=gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.xaxis.grid(False)
ax.set_axisbelow(True)


xlabel("Parallellism")
ylabel("Bootstrap Time (s)")


savefig("bootstrap.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)

