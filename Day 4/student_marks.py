"""Day 4: Student Marks Management System.

A command-line application that manages student marks across multiple subjects
(Python, SQL, DSA), computes averages, and persists records to a JSON file.
"""

import json
import os

# Target the data file in the same directory as this script
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")

students = {}


def validate_mark(subject):
    """Prompt the user for a numeric mark between 0 and 100 with validation."""
    while True:
        try:
            mark = int(input(f"Enter the mark for {subject} (0-100):\n"))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")


def add_student():
    """Add a new student record with marks for Python, SQL, and DSA."""
    name = input("Enter the name of the student:\n").strip()

    if not name:
        print("Student name cannot be empty")
        return

    if name in students:
        print(f"Student {name} already exists!")
        return

    python_marks = validate_mark("Python")
    sql_marks = validate_mark("SQL")
    dsa_marks = validate_mark("DSA")

    students[name] = {
        "Python": python_marks,
        "SQL": sql_marks,
        "DSA": dsa_marks,
    }

    print(f"Student {name} marks added successfully")


def display_students():
    """Display all student records and their subject scores."""
    if not students:
        print("No students found")
        return

    print("------ Student Records ------")
    for name, marks in students.items():
        print(f"Student : {name}")
        for subject, score in marks.items():
            print(f"{subject} : {score}")
        print()


def search_student():
    """Search for a student by name and display their marks."""
    s_name = input("Enter student name to search: ").strip()

    if not students:
        print("No students found")
        return

    if s_name in students:
        print(f"Student: {s_name}")
        for subject, score in students[s_name].items():
            print(f"{subject}: {score}")
    else:
        print("Student not found")


def calculate_average():
    """Calculate and display the average marks for a specific student."""
    s_name = input("Enter the student name: ").strip()

    if not students:
        print("No students found")
        return

    if s_name not in students:
        print("Student not found")
        return

    marks = students[s_name]
    total = sum(marks.values())
    average = total / len(marks)

    print(f"{s_name}'s average marks: {average:.2f}")


def save_data():
    """Persist current student records to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=2)
        print("Data saved successfully")
    except OSError as e:
        print(f"Error saving file: {e}")


def load_data():
    """Load student records from the JSON file into memory."""
    try:
        if not os.path.exists(DATA_FILE):
            print("No existing data found starting fresh")
            return

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)

        if not isinstance(loaded_data, dict):
            print("Invalid data format in JSON file")
            return

        students.clear()
        students.update(loaded_data)

    except json.JSONDecodeError:
        print("File contains invalid json")
    except OSError as e:
        print(f"Error loading file: {e}")


def main():
    """Main CLI menu loop for Student Marks Manager."""
    load_data()

    while True:
        print("\n========== STUDENT MARKS MANAGER ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Calculate Average")
        print("5. Save Data")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice:\n "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            calculate_average()
        elif choice == 5:
            save_data()
        elif choice == 6:
            save_data()
            print("Exiting Student Marks Manager...")
            break
        else:
            print("Invalid choice. Select between 1 and 6.")


if __name__ == "__main__":
    main()