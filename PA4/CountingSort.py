A = [1,0,1,3,1,3,3,1,0]
def CountingSort(A, k):
#where k is the maximum value of A, it can be also given
    answer = []
    count = []
    for index1 in range (0, len(A)):
        answer.append(0)
    for index2 in range (0, k+1):
        count.append(0)
    for index3 in range (0, len(A)):
        count[A[index3]] += 1


    for index4 in range (1, k+1):
        count[index4] = count[index4] + count[index4-1]

    for i in range (0, k+1):
        count[i] -= 1

    print("count:  ", count)
    print("answer: ", answer)
    print("=================================================")
    for index in range (len(A)-1, -1, -1):
        answer[count[A[index]]] = A[index]
        count[A[index]] -= 1
        print("count:  ", count)
        print("answer: ", answer)
        print("=================================================")

    return answer


print(CountingSort(A,3))
