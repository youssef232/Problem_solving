def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    arr = [0] * 1001
    output = []
    for i in nums1:
        arr[i] += 1


    for i in nums2:
        if arr[i] > 0:
            output.append(i)
            arr[i] -= 1

    return output


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))
