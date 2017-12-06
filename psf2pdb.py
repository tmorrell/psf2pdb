from __future__ import print_function
import sys

pdbfile = open(sys.argv[1],'r')
psfile = open(sys.argv[2],'r')

inline = pdbfile.readline()
output = ''
while inline != 'END\n':
    output = output + inline
    inline = pdbfile.readline()
    if inline == '': #sanity check
        print("Error")
        exit()

inline = psfile.readline().split()
while inline[1] != '!NBOND:':
    inline = psfile.readline().split()
    while len(inline)<1:
        inline = psfile.readline().split()

bondlist = psfile.readline().split()
for i in range(int(inline[0])):
    new = int(bondlist.pop(0))
    output = output + 'CONECT%5d%5d\n' % (new, int(bondlist.pop(0)))
    if len(bondlist)==0:
        bondlist = psfile.readline().split()

outfile = open(sys.argv[3],'w')
outfile.write(output)
