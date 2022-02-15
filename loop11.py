a = 0
b = 0
c = 1
for x in range(1,5):
	for s in range (x ,5):
		print('  ',end='')
	for y in range(1, x+1):
		a = b
		b = c
		c = a+b
		print("%2d"%(c), '   ' , end='')
	print('')

for x in range(4,0,-1):
	for s in range(x,5):
		print('  ',end='')
	for y in range(1, x+1):
		a = b
		b = c
		c = a+b
		print("%2d"%(c), '  ' , end='')
	print('')