def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
print(lcm(a, b))


#*******************************************
##PROGRAM STEPS:
##1.Take in both the integers and store it in separate variables.
##2.Find which of the integer among the two is smaller and store it in a separate variable.
##3.Use a while loop whose condition is always True until break is used.
##4.Use an if statement to check if both the numbers are divisible by the minimum number and increment otherwise.
##5.Print the final LCM.
##6.Exit.
#*******************************************
##TEST CASES:
##
##Case 1:
##I/P:
##Enter the number 1 : 4
##Enter the number 2 : 6
##
##O/P:
##12
##
##Case 2:
##I/P:
##Enter the number 1 : 4
##Enter the number 2 : 8
##
##O/P:
##8
##
##Case 3:
##I/P:
##Enter the number 1 : 15
##Enter the number 2 : 17
##
##O/P:
##255
##
##Case 4:
##I/P:
##
##Enter the number 1 : 0
##Enter the number 2 : 0
##
##O/P: Trace back most recent call error
##     if((z % x == 0) and (z % y == 0)):
##ZeroDivisionError: integer division or modulo by zero
##
##Case 5:
##I/P:
##
##Enter the number 1 : 0
##Enter the number 2 : 1
##
##O/P: Trace back most recent call error
##     if((z % x == 0) and (z % y == 0)):
##ZeroDivisionError: integer division or modulo by zero




