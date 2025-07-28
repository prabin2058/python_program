students = {}

while True:
    print("\n===== Student Menu =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        if roll in students:
            print("Student with this roll number already exists.")
        else:
            students[roll] = name
            print("Student added successfully.")

    elif choice == '2':
        roll = input("Enter roll number to delete: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully.")
        else:
            print("No student found with this roll number.")

    elif choice == '3':
        if not students:
            print("No students found.")
        else:
            print("\n--- Student List ---")
            for roll, name in students.items():
                print(f"Roll No: {roll}, Name: {name}")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
