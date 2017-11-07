#!/usr/bin/python

import sys
import serial
import time

if len(sys.argv) > 2:
    passes = int(sys.argv[2])
else:
    passes = 1

with open(sys.argv[1], "r") as f:
    with serial.Serial('/dev/ttyUSB0', 57600) as s:
        s.parity = serial.PARITY_ODD # work around pyserial issue #30
        s.parity = serial.PARITY_NONE

        print(s.readline())

        s.write("?\n")
        s.flush()
        res = s.readline()
        print(res)
        if res[0] == '!':
            raw_input("Press to continue")
            s.write('~\n')
            s.flush()
	
        for i in range(passes):
            print("Pass: " + str(i + 1))
            f.seek(0)
            for line in f:
                s.write(line.strip() + '\n')
                s.flush()
                s.readline()
