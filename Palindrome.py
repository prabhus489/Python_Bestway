def palindrome(my_str):
    if(my_str == my_str[::-1]):
        return True
    else:
        return False


my_str = raw_input("Enter a string to check wheather a string is palindrome or not  :")

print(palindrome(my_str))

##***********************************

##Program Steps:
##
##1. Take a string from the user and store it in a variable.
##2. Reverse the string using string slicing and compare it back to the original string.
##3. Print the final result
##4. Exit.
##
##************************************
##Test cases:
##
##case 1 :
##
##    I/P :
##Enter a string to check wheather a string is palindrome or not  : malayalam
##
##O/P:
##    True

