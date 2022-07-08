def containsDuplicate(nums: list[int]) -> bool:
    mydict = {}
    for i in nums:
        if i not in mydict:
            mydict[i] = True
        else:
            return True
    return False


arr = [1,2,3,1]
print(containsDuplicate(arr))
