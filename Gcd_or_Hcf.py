#method to compute gcd ( recursion )
#Native methiod to find GCD or HCF
#Eludes method to find GCD or HCF

def ComputeGCD(a,b):
    if b==0:
        return a
    else:
        return ComputeGCD(b,a%b)


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print(ComputeGCD(num1,num2))


#******************************************

##Logic For GCD:

##Elude's or Eludeion's rule to calculate GCD:

##a = b*x + (a%b)
##64 = 48 * x + reminder  
##64 = 48*1 + 16          --- a = b*x + (a%b)
##48=16*x + reminder      --- a=b, b = a%b
##48={~16~} *3 + 0        ---when  b = a%b = 0                 
##48=48                   ---then the diviser is Greatest common deviser
##Therefore 16 is GCD Here

#******************************************

##Test cases:

##Case 1:
##I/p:
##Enter first number: 48
##Enter second number: 64
##O/p:
##    16
##
##Case 2:
##I/p:
##Enter first number: 250
##Enter second number: 30
##O/p:
##    10
##
##Case 3:
##I/p:
##Enter first number: 12
##Enter second number: 14
##O/p:
##    2
##
##Case 4:
##I/p:
##Enter first number: 21
##Enter second number: 17
##O/p:
##    1


#******************************************

