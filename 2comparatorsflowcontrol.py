""" Page 2 basics """

# 1. comparators 
print(45<56 and 67>73)
print(23!=23 or 34<=45)
print(not 3==3)

# 2.flow controlif elif and else  statements
name = input("what is your name?")
length = len(name)
if length< 4:
    print("your name is too short")
elif length>=4 and length<=10:
    print("Your name is atleast 4 characters and less than 10 characters")
else:
    print("your name is too long to print")

# calling functions and their parameters
def cal():
    print("this is the function")
    
def intfun(a1):
    return a1 * 2

def two(int1, int2):
    return int1*int2

def Inside(a, b, c):     #calling functions by passing parameters inot it
    print(two(intfun(a), b) * c)

cal()
Inside(7, 4, 2)           #parameters passed into function 'Inside'
