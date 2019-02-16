def list_sort(list, list_len):
    l, r = 0, list_len - 1
    k = 0
    flag = True
    while flag:
        flag = False
        try:
            count = 0
            list = []
            for i in range(0, 5):
                number = int(round(float(input('Please enter a number: '))))
                list.append(number)
                print(list)
        except ValueError:
            print("Enter a Valid Input")
            flag = True
        while (l < r):
            while (list[l] % 2 != 0):
                l += 1
            while (list[r] % 2 == 0 and l < r):
                r -= 1

            if (l < r):
                list[l], list[r] = list[r], list[l]

        odd = list[:k]
        even = list[k:]

        odd.sort()
        even.sort()
        odd.extend(even)

    return odd
list_len = 6
kk = list_sort()
print("xhs", kk)