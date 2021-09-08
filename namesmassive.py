#!/usr/bin/env python3                                                                
                                                                                       
import itertools                                                                    
import io                                                                             
import random

adjectives = map(str.strip, io.open("namegen/adjectives.txt").readlines())                    
animals    = map(str.strip, io.open("namegen/animals.txt").readlines())                       
names      = map(str.strip, io.open("namegen/names.txt").readlines())                         






things = itertools.product(adjectives, animals, names)                                
outputs = list(itertools.islice(map(lambda _: "{} {} {}\n".format(*_), things), 100000000000000000))       
random.shuffle(outputs)                                                                                      
io.open("output_file.txt", "w").writelines(outputs)   

