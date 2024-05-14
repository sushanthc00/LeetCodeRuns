# This python program tells if there exists a pair in array whose sum results in x.

def checkPair(A, size, value):
    for i in range(0, size):
        for j in range(0, size):
            if A[i] + A[j] == value:
                return 1
    return 0


def hashCheckPair(A, size, value):
    hashmap = {}

    for i in range(0, size):
        temp = value - A[i]
        if temp in hashmap:
            print("Yes")
            return
        hashmap[A[i]] = i
    print("No")


if __name__ == "__main__":
    A = [1, 2, -4, -2, 9, 0, -6, 3, 5]
    value = int(input("Enter the number for which you want to check the sum for: "))
    size = len(A)

    if checkPair(A, size, value):
        print("Yes")

    else:
        print("No")

    # hashCheckPair(A, size, value)
