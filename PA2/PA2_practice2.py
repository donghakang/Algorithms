#Takes in list of Emails A, and indices p and r
#Chooses A[r] as a pivot Email and re-orders the list so that
#all Emails with a longer sender name than the pivot come
#before the pivot in the list, and all Emails with a shorter
#sender name come after.
#Returns the index where the pivot is located
A = [3,6,2,9,8,7]
B = [0,5]


def partition(A,p,r):
    Pivot = A[r]
    i = p - 1
    for j in range (p, r):
        if A[j] >= Pivot:
            i = i + 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp2 = A[i+1]
    A[i+1] = A[r]
    A[r] = temp2
    return i+1
    pass



#Takes in list of Emails A, and indices p and r
#Sorts the sublist A[p...r], in order of the length of each Email's
#sender, from longest name to shortest, using Quicksort
#Returns nothing
def quicksort(A,p,r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    pass

quicksort(A,0,5)
print(A)
