#Numerics - Observe that you dont need to specify the type of variable
a = 10
b = 21
c = a + b # result in 31

#Boolean values
is_True = True
otherwise = False

#String - Observe we can assign the same variable with different value
a = "Hello World"
b = a[0]
print(f'the first character of string in a is {b}')

#List
lst = [10, 20, 30, "Hello"]
print(lst)
lst.append(40) # one of the built in function to add into list
c = lst[1]
print(f'the second element of string in a is {c}')

#Dictornary
a = {11: 'Akhil', 12: 'Ron', 'test': 10}
print(f'Value corresponding to the the key 11 is {a[11]}')

#Set
a = set()
a.add(1)
a.add(1)
print(f'set of a {a}')

#Tuples - Ordered pair of elements
a = (1, "Hello")
print(f'The first element of a tuple is {a[0]}')