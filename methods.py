#Different methods used in python
l = [0, 5, 3, 6, 4, 3, 1, 2, 90]
m = ['a','b','z','e']

l.remove(0)
print("removes the first occurance of the value:\n",l)

l.append(7)
print("7 is appended at end of list l:\n", l)

print(l.count(3)) #Counts no. of occurances of value

print(l.index(90)) # shows us the index value of 90 in the list

l.insert(1,3)
print("value 3 is inserted at index 1 in list l:",l)

l.pop()
print("value at end of the list is poped out \n",l)

l.pop(8)
print("number at index 8 of the list is poped out \n",l)

l.sort()
print("Sorted out in ascending order\n",l)

m.sort()
print("Sorted out in ascending order\n",m)

l.extend(m)
print("list m is added to l at the end and the result is:\n",l)

l.reverse()
print("revreses the entire list: \n",l)
