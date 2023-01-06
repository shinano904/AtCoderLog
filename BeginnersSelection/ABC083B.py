n, a, b = map(int, input().split())

result = 0
sum = 0
for num in range(n + 1) :
    result = 0
    for num2 in list(str(num)):
        result = result + int(num2)
    if (a <= result) and (result <= b) :
        sum = sum + num

print(sum)