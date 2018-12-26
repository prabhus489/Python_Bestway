
n = int(input("Enter the number of series to be printed:"))


def FibonacciNumbers(n):
    first=0
    second=1
    if (n < 0):
        print("Invalid Input")
    for i in range(n):
        print(first)
        temp=first
        first=second
        second=temp+second



FibonacciNumbers(n)


##PROGRAM EXPLAINATION:

##getting input from user
##initialising first value as 0 in variable
##initialising second value as 1 in another variable
##for loop is am using for iteration for series
##printing first values as it is
##storing first value in temp variable to use it for second sequence value
##Now assigning second variable value 1 for first variable
##Now assigning Second variable is equals to sum of temp value and second value


##Test case for fibonacci series can be: 

##1.When an zero is entered it should not return anything.
##2.When a negative integer is entered it should not accept the value and should return an error msg(Invalid Input).
##3.When a positive value is entered then it should return the output.

##Output:

##case 1:
##    Enter the number of series to be printed:5
##    o/p : 0 1 1 2 3
##
##case 2:
##    Enter the number of series to be printed:10
##o/p:
##    0
##    1
##    1
##    2
##    3
##    5
##    8
##    13
##    21
##    34
##
##case 3:
##    Enter the number of series to be printed:0
##o/p:
##
##case 4:
##    Enter the number of series to be printed:1
##o/p: 0
##
##case 4:
##    Enter the number of series to be printed: abcdef
##o/p: Traceback error message


    
    

