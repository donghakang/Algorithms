
# C is a set of n characters and the each character c is with in class
def Huffamn(C):
    n = |C|
    Q = C
    for i = 1 to n - 1:
        allocate a new node z
        z.left = x = Extract-min(Q)
        z.right = y = Extract-min(Q)
        z.freq = x.freq + y.freq
        Insert(Q,z)
    return Extract-min(Q)
