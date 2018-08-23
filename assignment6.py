#Q.1)Create a function to calculate the area of a sphere by taking radius from user.
r = int(input("Enter radius of sphere: "))
pi = 3.14
def area(r):
    a = 4*pi*r*r
    return a
print("Area of sphere is: ",area(r))

#Q.2)Write a function “perfect()” that determines if parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
#  sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect():
    for x in range(1,1001):
        a=1
        sum=0
        while a<=int(x/2):
            if(x%a==0):
                sum+=a
            a+=1
        if(sum==x):
            print(x)
perfect()

#Q.3)Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
n = int(input("Enter the number: "))
def multiplication_table(n):
    for i in range(1, 11):
        m = n * i
        print("{}*{} = {}".format(n,i,m))
print("Multiplication table of {} is: ".format(n))
multiplication_table(n)

 #Q.4)Write a function to calculate power of a number raised to other ( a^b ) using recursion
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
def power(base,exp):
    if(exp==0):
        return 1
    if(exp>0):
        return(base*power(base,exp-1))
print("Result:",power(base,exp))


