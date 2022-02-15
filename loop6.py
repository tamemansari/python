no = int(input("enter a num"))
sum = 0
for x in range (1 , no+1):
	print (x)
	sum = sum+x
print ("sum is:" sum)

sum =0 
for x in range (1 , no+1, 2):
	print (x)
	sum = sum+x
print ("sum is:" sum)

sum =0 
for x in range (1 , no+1, -2):
	print (x)
	sum = sum+x
print ("sum is:" sum)
