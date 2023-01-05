a = int(input()) + 1
b = int(input()) + 1
c = int(input()) + 1
x = int(input())

count = 0
for numA in range(a):
    for numB in range(b):
        for numC in range(c):
            if (numA * 500) + (numB * 100) + (numC * 50) == x :
                count = count + 1
print(count)