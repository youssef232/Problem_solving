# 350. Intersection of Two Arrays II

### brute force solution is to two for loops and check every element in one array into the other 
### array but be careful not to take one element more than one time


### because of the constraints in this problem 
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
### i decided to make an array with length 1001 (arr) and loop through one array 
### and increase the index in arr. then loop through the other array and check if arr[i] > 0

### Time complexity O(m + n) 
### where m ----> array1.length , n ------> array2.length
### space complexity(1001)
