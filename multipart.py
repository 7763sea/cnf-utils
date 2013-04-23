#!/usr/bin/env python

import sys, string, os

print "c %s" % sys.argv


#create header
headerNumVars = 0
headerNumCls = 0
at = 0
for f in sys.argv :
    at+=1
    if at == 1 :
        continue

    thisnumvars = 0
    ins = open( f, "r" )
    for line in ins :
        if line[0] == 'p' or line[0] == 'c' :
            continue

        for part in line.split() :
            thisnumvars = max(thisnumvars, int(part))

        headerNumCls += 1
    headerNumVars += thisnumvars

print "p cnf %d %d" % (headerNumVars, headerNumCls)

#print final CNF
ret = ""
at = 0
numvarsUntilNow = 0
for f in sys.argv :
    at+=1
    if at == 1 :
        continue

    thisnumvars = 0
    ins = open( f, "r" )
    for line in ins:
        #ignore header and comments
        if line[0] == 'p' or line[0] == 'c' :
            continue

        line = line.rstrip().lstrip()
        parts = line.split()
        towrite = ""
        for part in parts :
            #end of line
            if (part == "0") :
                towrite += "0"
                #sys.stdout.write("0\n")
                break

            #update number of variables in this part
            if int(part) > thisnumvars :
                thisnumvars = int(part)

            #increment variable number if need be
            newLit = abs(int(part)) + numvarsUntilNow

            #invert if needed
            if (int(part) < 0) :
                newLit = -1*newLit

            #write updated literal
            towrite += "%s " % newLit #sys.stdout.write("%d " % newLit)

        #end of this line in file
        print towrite

    #next part has to be updated with incremented varaibles
    numvarsUntilNow += thisnumvars




#file1 = sys.argv[1]
#file2 = sys.argv[2]