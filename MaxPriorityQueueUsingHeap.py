from HeapImplementation import *

def MPQCreate():
  return []

def MPQCreate(A):
  return HeapBuildMaxHeap(A)

def MPQEnqueue(A, key):
  HeapMaxHeapInsert(A, key)

def MPQDequeue(A):
  return HeapExtractMax(A)

def MPQIncreasePriority(A, i, newKey):
  if(A[i]<newKey):
    HeapIncreaseKey(A, i, newKey)


def MPQDecreasePriority(A, i, newKey):
  if(A[i]>newKey):
    HeapIncreaseKey(A, i, newKey)

myHeap = ['Empty', 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

myPQ = MPQCreate(myHeap)
print myPQ

MPQDecreasePriority(myPQ, 1, 0)
print myPQ