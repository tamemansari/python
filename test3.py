Name = input("Enter Name: ")
Hall_Ticket_no = int(input("Enter Hall Ticket num: "))
Std = int(input("Enter Class: "))
Result = "pass"
Total = 0
x = 1
while x<=10:
    m = int(input("Enter Marks: "))
    Total = Total+m
    print("Total is:",Total)
    avg = (Total/10)
    print("Avg is: ",avg)
    if m<40:
        print("Fail")
    x = x+1
else:
    print("Pass")


