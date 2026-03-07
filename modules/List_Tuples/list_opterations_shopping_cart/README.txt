List Operations
Operation	Description
append(x)	Adds element to end of list
insert(i, x)	Inserts element at index i
extend(iterable)	Adds multiple elements
remove(x)	Removes first occurrence of value
pop()	Removes element by index (default last)
clear()	Removes all elements
index(x)	Returns index of element
count(x)	Counts occurrences
sort()	Sorts list
reverse()	Reverses order
copy()	Creates shallow copy
Shallow Copy vs Deep Copy
Shallow Copy

Copies only the outer list

Inner objects are shared references

Changes inside nested objects affect both lists

Example result:

Original Nested List: [[99, 2], [3, 4]]
Shallow Copy: [[99, 2], [3, 4]]
Deep Copy

Copies entire structure recursively

Inner objects are independent

Example result:

Deep Copy: [[1, 2], [3, 4]]