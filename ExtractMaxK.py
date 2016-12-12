import random

import time

from HeapImplementation import *

def ExtractMaxK (NumberList, k):
    output = []
    a = HeapBuildMaxHeap(NumberList)
    for i in range(k):
        output.append(HeapExtractMax(NumberList))
    return output

def RandListGen(n):
    return [random.randint(0, n) for i in range(n)]

test = [(RandListGen(10), 3), (RandListGen(100), 5), (RandListGen(200), 7), (RandListGen(700), 10), (RandListGen(1000), 10),
        (RandListGen(2000), 15), (RandListGen(3500), 20), (RandListGen(5000), 30), (RandListGen(7500), 35), (RandListGen(10000), 40)]

for element in test:
    start = time.time()
    ExtractMaxK(element[0], element[1])
    end = time.time();
    print (end-start)*1000