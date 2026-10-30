# text= input("enter a text:")
# y=int(input("enter a number for reating text:"))
# for i in range(y):
#     print(text)

#while loop
# i=0
# while i<=7:
#     print(i)
#     i+=1

# password = ""
# while password != "123":
#     password = input("Enter password: ")
# print("Access granted!")


# i = 1
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# i= 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue  # Skip when i is 3
#     print(i)

# count = 5
# while count > 0:
#     print(count)
#     count -= 1
# print("Time's up!")


# function in python function user defined function
'''
def fun():
    print("function as here")
fun()# calling the function

#types of function
#1. function without parameter and without return type
def fun1():
    print("This is a function without parameter and without return type")
fun1()

#2. function with parameter and without return type
def fun2(name):
    print(f"hello, {name}!")# hello, Athmeeya!
fun2("Athmeeya")

#3. function without parameter and with return type
def fun3():
    return "This is a function without parameter and with return type"
result = fun3()
print(result) # This is a function without parameter and with return type

#4. function with parameter and with return type
def fun4(x, y):
    return x + y
sum_result = fun4(5, 3)
print(sum_result) #8
'''
# examples of function 
'''def operation(a, b, c):
    
    return a+b*c
a=operation(10, 20, 30) #610
print(a)

def operation1():
    a=10
    b=20
    c=30
    return a+b*c
a=operation1() #610
print(a)

# deafult and keyword argument
def demo(a=1, b=2,c=3):
    print(a)
    print(b)
    print(c)
x=10
y=20
z=23
demo(x,y,z)
demo() # default values will be used

# actual and formal parameter in function
# Here, a and b are formal parameters. x and y are actual parameters.
def fun(a=1, b=2):
    temp = a
    a = b
    b = temp
    return a, b

x = 10
y = 20
print("Before swap:", x, y)

k= fun(x, y)
print("After swap:", k[0], k[1])


#nested function example 1
def large_fun():
    print("This is the outer function.")
    def small_fun(a,b):
        print("This is the inner function.")
        c= a / b
        print(c)
    small_fun(100,10)
large_fun() 

# example2
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 5
output = outer_function(3)
print(output)  # Output: 11


# global variable, a variable that is defined outside of any function and can be accessed and modified from any part of the code, including inside functions. In Python, you can declare a variable as global using the global keyword.
global_variable = 20
def my_function():
    global global_variable
    a= 10
    b=20
    global_variable = 200
    print(a+b )
    print(global_variable)  
my_function()
print(global_variable)  

#exapmle 2
x=1
def fun1():
    global x
    x = 10  # Declare x as a global variable
    print("Inside fun1, x =", x)
    def fun2():
        global x
        x = 20  # Declare x as a global variable
        print("Inside fun2, x =", x)
    fun2()
fun1()
print("Outside functions, x =", x)  # Output: 20

#nonlocal variable, a variable that is defined in an enclosing function and can be accessed and modified from inner functions. In Python, you can declare a variable as nonlocal using the nonlocal keyword.
#c=355
def funs():
    #global c
    a=100
    b=200
   # print("global",c)
    print("outer-fun",a+b)
    def funs1():
       # global c
        nonlocal a
        nonlocal b
        a= 10 # local variable
        b=20
        print("inner-fun",a+b)
    funs1()
funs()

#global, local, nonlocal, static variable, class variable, instance variable, constant variable
c=222
def funs():
    global c
    a=100
    b=200
    print("global",c)
    print("outer-fun",a+b)
    def funs1():
        global c
        nonlocal a
        nonlocal b
        a= 10 # local variable
        b=20
        print("inner-fun",a+b)
        print("local",a,b)
    funs1()
funs()
class Demo:
    static_variable = 100  # Static variable (under a class and shared among all instances)
    
    def __init__(self,ab, cb):
        self.instance_variable = ab  # Instance variable
        self.instance_variable1 = cb
    def display(self):
        print("Static Variable:", Demo.static_variable)
        print("Instance Variable:", self.instance_variable)
d1 = Demo(111, 222)
d1.display()
print("Accessing static variable directly:", Demo.static_variable)
print(d1.instance_variable)
print(d1.instance_variable1)
print(c)
#print(a)#name error
#print(b)#name error 
'''
# types of fun: lambda function
'''
variable = lambda a,b : a/b
print(variable(10,20)) 
'''

# higher order function : filter , map function
#filter function by using
'''
def even(num):
    if num%2==0 :
        return True
    else:
        return False
L=[]
i=0
while (i<=4):
    data=int(input("enter a number"))
    L.insert(i,data)
    i=i+1
print(L)
K=list(filter(even, L))
print("the even num are:",K)

 # by using lambda fun with in filter fun   
L=[]
i=0
while (i<=4):
    data=int(input("enter a number"))
    L.insert(i,data)
    i=i+1
print(L)
K=list(filter(lambda num:num%2!=0, L))
print("the odd num are:",K)'''

# map function by using fun
'''
def operation(n):
    return n+10
L=[]
i=0
while (i<=4):
    data=int(input("enter a number"))
    L.insert(i,data)
    i=i+1
print(L)
K=list(map(operation, L))
print("the updated num are:",K)'''

# lambda fun with in map fun
'''
L=[]
i=0
while (i<=4):
    data=int(input("enter a number"))
    L.insert(i,data)
    i=i+1
print(L)
K=list(map(lambda n : n+10 , L))
print("the updated num are:",K)

# types of fun : built-in fun
from math import pi
#pi=3
def fun1():
    #pi=1
    #print(pi)
    print("hlo")
    def fun2():
        #pi=2
        print(pi)
        print("hi")
    fun2()
fun1()
'''
#modules in a python : function
'''
def fun1():
    print("the modules in python")
def fun2():
        a=1
        b=4
        print(a+b)
def fun3(v,n):
    return v*n
    '''
    
''' closure in python'''

# def outer():
#     print("entering outer fun")
    
#     def inner():
#         print("entering inner fun")
#         # print("outside of inner")
#     return inner
# print("outside of inner")
    
# result=outer()
# print(result)
# result()

# def outer():
#     a=10
#     b=10
    
#     def inner():
#         print("addition")
#         sum=a+b
#         print(sum)   
#     return inner
# res=outer()
# print( res.__closure__)
# print('a is',res.__closure__[0].cell_contents)
# print('b is',res.__closure__[1].cell_contents)
# res()
    
'''decorator'''
'''def outer(func):
    print("the decorator function")
    def inner():
        res = func()
        print("Original message:", res)
        ref = res[::-1]
        print("Reversed message:", ref)
        print("exit inner fun")
        print(ref)
    return inner

@outer
def msg_print():
    msg = 'hlo world'
    print(msg)
    return msg
msg_print()

'''
'''class Demo:
    def __init__(self):
        self.__A=''
       
    def setter(self,name):
        self.__A=name
      
    def getter(self):
        return  self.__A
D1=Demo()
# a=D1.setter('krishna')
# print(a)
# b=D1.getter()
# print(b)
D1.setter('krishna')
print(D1.getter())
'''

# by passing parameter in encapsulation'''
'''class Book:
    def __init__(self,value):
        self.__pages=value
    def setter1(self,value):
        if value>0:
            self.__pages=value
    def getter1(self):
         return self.__pages
b=Book(100)
b1=b.getter1()
print(b1)
b.setter1(200)
print(b.getter1())
b.setter1(-200)
print(b.getter1())'''
# property method
class Book:
    def __init__(self):
        self.__pages1=''
        self.__pages2=''
    def setter1(self,value):
        self.__pages1=value
    def getter1(self):
         return self.__pages1
    setget=property(getter1,setter1)
    def setter2(self,value):
            self.__pages2=value
    def getter2(self):
             return self.__pages2
    getset=property(getter2,setter2)
b=Book()
b.setget= 100
res=b.setget
print('pages1=',res)
b.getset= 200
res1=b.getset
print('pages2=',res1)
    