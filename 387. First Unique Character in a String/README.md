# 387. First Unique Character in a String

### a brute force solution is two for loop and check if this character appears again in the string
### O(n<sup>2</sup>)

### a much better solution using hash table :
### 1. loop through the array check if it in the hash table add one if it not, add it to the hash table.
### 2. loop again through the array and check if this char appeared once return its index 
### 3. at the end return -1 if no char appeared once