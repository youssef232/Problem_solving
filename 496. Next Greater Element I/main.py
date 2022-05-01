def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    output_list = []
    myDict = dict()
    for i in range(len(nums1)):
        myDict[nums1[i]] = i

    for j in nums2:
