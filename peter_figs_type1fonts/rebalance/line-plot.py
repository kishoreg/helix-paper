#!/usr/bin/python

from pylab import *

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True

rcParams['font.size'] = 16
rcParams['legend.fontsize'] = 16
rcParams['figure.figsize'] = 8, 4

def parse_file(f):
    ret = {}
    lines = open(f).read().split("\n")
    for line in lines:
        ret[int(line.split(":")[0][5:])] = [int(i) for i in line.split(":")[1][2:].split("   ")]
    return ret

master_offset = 1
slave_offset = 2

initial = parse_file("initial")
first = parse_file("balance1")
second = parse_file("balance2")

sizes = [20, 25, 30]
data = [initial, first, second]

masters = []
mastererr = []

for d in data:
    masterload = [d[i][master_offset] for i in d.keys()]
    masters.append(average(masterload))
    mastererr.append(std(masterload))

errorbar(sizes, masters, yerr=mastererr, label="Master", linewidth=2, ms=8)

slaves = []
slaveerr = []

for d in data:
    slaveload = [d[i][slave_offset] for i in d.keys()]
    slaves.append(average(slaveload))
    slaveerr.append(std(slaveload))

errorbar(sizes, slaves, yerr=slaveerr, label="Slave", linewidth=2, ms=8)

xlabel("Cluster Size (Nodes)")
ylabel("Average Number of Partitions per Node")

legend(title="Partition Type")

xticks([20, 25, 30])
xlim(xmin=19, xmax=31)


show()
#legend((p1[0], p2[0], p3[0]), ('Initial', 'First Rebalance', 'Second Rebalance'))

savefig("rebalance.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)

