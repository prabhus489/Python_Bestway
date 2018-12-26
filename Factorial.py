def factorial(num):
    result = 1
    for i in range(num):
        result=result * (i+1)
    return result


user_input = input("Enter the number to find factorial: ")
factorial_of_user_input = factorial(user_input)

print(factorial_of_user_input)


##********************************************
##Programming logic:
##The factorial of a number is the product of all the integers from 1 to that number.
##factorial of n is n!
##5! = 5*4*3*2*1 =120
##Factorial is not defined for negative numbers
##And the factorial of zero is one, 0! = 1.

##********************************************
##Program Explaination:
##    
##1.defining functio for factorial
##2.declaring result variable as 1 in initial
##and this result variable will be used to store
##the output factorial value.
##3.By using for loop we are iterating num value(ie, user input as parameter)
##4. result =result *(i+1) (ie, iterating user input
##                          and multiplying by result variable
##                          and storing in result and for next iteration
##                          it will multiply by updated result variable with i upto n number)
##

##********************************************

##Test cases:
##    
##case 1:
##    I/P:
##        Enter the number to find factorial: 5
##    O/p:
##        120
##
##case 2:
##    I/P:
##        Enter the number to find factorial: 0
##    O/p:
##        1
##
##case 3:
##    I/P:
##        Enter the number to find factorial: 1
##    O/p:
##        1
##case 4:
##    I/P:
##        Enter the number to find factorial: 7
##    O/p:
##        5040
##********************************************
