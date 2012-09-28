#!/usr/bin/python

from pylab import *

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True

rcParams['font.size'] = 12
rcParams['legend.fontsize'] = 12
rcParams['figure.figsize'] = 8, 2

def get_data(f):
    lines = open(f).read().split('\n')
    
    times = []
    partitions = []
    
    starttime = None
    
    prevp = 0
    prevt = 0
    gaptime = 0

    for line in lines:
        if line == "":
            continue
        curtime = int(line.split()[2])/1000.

        if starttime == None:
            starttime = curtime

        curp = int(line.split()[3])

        if prevp == 2000 and curp != 2000:
            gaptime += (curtime-prevt)

        times.append(curtime-starttime-gaptime)

        partitions.append(curp)

        prevt = curtime
        prevp = curp

    return times, partitions


for pct in [25, 50, 100]:
    t, p = get_data("%dpct.out" % (pct))
    
    plot(t,p, label=str(pct)+"%", lw=2)

xlabel("Time (s)")
ylabel("Live Partitions")

legend(loc="lower right", title="Concurrently Migrated")

savefig("migration-timeseries.pdf", transparent=True, bbox_inches='tight', pad_inches=.05)

