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
