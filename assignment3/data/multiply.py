import MapReduce
import json
import sys

mr = MapReduce.MapReduce()
#from matrix.json file, A, B are 5X5 matrix
max_dim = 5

def mapper(record):
    global max_dim
    key = str(record[1]) +''+ str(record[2])
    value = record[0] +''+ str(record[3])
    if record[0] == 'a':
       
        for k in range(0, max_dim):
            mr.emit_intermediate(str(record[1]) +''+ str(k), record)
    else:
        for j in range(0, max_dim):
            mr.emit_intermediate(str(j) +''+ str(record[2]), record)

def reducer(key, list_of_values):
    global max_dim
    temp = 0
    res = 0
    lst = []
    for term1 in list_of_values:
        for term2 in list_of_values:
            if term1[0] == 'a':
                if term1[2] == term2[1] and term2[0] == 'b':
                    temp = term1[-1] * term2[-1]
                    res += temp
    mr.emit((int(list(key)[0]), int(list(key)[1]), res))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
