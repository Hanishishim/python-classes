# def add(*arg):
#     sum = 0
#     for x in arg:
#         sum = sum + x
#     print(sum)
# add(31,24,432)

# def sqrofnum(*arg):
#     sqr = 0
#     for x in arg:
#         sqr = x ** 2
#     print(sqr)
# sqrofnum(4)

# def f(**arg):
#     print(arg)

def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact * 1
    return fact
def square(n):
    return n*n
x = lambda n:n*n
print(x(5))

def cube(n):
    return n*n*n
x = lambda n: n*n
print(x(5))

def add(x,y,z):
    return x+y+z
x = lambda x,y,z:x,y,
print(y(1,2,3))

def OddOrEven(n):
    rem = n % 2
    if rem == 0:
        return "even"
    else:
        return "odd"
x = lambda n: "even" if n%2 == 0 else "odd"

def divORnot(n):
    div = n % 5 
    div2 = n % 3
    if div == 0:
        print("divisible by 5")
    elif div2 == 0:
        print("divisible by 3")
    else:
        print("Not divisible by 3 or 5!")
x = lambda n:"Divsible by 3 or 5" if n%3 == 0 or n%5 == 0 else "Not divisible by 3 or 5!"

listOFStudents = ["HANISH", "Daksh", "Riyansh", "Devarsh"]
x = lambda marks: "pass" if marks >=70 else "fail"
