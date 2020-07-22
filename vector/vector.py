import sys
import math
import csv
from math import sqrt



#intial some example
#define vector [ARCHER,TSAN,ROMP,INTEL,OpenMP Extractor, clause]

#input new vector

input_vector = input("enter your new vector separated by commas, end by enter:")
NEW_VECTOR=input_vector.split(",");

#load reference, directive map and clause map

Lines = csv.reader(open(sys.argv[1],"r"))
reference = list(Lines)

file = open(sys.argv[2],"r")
Lines = file.readlines()
directive = [line.strip() for line in Lines]

file = open(sys.argv[3],"r")
Lines = file.readlines()
clause = [line.strip() for line in Lines]

#mapping new director and their clause
for item in directive:
	directive_map = item.split(":")
	if NEW_VECTOR[4] == directive_map[0]:
		NEW_VECTOR[4] = directive_map[1]
for item in clause:
	clause_map = item.split(":")
	if len(NEW_VECTOR) >= 6:
		if NEW_VECTOR[5] == clause_map[0]:
			NEW_VECTOR[5] = clause_map[1]
if len(NEW_VECTOR) < 6:
	NEW_VECTOR.append(0)

#calcualte ED
if reference == []:
	reference.append(NEW_VECTOR)
	with open('reference.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(reference)
flag = 0;
for item in reference:
	dis = 0.0
	tmp = []
	for item1 in item:
		if item1.isnumeric():
			tmp.append(item1)
	for i in range(len(tmp)):
		dis = dis + pow((float(tmp[i]) - float(NEW_VECTOR[i])),2)
	dis = sqrt(dis)
	if dis > 0.5:
		flag = 1;
	else:
		flag = 0;
		break;
if flag == 0: 
    	print("it's similar pattern, please check and make sure it is not redundant!")
else:
	print("This is a new pattern add it to the reference file!")
	reference.append(NEW_VECTOR)
	with open('reference.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerows(reference)
'''

reference1_encode = []
reference2_encode = []
reference3_encode = []
new_encode = []
dis1 = 0
dis2 = 0
dis3 = 0
#encode the reference and new vector

for item in reference1:
    if item == TRUE:
        reference1_encode.append(0)
    elif item == FLASE:
        reference1_encode.append(1)
    elif item == TO:
        reference1_encode.append(3)
    elif item == SEG:
        reference1_encode.append(4)
    else:
        print("Your result is invalid!")
        
for item in reference2:
    if item == TRUE:
        reference2_encode.append(0)
    elif item == FLASE:
        reference2_encode.append(1)
    elif item == TO:
        reference2_encode.append(3)
    elif item == SEG:
        reference2_encode.append(4)
    else:
        print("Your result is invalid!")
        
for item in reference3:
    if item == TRUE:
        reference3_encode.append(0)
    elif item == FLASE:
        reference3_encode.append(1)
    elif item == TO:
        reference3_encode.append(3)
    elif item == SEG:
        reference3_encode.append(4)
    else:
        print("Your result is invalid!")

for item in NEW_VECTOR:
    if item == TRUE:
        new_encode.append(0)
    elif item == FLASE:
        new_encode.append(1)
    elif item == TO:
        new_encode.append(3)
    elif item == SEG:
        new_encode.append(4)
    else:
        print("Your result is invalid!")

#calculate the three distance

for i in range(4):
    dis1 = dis1 + pow((new_encode[i]-reference1_encode),2)
    dis2 = dis2 + pow((new_encode[i]-reference3_encode),2)
    dis3 = dis3 + pow((new_encode[i]-reference3_encode),2)
    dis1 = sqrt(dis1)
    dis2 = sqrt(dis2)
    dis3 = sqrt(dis3)

#check if it is similar pattern

if dis1 > 0.5 or dis2 > 0.5 or dis3 > 0.5:
    print("it's similar pattern")
else:
    reference = NEW_VECTOR
'''
