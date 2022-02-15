#right pascal triangle pattern
z =1 
for x in range(1,6):
    for y in range(1, x + 1):
        print(z, ' ', end="")
        z = z+1
    print()

for x in range(4 , 0 , -1):
    for y in range(1 , x+1):
        print(z ,' ', end="")
        z = z+1
    print()