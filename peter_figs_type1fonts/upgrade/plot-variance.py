#!/usr/bin/python

from pylab import *

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True

rcParams['font.size'] = 12
rcParams['legend.fontsize'] = 12
rcParams['figure.figsize'] = 8, 4

def get_data(f):
    lines = open(f).read().split('\n')
    
    unavailability = []
    
    starttime = None
    
    prevp = 0
    prevt = 0
    gaptime = 0
    epochstart = 0

    for line in lines:
        if line == "":
            continue

        curtime = int(line.split()[2])/1000.

        if starttime == None:
            epochstart = curtime
            starttime = curtime

        curp = int(line.split()[3])

        if prevp == 2000 and curp != 2000:
            epochstart = curtime

        partitionsonline = curp-prevp
        for i in range(0, partitionsonline):
            unavailability.append(curtime-epochstart)

        prevt = curtime
        prevp = curp

    return unavailability


pcts = [10, 20, 25, 50, 100]
times = []

us = []
uerr = []

for pct in pcts:
    u = get_data("%dpct.out" % (pct))

    print u
    us.append(average(u))
    uerr.append(std(u))


errorbar(pcts, us, fmt='o-', yerr=uerr, lw=2, capsize=10, mew=2, markeredgecolor="blue")

xlim(xmin=8, xmax=102)
ylim(ymin=0)

xlabel("Percent of Partitions Migrated Concurrently")
ylabel("Average Per-Partition Unavailability (s)")

legend(loc="lower right")

savefig("average-migration.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)
