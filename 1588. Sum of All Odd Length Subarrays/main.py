def sumOddLengthSubarrays( arr: list[int]) -> int:
    output = 0
    for i in range(0 , len(arr)):
        j = i
        while j < len(arr):
            output += sum(arr[i: j + 1])
            j += 2
    return output


print(sumOddLengthSubarrays([10, 11, 12]))