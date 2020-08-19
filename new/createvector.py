import sys
import math
import csv
from math import sqrt
import re



#intial some example
#define vector [directive, clause,ARCHER,TSAN,ROMP,INTEL,loopdepth]


#load reference, directive map and clause map

file = open(sys.argv[1],"r")
Lines = file.readlines()
testfile = [line.strip() for line in Lines]

file = open(sys.argv[2],"r")
Lines = file.readlines()
directive = [line.strip() for line in Lines]

file = open(sys.argv[3],"r")
Lines = file.readlines()
clause = [line.strip() for line in Lines]

file = open(sys.argv[4],"r")
Lines = file.readlines()
result = [line.strip() for line in Lines]
data = []
for item in result:
    x = item.split(",")
    data.append(x)
mark = 0
w = 128
vector = []
newvector = []
for item in testfile:
    x = re.search("^RUNNING",item)
    if x:
        name = item.split("/")
        number = name[1].split("-",1)
        id = re.search('[1-9]\d*', number[0]).group()
        mark = int(id)
    else:
        para = item.split(":")
        if para[0] == "loopid ":
            if newvector:
                vector.append(newvector)
            newvector = [0 for x in range(w)]
            newvector[0] = "DRB" + id + "+" + "loop" + para[1]
            newvector[124] = data[mark+1][3]
            newvector[125] = data[mark+1][5]
            newvector[126] = data[mark+1][7]
            newvector[127] = data[mark+1][9]
        elif para[0] == "pragam ":
            for dire in directive:
                direx = dire.split(":")
                if direx[0] == para[1]:
                    i = int(direx[1]) + 1
                    newvector[i] = 1;
        elif para[0] == "clause ":
            for clau in clause:
                claux = clau.split(":")
                if claux[0] == para[1]:
                    i = int(claux[1]) + 87
                    newvector[i] = 1;
        elif para[0] == "END ":
            vector.append(newvector)
        else:
            print("wrong input!")
            print(para)
with open("vector.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(vector)
'''
for item in testfile:
    x = re.search("^RUNNING",item)
    if x:
        name = item.split("/")
        number = name[1].split("-",1)
        id = re.search('[1-9]\d*', number[0]).group()
        mark = int(id)
    else:
        para = item.split(":")
        if para[0] == "pragam ":
            for dire in directive:
                direx = dire.split(":")
                if direx[0] == para[1]:
                    i = int(direx[1])
                    vector[mark-1][i] = 1;
        elif para[0] == "clause ":
            for clau in clause:
                claux = clau.split(":")
                if claux[0] == para[1]:
                    i = int(claux[1]) + 86
                    vector[mark-1][i] = 1;
        else:
            print("wrong input!")
with open("vector.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(vector)
'''
