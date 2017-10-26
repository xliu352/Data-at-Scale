import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    
    mr.emit((key, len(list_of_values)))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
