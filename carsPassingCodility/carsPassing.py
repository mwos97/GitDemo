def solution(A):
    sE = 0
    s = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            sE += 1
        elif A[i] == 1:
            s += sE
    if  s > 1000000000:
        return -1
    else:
        return s


A = [0, 1, 0, 1, 1]
solution(A)
print(A)
print("new commit")


print("new")
print("test for develop branch")
print("test for develop branch1")
print("test for develop branch2")
print("test for develop branch3")
print("test for develop branch4")


def new_test():
    pass

def new_test2():
    pass

