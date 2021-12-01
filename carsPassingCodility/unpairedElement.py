def solution(A):
    a = 0
    for i in range(0, len(A)):
        a = a ^ A[i]
    return a



A = [9,3,9,3,9,7,9]
solution(A)