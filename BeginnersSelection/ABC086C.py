n = int(input())
result = True
t1 = 0
tx = 0
ty = 0


for i in range(n):
    if abs(x - tx) + abs(y -ty) > (t-t1) :
        result = False
    elif (abs(x - tx) + abs(y -ty)) % 2 != (t-t1) % 2 :
        result = False

    t1 = t
    tx = x
    ty = y

if result:
    print('Yes')
else:
    print('No')