def removeDuplicate2(nums):
    if len(nums)<=3:
        return len(nums)
    i=2
    for j in range(2,len(nums)):
        if nums[j]!=nums[i-2]:
            nums[i]=nums[j]
            i+=1
    print(nums)
    return i

removeDuplicate2([0,0,1])