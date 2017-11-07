#!/usr/bin/python

import sys

out = sys.stdout
if len(sys.argv) > 2:
    out = open(sys.argv[2], 'w+')

with open(sys.argv[1], "r") as f:
    lastLine = None
    for line in f:
        if line[:2] in ("G0", "G1"):
            newLine = []
            for val in line.split():
                if val[0] in ("X", "Y"):
                    newLine.append(val[0] + "{0:.2f}".format(round(float(val[1:]), 2)))
                else:
                    newLine.append(val)
            line = ' '.join(newLine) + "\n"
            
            if lastLine is not None:
                if lastLine[:2] == newLine[0] == "G0":
                    sameRow = False
                    for val in lastLine.split():
                        if val[0] in ("Y") and val in newLine:
                            sameRow = True
                            break
                    if not sameRow:
                        out.write(lastLine)
                        out.write(line)
                        lastLine = None
                    else:
                        lastLine = line
                else:
                    out.write(lastLine)
                    if line != lastLine:
                        lastLine = line
                    else:
                        lastLine = None
            else:
                lastLine = line
        else:
            if lastLine:
                out.write(lastLine)
                lastLine = None
            out.write(line)

out.flush()
out.close()
