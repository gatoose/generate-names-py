#!/usr/bin/env python3

import itertools
import io
import random

adjectives = list(map(str.strip, io.open("namegen/adjectives_C.txt").readlines()))
animals    = list(map(str.strip, io.open("namegen/animals_C.txt").readlines()))
names      = list(map(str.strip, io.open("namegen/names_C.txt").readlines()))

random.shuffle(adjectives)
random.shuffle(animals)
random.shuffle(names)

adjectives = adjectives[:100]
animals = animals[:100]
names = names[:100]

things = itertools.product(adjectives, animals, names)
outputs = list(map(lambda _: "{} {} {}\n".format(*_), things))
random.shuffle(outputs)

io.open("output_file_1.txt", "w").writelines(outputs)
