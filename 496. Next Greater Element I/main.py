def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    output = [-1] * len(nums1)
    mydict = {n: i for i, n in enumerate(nums1)}
    stack = []
    for i in nums2:
        while stack and i > stack[-1]:
            val = stack.pop()
            index = mydict[val]
            output[index] = i

        if i in mydict:
            stack.append(i)

    return output


print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
