v1 = input('Your weight')
v2 = input('Your height')
v2 = int(v2) * int(v2)

v2 = int(v2) / 10000
v3 = float(v1) / float(v2)
print(v3)

if v3 < 17:
	print('you are drisch')
else 