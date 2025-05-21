# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 76
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks
# Step 4: Handle the case where the student is not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"No records found for student '{student_name}'.")
