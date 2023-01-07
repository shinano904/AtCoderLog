n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

alice = 0
bob = 0

for index, num in enumerate(a):
    if index % 2 == 0:
        alice = alice + num
    else :
        bob = bob + num

print(alice - bob)