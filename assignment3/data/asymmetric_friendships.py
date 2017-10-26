import MapReduce
import json
import sys

mr = MapReduce.MapReduce()
def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    #represent (a,b) and (b,a) as the same key
    mr.emit_intermediate(hash(key)+hash(value),record)

def reducer(key, list_of_values):

    if len(list_of_values) == 1:
        print key

        mr.emit((list_of_values[0][0], list_of_values[0][1]))
        mr.emit((list_of_values[0][1], list_of_values[0][0]))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
