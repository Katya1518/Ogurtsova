A = [1, 2, 3, 4, 5, 6, 7]
B = [0]
for i in range(len(A)):
    B[i] = A[i]
for i in range(len(B)):
    if B.count(B[i]) == 1:
        print (B[i])

