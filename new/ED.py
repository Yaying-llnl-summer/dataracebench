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
w = len(vector) + 1
ed = [[0 for x in range(w)] for y in range(w)]
ed[0][0] = "test name"
for x in range(len(vector)):
    ed[0][x+1] = vector[x][0]
    ed[x+1][0] = vector[x][0]

i = 1
for item in vector:
        j = 1
        for x in vector:
            dot = 0
            a = 0
            b = 0
            for k in range(1,len(item)):
                dot += float(item[k]) * float(x[k])
                a += pow(float(item[k]),2)
                b += pow(float(x[k]),2)
            dis = dot / (sqrt(a) * sqrt(b))
            ed[i][j] = dis
            j += 1
        i += 1

with open("cosdistance.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(ed)
