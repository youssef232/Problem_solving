# 977. Squares of a Sorted Array
### brute force :
### square all the array then sort it by using merge sort. 
### O(nlg(n)) --> time complexity 
### after reading the question one more time i knew i missed that the array was <b><i>sorted</b></i> :(
### a better solution by using Two Pointers
### O(n) --> time complexity
### the idea is the biggest squared element is at the first element or the last element
### two pointer one at the beginning and one at the end, compare the <i><b> absolute</b> </i>
