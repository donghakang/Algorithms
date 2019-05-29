class Email:
    def __init__(self,sender,subject):
        self.sender = sender
        self.subject = subject
    def __repr__(self):
        return "\n"+self.sender + ": " + self.subject


#Setup test cases
e1 = Email("Inigo Montoya","You killed my father. Prepare to die.")
e2 = Email("IRS", "THIS IS YOUR FINAL WARNING")
e3 = Email("Your Grandson", "Need Money for College")
e4 = Email("Prince of Nigeria", "Help transferring funds")
e5 = Email("Jackpot Lottery", "YOU'RE WINNER!")
e6 = Email("Super Antivirus Pro", "Virus Detected! Download Now!")
e7 = Email("Anonymous", "Forward this to 20 friends and you will get $$$")
e8 = Email("The Bank", "Please confirm your password")

e9 = Email("Ted", "HAHAHAHAHAHAHAHAHAHA")
e10 = Email("Tedd","mine!")
e11 = Email("Teddd","be")
e12 = Email("Tedddd","will")
e13 = Email("Teddddd","Vengeance")
e14 = Email("Tedddddd","day.")
e15 = Email("Teddddddd","this")
e16 = Email("Tedddddddd","for")
e17 = Email("Teddddddddd","waited")
e18 = Email("Tedddddddddd","I")
e19 = Email("Teddddddddddd","have")
e20 = Email("Tedddddddddddd","Long")

E = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i1 in range(0, n1):
        L.append( A[p + i1] )
    for i2 in range(0, n2):
        R.append(A[q + i2 +1])
    L.append(-1)
    R.append(-1)

    i1 = 0
    i2 = 0

    for j in range (p, r + 1):
        if R[i2] == -1:
            A[j] = L[i1]
            i1 = i1 + 1
        elif L[i1] == -1:
            A[j] = R[i2]
            i2 = i2 + 1
        elif len(R[i2].sender) < len(L[i1].sender):  #
            A[j] = L[i1]
            i1 = i1 + 1
        else:
            A[j] = R[i2]
            i2 = i2 + 1
    pass


#Takes in list of Emails A, and indices p and r
#Sorts the sublist A[p...r], in order of the length of each Email's
#sender, from longest name to shortest, using Merge Sortp
#Returns nothing
def merge_sort(A,p,r):
    q = int((r + p)/2)
    if p < r:
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    pass


merge_sort(E,0,len(E)-1)
print(E)
