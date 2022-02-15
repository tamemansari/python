name = input("Enter student name: ")
RollNO = input("Enter student Rollno:")
Standard = input("Enter class:")
Laws = int(input("Enter Laws marks: "))
Correspondance = int(input("Enter Correspondance marks"))
Mathmatics = int(input("Enter Mathmatics marks"))
Reasoning = int(input("Enter Reasoning marks"))
total_marks = Laws + Correspondance + Mathmatics + Reasoning
print ("Total Optained Marks is: " , total_marks)
percentage = (total_marks/4)
print ("your percentage is: %.2f" %(percentage))
if Laws<40 or Correspondance<40 or Mathmatics<40 or Reasoning<40:
	print("Result: Fail")
else:
	print("Result: pass")
	if percentage<50:
		print ("Beter luck next time")
	else:
		print("your Qualified")