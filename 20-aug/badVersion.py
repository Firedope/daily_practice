def isBadVersion(n):
    if n>=4:
        return True
    else:
        return False

def firstBadVersion(n):
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if low == high:
            return low
        elif isBadVersion(mid)==False:
            low = mid + 1
        else:
            high = mid

print(firstBadVersion(5))