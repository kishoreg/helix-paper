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

data = [initial, first, second]

masters = []
mastererr = []

for d in data:
    masterload = [d[i][master_offset] for i in d.keys()]
    masters.append(average(masterload))
    mastererr.append(std(masterload))

slaves = []
slaveerr = []

for d in data:
    slaveload = [d[i][slave_offset] for i in d.keys()]
    slaves.append(average(slaveload))
    slaveerr.append(std(slaveload))

totals = []
totalerr = []

for d in data:
    totalload = [d[i][slave_offset]+d[i][master_offset] for i in d.keys()]
    totals.append(average(totalload))
    totalerr.append(std(totalload))

width = 1

xt = [i*width for i in range(0, 3)]

for i in range(0, 3):
    plta = bar(xt[i], masters[i], width*.8, color="#24938C", capsize=10, ecolor="black", lw=1.5)
    pltb = bar(xt[i], slaves[i], width*.8, bottom=masters[i], color="#5B7EB0", capsize=10, ecolor="black", lw=1.5)
    errorbar(xt[i]+width*.8/2, slaves[i]+masters[i], slaveerr[i], color="black", capsize=16, mew=1.5, elinewidth=1.5)

legend(title="Partition Type")

xticks([x+width*.8/2. for x in xt], ["Initial\n(N=20)", "Rebalance 1\n(N=25)", "Rebalance 2\n(N=30)"])

ylabel("Average Partitions Per Node")

xlim(xmin=-.2)

for tick in gca().xaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False


legend((pltb[0], plta[0]), ("Slave", "Master"), title="Partition Type")

savefig("rebalance.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)

