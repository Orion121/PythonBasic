# 2. Student Grades
# Create a dictionary where the keys are student names and the values are their grades.
# Allow the user to:
# - Add a new student and grade.
# - Update an existing student’s grade.
# - Print all student grades.
# Used dictionary and basic operations. Using if else:

students = {}

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update student grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added with grade {grade}.")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print(f"{name} not found in the list.")
    elif choice == "3":
        print("Student Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
