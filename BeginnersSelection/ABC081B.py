def isEven(list):
    result = True
    for num in list:
        if int(num) % 2 != 0:
            result = False
            break
    return result

num = input()
numlist = input().split()

count = 0
list = []
while True:
    if isEven(numlist) == True:
        list = numlist
        numlist = []
        for num in list:
            numlist.append(int(num) / 2)
        count += 1
    else:
        break

print(count)