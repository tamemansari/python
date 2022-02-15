# diamond star pattern
z=1
for x in range(1,6):
	for s in range (x ,6):
		print('  ',end='')
	for y in range(1, x+1):
		print("%2d"%(z), ' ' , end='')
		z =z+1
	print()

for x in range(4,0,-1):
	for s in range (x ,6):
		print('  ',end='')
	for y in range(1, x+1):
		print("%2d"%(z), '   ' , end='')
		z =z+1
	print()