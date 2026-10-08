'''a=[1,23,5,'avb']
s= 'abbbc 123'
set ={12,13,14,15}
print(1 in a)
print('123' in s)
print('abb' in s)
print(12 not in set)




l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2)
print(l1 is not l2)
print('*************')
print(id(l1))
print(id(l2))
print('*************')
s1='abc'
s2='abc'
print(s1 is s2)
print(id(s1))
print(id(s2))
print('*************')
x=10
print( 10 is x)
print(id(x))
print(id(10))
'''



'''
num=(int(input("user enter a string:")))
if (num>0):
     print("positive")
print("program excute")

 
num=(int(input("user enter a string:")))
if (num>0):
     print("positive num")
else:
    print("its a netural number")
print("program excute")

'''


"""

atm=(int(input("user enter a string:")))
if(atm>=5000):
     print("50% is discount")
elif(3000<=atm<5000):
     print("25% is discount")
elif(1000<=atm<3000):
     print("10% is discount")
else:
     print("draw agian")
print("thank you for ur withdraw")



# if

num=(int(input("user enter a num:")))
if num>0:print("positive")

# if-else

num=(int(input("user enter a num:")))
print("positve")if num>0 else print("netural or negative")
"""
'''
n=print(input("enter input:"))
#elif ladder
if n>0:
    print("positive number")
elif n<0:
    print("neative number")
else:
    print("its neutral number")
"""
# short-hand elif

print("positive number")if n>0 else  print("neative number")if n<0  else print("neutral numbr")
'''
"""
day_name=(input("enter a week day:")
print(" lord shiva")if day_name=='monday'else print("lord ganesha")if day_name=='tuesday'else print("lord parvati")if day_name=='wendnesday'else print ("free day")


n= int(input("enter a num:"))
for i in range(1,(n),1):
    print(i, end=" ") 
print("\nlast updated i: ", i)
"""

# for loop
'''
n= int(input("enter a num:"))
for i in range(n,(1-1),-2):
    print(i, end=" ") 
print("\nlast updated i: ", i)
'''
'''l1=[1,4,3]
for i in l1:
    print(i,end='|')
print("\n+++++++++")



l2="100"
for i in l2:
    print(i,end='|')
print("\n+++++++++")

l3=2000
for i in l3:
    print(i,end='|')
print("\n+++++++++")#error

for i in 1,2,3,45,9:
    print(i,end='|')
print("\n+++++++++")




print(i,end="|")
print("\n*******")
s1='abc'
for j in s1:
    print(j,end="|")
print("\n........")


#while loop
n=int(input("enter a num:"))
i=3
while i<=n:
    print(i,end=' ')
    i=i+1
print("\n last updtared i:",i)

n=int(input("enter a num:"))
i=8
while i<=n:
    print(i,end=' ')
    continous
    i=i+1
print("\n last updtared i:",i)



# even num

def isEvenodd(n):
    return n%2==0
count = int(input("enter a num:"))
series=1
print(f"the first {count}even num's are:")
while count>0:
    flag=isEvenodd(series)
    if flag:
        print(series,end=" ")
        count-=1
    series+=1

# odd num

def isEvenodd(n):
    return n%2==1
count = int(input("enter a num:"))
series=1
print(f"the first {count}odd num's are:")
while count>0:
    flag=isEvenodd(series)
    if flag:
        print(series,end=" ")
        count-=1
    series+=1

'''
'''
year=int(input("enter a year:"))
if((year % 100!=0 and year % 4==0)or(year % 400==0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



def isLeapYear(year):
    return (year%100!=0 and year % 4 ==0) or (year % 400 ==0)
year=int(input("enter a year:"))
flag = isLeapYear(year)
if flag:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
    
'''
"""
def isLeapYear(year):
    return (year%100!=0 and year % 4 ==0) or (year % 400 ==0)
start_year=int(input("enter start a year:"))
end_year=int(input("enter end a year:"))
if start_year>end_year:
    print("invalid input")
else:
    print("leap year's are:")
    for i in range(start_year,(end_year+1)):
        flag = isLeapYear(i)
        if flag:
            print(i,end=' ')


"""
# leap year and non leap year in same code as separate

"""
def isLeapYear(year):
    return (year%100!=0 and year % 4 ==0) or (year % 400 ==0)
start_year=int(input("enter start a year:"))
end_year=int(input("enter end a year:"))
if start_year>end_year:
    print("invalid input")
else:
    print("leap year's are:")
    for i in range(start_year,(end_year+1)):
        flag = isLeapYear(i)
        if flag:
            print(i,end=' ')
    print("\n non-leap year's are:")
    for i in range(start_year,(end_year+1)):
        flag = isLeapYear(i)
        if not flag:
            print(i,end=' ')

            
  """

# count digits
"""
a=int(input("enter a digit:"))
count=0
while a>0:
    a=a//10
    count=count+1
print(count)

# optimize code with fun

def CountDigits(a):
    count=0
    while a>0:
        a//=10  # a=a//10
        count+=1 # count=count+1
    return count
a=int(input("enter a digit:"))
res=CountDigits(a)
print(f"the count of digits in {a} is: {res}")
    
"""
"""
def CountDigits(a):
    count=0
    while a>0:
        a//=10  # a=a//10
        count+=1 # count=count+1
    return count
start_digit=int(input("enter a  start digit:"))
end_digit=int(input("enter a  end digit:"))
if start_digit>end_digit:
    print("invalid input")
else:
    for i in range(start_digit,(end_digit+1)):
        res = CountDigits(i)
        
    print(f"the count of digits in {a} is: {res}")
    """

"""

# Armstrong number

def coundigits(n):
    count =0
    while n>0:
        n=n//10
        count+=1
    return count

def isASN(n):
    temp =n
    if n<0:
        n=n*-1
    asn=0
    pow = coundigits(n)

    while n>0:
        base =n%10
        asn=asn+(base**pow)
        n=n//10

    if temp<0:
        asn=asn*-1
    return temp==asn

n=int(input("enter number:"))
flag =isASN(n)
if flag:
    print(f"{n} is an ASN")
else:
    print(f"{n} is not an ASN")


def coundigits(n):
    count =0
    while n>0:
        n=n//10
        count+=1
    return count

def isASN(n):
    temp =n
    if n<0:
        n=n*-1
    asn=0
    pow = coundigits(n)

    while n>0:
        base =n%10
        asn=asn+(base**pow)
        n=n//10

    if temp<0:
        asn=asn*-1
    return temp==asn

start=int(input("enter start digit:"))
end=int(input("enter end digit:"))
if start>end:
    print("invalid input")
else:
    print("the ASN are:")
    for i in range(start,(end+1)):
        flag =isASN(i)
        if flag:
            print(i, end=' ')
"""
#ASN and non ASN
"""
def coundigits(n):
    count =0
    while n>0:
        n=n//10 
        count+=1
    return count

def isASN(n):
    temp =n
    if n<0:
        n=n*-1
    asn=0
    pow = coundigits(n)

    while n>0:
        base =n%10
        asn=asn+(base**pow)
        n=n//10

    if temp<0:
        asn=asn*-1
    return temp==asn

start=int(input("enter start digit:"))
end=int(input("enter end digit:"))
if start>end:
    print("invalid input")
else:
    print("the ASN are:")
    for i in range(start,(end+1)):
        flag =isASN(i)
        if flag:
            print(i, end=' ')
    print("\nthe non  ASN are:")
    for i in range(start,(end+1)):
        flag = not isASN(i)
        if flag:
            print(i, end=' ')

"""
# first n ASN
'''
def coundigits(n):
    count =0
    while n>0:
        n=n//10 
        count+=1
    return count

def isASN(n):
    temp =n
    if n<0:
        n=n*-1
    asn=0
    pow = coundigits(n)

    while n>0:
        base =n%10
        asn=asn+(base**pow)
        n=n//10

    if temp<0:
        asn=asn*-1
    return temp==asn

count = int(input("enter a num:"))
series =1
while count>0:
    flag=isASN(series)
    if flag:
        print(series, end=" ")
        count-=1
    series +=1


# ASN ,non ASN COUNT all in one

def coundigits(n):
    count =0
    while n>0:
        n=n//10 
        count+=1
    return count

def isASN(n):
    temp =n
    if n<0:
        n=n*-1
    asn=0
    pow = coundigits(n)
    while n>0:
        base =n%10
        asn=asn+(base**pow)
        n=n//10

    if temp<0:
        asn=asn*-1
    return temp==asn
count = int(input("enter a num:"))
series =1

while count >0:
    flag = isASN(series)
    if flag:
        print(series, end=" ")
        count-=1
    series +=1
print("the ASN are: ")
for i in range(series,(series+1)):
    flag =isASN(i)
    if flag:
        print(i, end=' ')
        print("\nthe non  ASN are: ")
for i in range(series,(series+1)):
    flag = not isASN(i)
    if flag:
        print(i, end=' ')
'''

# reverse fun
'''
def reversenum(n):
    temp=n
    if n<0:
        n=n*-1
    reverse =0
    while n>0:
        reminder = n%10
        reverse = (reverse*10)+reminder
        n=n//10
    if temp <0:
        reverse = reverse*-1
    return reverse
n= int(input("enter a num:"))
res=reversenum(n)
print(f"the reverse number{n} is:{res}")
 '''    


# WAP to display the reversal of each indidual number present in a user defined range.
"""
def reversenumber(n):
    temp=n
    if n<0:
        n=n*-1
    reverse =0
    while n>0:
        reminder = n%10
        reverse = (reverse*10)+reminder
        n=n//10
    if temp <0:
        reverse = reverse*-1
    return reverse
start_num = int(input("enter  a start  num:"))
end_num = int(input("enter  a end   num:"))
if end_num>0:
    for i in range(start_num,(end_num+1)):
        flag = reversenumber(i)
        result=reversenumber(i)
        print(f"the reversal of {i} is:{result}")
"""


# palindrome for enter given number

'''
def palindrome(n):
    temp=n
    if n<0:
        n=n*-1
    rev = 0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp <0:
        rev = rev*-1
    return rev
num=int(input("enter a number:"))
res=palindrome(num)
falg=palindrome(num)
if num == falg :
    print( f"{num} the number is palindrome {res}")
else:
    print( f"{num} the number in not palindrome{res}")
    
'''
#  first n non integer palindrome
'''def countdigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
def palindrome(n):
    temp=n
    if n<0:
        n=n*-1
    rev = 0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp <0:
        rev = rev*-1
    return temp==rev
count=int(input("enter a number:"))
series=1
while count>0:
    flag= palindrome(series)
    if not flag:
        print(series, end=' ')
        count-=1
    series+=1
    '''
#  integer palindrome first n 
'''def countdigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
def palindrome(n):
    temp=n
    if n<0:
        n=n*-1
    rev = 0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp <0:
        rev = rev*-1
    return temp==rev
count=int(input("enter a number:"))
series=1
while count>0:
    flag= palindrome(series)
    if  flag:
        print(series, end=' ')
        count-=1
    series+=1'''
#WAP to display all the integer palindrome present in a user defined range of values.?
'''def palindrome(n):
    temp=n
    if n<0:
        n=n*-1
    rev = 0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp <0:
        rev = rev*-1
    return rev
start_num=int(input("enter a start number:"))
end_num=int(input("enter a end  number:"))
for i in range(start_num,(end_num+1)):
    res=palindrome(i)
    falg=palindrome(i)
    if i==falg :
        print( f"{i} the number is palindrome : {res}")
'''
# WAP to all the integer palindromes and non-integer palindrome present in a user defined range of values separately? 
'''
def palindrome(n):
    temp=n
    if n<0:
        n=n*-1
    rev = 0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp <0:
        rev = rev*-1
    return rev
start_num=int(input("enter a start number:"))
end_num=int(input("enter a end  number:"))
for i in range(start_num,(end_num+1)):
    res=palindrome(i)
    falg=palindrome(i)
    if i==falg :
        print( f"{i} the number is palindrome : {res}")
    else:
        print( f"{i} the number in not palindrome : {res}")

    '''




# WAP to display all the factors of a given number.
'''
def displayfactors(n):
    for i in range(1,(n+1)):
        if n% i==0:
            print(i,end=' ')
num=int(input("enter a num:"))
displayfactors(num)

'''


'''

#WAP to display all the factors of a given number?
def displayfactors(n):
    for i in range(1,(n+1)):
        if n% i==0:
            print(i,end=' ')
# wap to count the number of factors of a given number?
def countingFactors(n):
    countFact = 0
    for i in range(1,(n+1)):
        if n%i==0:
             countFact +=1
    return countFact
#wap to count the number of cycles thaken display all the factors of a given number?
def countingcycles(n):
    countcycles=0
    for i in range(1,(n+1)):
        countcycles+=1
        if n%i==0:
            continue
    return countcycles

def displayfactors1(n):
    i=i
    while i*i<=n:
        if n%i==0:
            print(i,end=' ')
            if (i!=(n//i)):
                print((n//i),end=' ')
        i+=1
def countingFactors(n):
    i=1
    countFact = 0
    while i *<=n:
        if n%i==0:
            print(i,end=' ')
            if (i!=(n//i)):
                countFact +=1
    return countFact        
        
num=int(input("enter a num:"))
displayfactors(num)
print("\n=========")
rescount=countingFactors(num)
print(f" the count of num  of {num} is : {rescount}")
print("\n========")
rescountcycles=countingcycles(num)
print(f" the count of num  ofcycles to get all the factors  is : {rescountcycles}")
print("=====")
displayfactors1(num)
print("cycles are:")

'''
'''
def displayfactors1(n):
    i=1
    while i*i<=n:
        if n%i==0:
            print(i,end=' ')
            if (i!=(n//i)):
                print((n//i),end=' ')
        i+=1
num=int(input("enter a num:"))
print("cycles are for: ",+num)
displayfactors1(num)

'''
'''
def countingFactors(n):
    i=1
    countFact = 0
    while i *i<=n:
        if n%i==0:
            print(i,end=' ')
            if (i!=(n//i)):
                countFact +=1
        i+=1
    return countFact      
num=int(input("enter a num:"))
print("counting factors are for: ",+num)
countingFactors(num)
'''


"""
def countingcycles(n):
    i=1
    countcycles=0
    while i *i<=n:
        if n%i==0:
            print(i,end=' ')
            if (i!=(n//i)):
                countcycles+=1
        i+=1
    return countcycles
num=int(input("enter a num:"))
print("count cycles are for: ",+num)
"""

'''
# wap to display the factors of each num present in a user defined range.
def displayfactors1(n):
    i=1
    while i*i<=n:
        if n%i==0:
            print(i,end=' ')
            if (i!=(n//i)):
                print((n//i),end=' ')
        i+=1
s_num=int(input("enter a st num:"))
e_num=int(input("enter a ed num:"))
if s_num>e_num:
    print("invalid ip")
else:
    for i in range(s_num,(e_num+1)):
        print(f"cycles are for:{i} is:", end=' ')
        displayfactors1(i)
 '''
'''
# prime number
def isprimnumber(n):
    i=1
    countfact = 0 
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (i!=(n//i)):
                countfact+=1
        i+=1
    return countfact == 2
num=int(input("enter a num:"))
flag=isprimnumber(num)
if flag :
    print( num, "is a prime number")
else:
    print( num, "is not a prime number")
    
'''
"""
# factorial number of first n natural num's
def factorialnum(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact
num=int(input( "enter a num: "))
a=factorialnum(num)
print(f"the factorial of {num} is :{a} ")
series=1
while num>0:
    flag = factorialnum(series)
    if flag :
        print(series, end = ' ')
        num-=1
    series+=1
"""
'''
# user defined range of factorila num's
def factorialnum(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact
s_n=int(input( "enter a start num: "))
e_n=int(input( "enter a end num: "))
if s_n>e_n:
    print("invalid ip")
else:
    for i in range(s_n,(e_n+1)):
        a=factorialnum(i)
        print(f"the factorial of {i} is :{a} ")
'''

'''
def factorialnum(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact
f=int(input( "enter a num: "))


#wap to display all the prime num's present in a user defined range both prime and non prime

"""
def isprimnumber(n):
    i=1
    countfact = 0 
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (i!=(n//i)):
                countfact+=1
        i+=1
    return countfact == 2
s_num=int(input("enter a start  num:"))
e_num=int(input("enter end a num:"))
if s_num>e_num:
    print("invalid input")
else:
    for i in range(s_num, (e_num+1)):
        flag=isprimnumber(i)
        if flag :
            print( i, "is a prime number")
        else:
            print( i, "is not a prime number")

"""

# prime number in user defined range
'''
'''
def isprimnumber(n):
    i=1
    countfact = 0 
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (i!=(n//i)):
                countfact+=1
        i+=1
    return countfact == 2
s_num=int(input("enter a start  num:"))
e_num=int(input("enter end a num:"))
if s_num>e_num:
    print("invalid input")
else:
    for i in range(s_num, (e_num+1)):
        flag=isprimnumber(i)
        if flag :
            print( i, "is a prime number")
'''

'''
# wap to print first n prime number

"""
def isprimnumber(n):
    i=1
    countfact = 0 
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (i!=(n//i)):
                countfact+=1
        i+=1
    return countfact == 2
num=int(input("enter a start  num:"))
print(f"first {num} prime numbers are:")
series=1
while num>0:
    flag = isprimnumber(series)
    if flag :
        print(series, end = ' ')
        num-=1
    series+=1

"""



# wap to print first n non prime number


def isprimnumber(n):
    i=1
    countfact = 0 
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (i!=(n//i)):
                countfact+=1
        i+=1
    return countfact == 2
num=int(input("enter a start  num:"))
print(f"first {num} prime numbers are:")
series=1
while num>0:
    flag = isprimnumber(series)
    if not flag :
        print(series, end = ' ')
        num-=1
    series+=1

'''
# gcd/hcf
'''
def findGCD(n1,n2):
    hcf=1
    lower=n1
    if n2<n1:
        lower=n2
    for i in range(2, (lower+1)):
        if n1%i==0 and n2%i==0 :
            hcf = i
    return hcf
num1= int(input("enter a 1st num: "))
num2= int(input("enter a 2nd num: ") )        
res=findGCD(num1,num2)
print(f"the gcd of {num1} and {num2} are : {res}")
'''

# co_prime numbers
'''
def check_co_prime(n1,n2):
    hcf=1
    lower=n1
    if n2<n1:
        lower=n2
    for i in range(2, (lower+1)):
        if n1%i==0 and n2%i==0 :
            hcf = i
    return hcf == 1
num1= int(input("enter a 1st num: "))
num2= int(input("enter a 2nd num: ") )
flag=check_co_prime(num1,num2)
if flag:
    print("the given num's are co-primes")
else:
    print("the given num's are not a co-prime num's")
'''

# fibonacci series
'''
def isfibonacci(pos):
    n1=0
    n2=1
    while pos>0:
        print(n1, end=' ')
        temp=n1+n2
        n1=n2
        n2=temp
        temp=n1
        pos-=1
pos=int(input("enter a position:"))
isfibonacci(pos)
'''
'''
def isfibonacci(pos):
    n1=0
    n2=1
    #decriment while
    
    while pos>0:
        print(n1, end=' ')
        temp=n1+n2
        n1=n2
        n2=temp
        temp=n1
        pos-=1
# increment while

    while i<= pos:
        print(n1, end=' ')
        temp=n1+n2
        n1=n2
        n2=temp
        temp=n1
        i+=1
# decriment for loop
    for i in range(pos ,0,-1):
        print(n1, end=' ')
        temp=n1+n2
        n1=n2
        n2=temp
        temp=n1
 #incriment loop     
    for i in range(1, pos+1):
         print(n1, end=' ')
         temp=n1+n2
         n1=n2
         n2=temp
         temp=n1
      

pos=int(input("enter a position:"))
isfibonacci(pos)

'''











