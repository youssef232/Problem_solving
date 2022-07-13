# 566. Reshape the Matrix

### first if m * n for the given the mat doesn't equal r * c return the mat
### my solution was to convert the incoming array into one dimension first,
### then two loop to form r * c and a pointer to loop in the one dimensional array.
### time complexity O(m * n + r * c)
### m * n = r * c 
### then O(2 r*c) --> O(r * c)
###space complexity O(r * c)