s = [input() for i in range(3)]

i2 = s[1].split(' ')
val = int(s[0]) + int(i2[0]) + int(i2[1])

print(str(val) + ' ' + s[2])