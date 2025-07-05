# Python List
thelist = ["one", "two", "three", "four", "five"]
print("The list is:", thelist)

#List functions
print("The first element is:", thelist[0])
print("The last element is:", thelist[-1])
print("The first two elements are:", thelist[0:2])  

#List methods
thelist.append("six")
print("After appending 'six':", thelist)
thelist.remove("three") 
print("After removing 'three':", thelist)
thelist.insert(2, "two and a half")
print("After inserting 'two and a half' at index 2:", thelist)
thelist.sort()  
print("After sorting the list:", thelist)
thelist.reverse()       
print("After reversing the list:", thelist)
thelist.insert(0, "one")
print("After inserting 'one' at the beginning:", thelist)
thelist.insert(0,"one")
print("After inserting 'one' again at the beginning:", thelist)
#Duplicate are allowed in list
thelist.pop()
print("After popping the last element:", thelist)

#List comprehension


squares = [x**2 for x in range(10)]
print("List comprehension for squares of numbers 0-9:", squares)
cubes = [x**3 for x in range(10)]
print("List comprehension for cubes of numbers 0-9:", cubes)
# List comprehension with condition
evens = [x for x in range(20) if x % 2 == 0]
print("List comprehension for even numbers 0-19:", evens)
# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print("Nested list comprehension for a 3x3 matrix:", matrix)