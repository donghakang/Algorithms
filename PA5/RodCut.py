def CutRod(prc, total_len):
    rev = [0] * (total_len + 1)
    split = [0] * (total_len + 1)

    for j in range (1, total_len+1):
        best = 10000
        for index3 in range (1, j+1):
            if best > prc[index3] + rev[j-index3]:
                best = prc[index3] + rev[j-index3]
                split[j] = index3
        rev[j] = best

    print(rev)
    print(split)
    num = total_len
    correct = []
    while num > 0:
        correct.append(split[num])
        num = num - split[num]
    print(correct)


A = [0, 4, 7, 7, 7, 7, 7, 8, 9, 10, 11,
       15, 16, 19, 20, 21, 23, 24, 24, 24, 24,
       24, 24, 24, 24, 31, 32, 32, 34, 34, 34,
       35, 35, 36, 36, 39, 39, 39, 40, 41, 41,
       41, 44, 45, 45, 46, 47, 48, 49, 51, 53]


B = CutRod(A,35)
print(B)
