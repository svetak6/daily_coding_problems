def isExist(l, k):
    seen = set()

    for num in l:
        if k - num in seen:
            return True
        seen.add(num)

    return False

def findNums(l, k):

    for num in l:
        diff = k - num
        if diff in l:
            return num, diff
    return 0,0

l = [10, 15, 3, 7]
k = 17

print(findNums(l, k))

