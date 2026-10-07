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


# function in python

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