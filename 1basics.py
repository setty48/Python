#starting python

print("Hello!") # print statements

# 1. storing integer values into variables 
a =120  
b =3

print(a)
print(b)

# 2.simple mathmatical operations
a //= 2     # floor div(quotient) a = a/2 i.e a=60 divide a by 2 resulting 60 and store back into a
print(a)    # recent value stored in 'a' would be 60 but not 120 

b **= 3     # exponential - **, b= b^3 results 27(3^3) and stored back in b
print(b)    # recent value stored in 'b' would be 27 but not 3 

a %= 7      # remainder is stored in a variable using %, so a = a%7(a=60) is 7 
print(a)

z=(9-7)*2**3+10%6//-1*2-1 #order of operations 1.paranthesis() 2. exponential** 3. modulo %, div /, mul *, floor div // 4. add +, sub -
print(z)

# 3. storing strings into variables using ' ' or " "
city = "Seattle"
state = "Washington"
print("The seahawks are from %s, %s."%(city, state))

name = "Praveen"
occupation = input("what is your major?") #asks your input
print("So, you are %s, you live in %s, % state and majoring in %s."%(name, city, state, occupation))

# 4. slicing strings
s = name[:3]     #first 3 index values will be stored in 's'
e = name[2:5]    #values from index 2 to index 5 will be stored in 'e'
t = name[4:]     # values from index 4 are stored in 't'
print(s,e,t, x)

x = len(name)    # length of string stored in name is stored in 'x'
print(len ("Kumar"))


# 5. Escape sequence
print("My name is \"Praveen Kumar Kandregula\".") #escape sequence

#6. convert string into lower and upper case 
print("KANDREGULA".lower()) #output reults in all lower cases
print(name.upper())

#7. String concatination
print("R2"+"-"+"D2")        # string concatination
