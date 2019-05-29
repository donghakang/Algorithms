A = [8, 5, 12, 12, 15, 20, 8, 5, 18, 5]

def parent(i):
    return int((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def MaxHeapify(A,i):
    largest = A[i]
    L = left(i)
    R = right(i)
    if L < len(A) and A[L] > A[i]:
        largest = L
    else:
        largest = i

    if R < len(A) and A[R] > A[largest]:
        largest = R

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A,largest)


def BuildMaxHeap(A):
    for i in range(int(len(A)/2)-1,-1,-1):
        MaxHeapify(A,i)




def heapincreasekey(A,i,key):
    if key < A[i]:
        return None

    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

    pass

def heapincreasekey2 (A, i):
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
    pass

def maxheapinsert(A,key):
    A.append(-10)
    i = len(A)-1
    heapincreasekey(A,i,key)
    pass

def HeapExtractMax(A):
    max = A[0]
    A[0] = A[len(A)-1]
    MaxHeapify(A,0)
    pass


def HeapDelete(A, i):
    A[i] = A[len(A)-1]          # first exchange with last node
                                # A[i] = A[A.heap-size]

    if A[i] > A[parent(i)]:
        while i > 0 and A[parent(i)] < A[i]:
            A[i], A[parent(i)] = A[parent(i)], A[i]
            i = parent(i)
    else:
        MaxHeapify(A,i)
    pass


A = [9,3,7,1,2,6]
print(A)
HeapDelete(A,3)
print(A)

B = [9,8,2,6,5,1]
print(B)
HeapDelete(B,1)
print(B)

C = [20, 20, 20, 3, 3, 20, 20, 2, 2, 3, 3, 20]
print(C)
HeapDelete(C,7)
print(C)
