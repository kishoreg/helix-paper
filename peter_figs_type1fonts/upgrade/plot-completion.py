#!/usr/bin/python

from pylab import *

rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True
rcParams['text.usetex'] = True



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


pcts = [10, 20, 25, 50, 100]
times = []


for pct in pcts:
    t, p = get_data("%dpct.out" % (pct))
    times.append(max(t))

plot(pcts, times, 'o-', lw=2)

xlabel("Percent of Partitions Migrated Concurrently")
ylabel("Time Required")

legend(loc="lower right")

show()
