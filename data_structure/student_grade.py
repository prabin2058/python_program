student_data = []
for i in range(3):
    subject = input("Enter name of subject: ")
    marks = int(input("Enter marks: "))
    student_data.append((subject, marks))
    
total_marks = sum(marks for subject, marks in student_data)
avg = total_marks / len(student_data)
print(avg)   