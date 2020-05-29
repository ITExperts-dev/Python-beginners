#itexpert127001@gmail.com

#A string is a series of characters, surrounded by single or double quotes.

# Make a 5-character string, and assign it to a name

S = 'Hello'
"""
print("String =",S)

#Length => len fn
print("Length =",len(S))

#Slicing
#The first item in S, indexing by zero-based position

value = S[0]

print("value at 0 Index = ",value)
print(S[0])

#The second item from the left
print("Second Index Element = %s" %S[1])


# The last item from the end in S
print("Last Element = %s" % S[-1])


# The second-to-last item from the end
print("second last Element = ",S[-2])


# Slice of S from offsets 1 through 2 (not 3)

# Hello

print("slicing S[1:3] = ",S[1:3])

print("slicing S[1:] = ",S[1:])

print("slicing S[0:3] = ",S[0:3])

print("slicing S[:3] = ",S[:3])


print("slicing S[:] = ",S[:]) 


"""


#Concatenation (combining strings)

first_name = 'hello'
last_name = 'python'

print("first_name = %s" %first_name)
print("last_name = %s " %last_name)

full_name = first_name+last_name
print("Before Space combining strings = ", full_name)

full_name = first_name + ' ' + last_name
print("After space combining strings = ",full_name)


# Immutable objects cannot be changed

obj = "python"

#obj[0] = 'P'

print(obj)

# But we can run expressions to make new object

#obj[1:] =  ython

# 'P' 

obj = 'P' + obj[1:] 
print(obj)