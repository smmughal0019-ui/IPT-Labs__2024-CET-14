name=input("Enter student name:")
roll_no=input("Enter roll number:")

subject1=float(input("Enter marks in subject 1:"))
subject2=float(input("Enter marks in subject 2:"))
subject3=float(input("Enter marks in subject 3:"))

total_marks = subject1+subject2+subject3
average_marks=total_marks / 3

print("\n---Student Information---")
print("Name:",name)
print("Roll Number:",roll_no)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)