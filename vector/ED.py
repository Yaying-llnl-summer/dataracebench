import sys
import math
import csv
from math import sqrt
import re



#intial some example
#define vector [directive, clause,ARCHER,TSAN,ROMP,INTEL,loopdepth]


#load vector, directive map and clause map

Lines = csv.reader(open(sys.argv[1],"r"))
vector = list(Lines)
w = 117
h = 117
ed = [[0 for x in range(w)] for y in range(h)]

for x in range(117):
    ed[0][x] = 'DRB' + str(x)
    ed[x][0] = 'DRB' + str(x)
i = 1
for item in vector:
        j = 1
        for x in vector:
            dis = 0
            for k in range(len(item)):
                dis = dis + pow((float(item[k]) - float(x[k])),2)
            dis = sqrt(dis)
            ed[i][j] = dis
            j += 1
        i += 1

with open("distance.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(ed)
