def solution(A):
    A = set(A)
    ans = 1
    while ans in A:
        ans += 1
    return ans

A = [-1, -2, 0, 1, 2, 3, 7, 5, 6, 4]
solution(A)