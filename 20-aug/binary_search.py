lst = [1,3,5,7,8,10,13,17,22,27,33]
target = 22
low = 1
high = len(lst)
while low<=high:
    mid = (low+high)//2
    if target == lst[mid]:
        print(mid)
        break
    elif target>lst[mid]:
        low = mid+1
    else:
        high = mid-1
