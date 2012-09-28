#!/usr/bin/python

from pylab import *

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True

rcParams['font.size'] = 8
rcParams['figure.figsize'] = 8, 2

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

initialcolor = "#3DCC53"
initialcolorslave = "#B5F5BF"

firstcolor = "#533DCC"
firstcolorslave = "#BFB5F5"

secondcolor = "#CC533D"
secondcolorslave = "#F5BFB5"

width = 1
spacewidth=1.5

base = 3

plotpoints = [base+(3*width+spacewidth)*i for i in range(0, len(second))]
plotpoints.append(len(second)*(3*width+spacewidth)+6)

for i in range(0, len(initial)):
    xpos = plotpoints[i]
    p1 = bar(xpos, initial[i][master_offset], width, color=initialcolor)
    bar(xpos, initial[i][slave_offset], width, bottom=initial[i][master_offset], color=initialcolorslave)

for i in range(0, len(first)):
    xpos = plotpoints[i]+width
    p2 = bar(xpos, first[i][master_offset], width, color=firstcolor)
    bar(xpos, first[i][slave_offset], width, bottom=first[i][master_offset], color=firstcolorslave)

for i in range(0, len(second)):
    xpos = plotpoints[i]+2*width
    p3 = bar(xpos, second[i][master_offset], width, color=secondcolor)
    bar(xpos, second[i][slave_offset], width, bottom=second[i][master_offset], color=secondcolorslave)

width=2
xpos = max(plotpoints)
masteravg = average([x[master_offset] for x in initial.values()])
slaveavg = average([x[slave_offset] for x in initial.values()])
bar(xpos, masteravg, width, color=initialcolor)
bar(xpos, slaveavg, width, bottom=masteravg, color=initialcolorslave)

xpos = max(plotpoints)+width
masteravg = average([x[master_offset] for x in first.values()])
slaveavg = average([x[slave_offset] for x in first.values()])
bar(xpos, masteravg, width, color=firstcolor)
bar(xpos, slaveavg, width, bottom=masteravg, color=firstcolorslave)

xpos = max(plotpoints)+2*width
masteravg = average([x[master_offset] for x in second.values()])
slaveavg = average([x[slave_offset] for x in second.values()])
bar(xpos, masteravg, width, color=secondcolor)
bar(xpos, slaveavg, width, bottom=masteravg, color=secondcolorslave)

xlabels = [str(i) for i in second.keys()]
xlabels.append("Avg")
xticks([p+width/2 for p in plotpoints], xlabels)


gca().get_xaxis().tick_bottom()

for tick in gca().xaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False

xlabel("Node Id")
ylabel("Number of Partitions")

xlim(xmax=150)

#legend((p1[0], p2[0], p3[0]), ('Initial', 'First Rebalance', 'Second Rebalance'))

savefig("rebalance.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)

    
