n, y = map(int, input().split())
result = False
for numA in range(n + 1):
    for numB in range(n + 1 - numA):
        numC = n - numA - numB
        if (10000 * numA + 5000 * numB + 1000 * numC == y) :
            print(str(numA) + ' ' + str(numB) + ' ' + str(numC))
            result = True
            break
    if (result) :
        break

if (result == False) :
     print('-1 -1 -1')