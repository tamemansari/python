Name = input("Enter Name: ")
Hall_Ticket_no = int(input("Enter Hall Ticket num: "))
Std = int(input("Enter Class: "))
Total = 0
x = 1
while x<=10:
    m = int(input("Enter Marks: "))
    Total = Total+m
    if m<40:
        print("Fail")
    x = x+1
else:
    print("Total is:",Total)
    print("Avg is: ",avg)
    if m>40 and avg>50:
        print("Pass")
    else:
        print("Fail")

