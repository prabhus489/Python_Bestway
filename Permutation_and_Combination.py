num1 = 0
num2 = 0
factor_num1 = 0
factor_num2 = 0
fact = 0
flag = 1
while flag:
    flag = 0
    try:
        num1 = int(input("Enter the Number: "))
        num2 = int(input("Enter the Number: "))
        if num1 <= 0:
            print("Number cannot be Zero")
            flag = 1
        elif num2 <=0:
            for x in range(1, num1 + 1):
                factor_num1 = factor_num1 * x
            print("The Permutation of num1 is", factor_num1)
            flag = 1
    except ValueError:
        print("Enter Valid Input")
        flag = 1
    if num1 > 0 and num2 > 0:
        for x in range(1, num1 + 1):
            factor_num1 = factor_num1 * x
            num = num1 - num2
            for x in range(1, num + 1):
                factor_num2 = factor_num2 * x
        fact = factor_num1 / factor_num2
    print("The permutation is", fact)
