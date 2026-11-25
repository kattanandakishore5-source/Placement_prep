# Day 4: Student Marks Management System

## Project Description
A command-line student management application designed to track and manage student academic performance across subjects (Python, SQL, DSA). It provides full CRUD-style capabilities, defensive input validation (enforcing mark ranges of 0–100), dynamic grade point/average calculation, and automated persistence using JSON files.

---

## Features
- **Add Student**: Registers student names and records marks for Python, SQL, and DSA with range checking ($0 \le \text{mark} \le 100$).
- **Display Records**: Iterates over all enrolled students and cleanly displays their subject scores.
- **Search Student**: Quickly queries a specific student by name with instant lookup.
- **Calculate Average**: Computes aggregate score and floating-point average for any student.
- **JSON Persistence**: Automatically loads data from and saves records to `students.json`, retaining state between sessions.
- **Automatic Save on Exit**: Ensures unsaved additions or edits are preserved before shutting down.

---

## Python Concepts Demonstrated
- **JSON Serialization**: Using Python's built-in `json` module (`json.dump` with indentation and `json.load`).
- **Nested Dictionaries**: Hierarchical data modeling (`dict[str, dict[str, int]]`).
- **Defensive Input Validation**: Looping with `try-except ValueError` blocks and numerical boundary checking.
- **CLI Flow Control**: Infinite interactive loop with exit conditions and choice routing.
- **File System Handling**: `os.path.exists` check and absolute path resolution relative to `__file__`.

---

## Requirements
- Python 3.8 or higher.
- Standard Library only (`json`, `os` — no external packages required).

---

## How to Execute the Program

### From the Repository Root
```bash
python "Day 4/student_marks.py"
```

### From the `Day 4` Directory
```bash
cd "Day 4"
python student_marks.py
```

---

## Example Usage

### 1. View Records (Option 2)
```text
========== STUDENT MARKS MANAGER ==========
1. Add Student
2. Display All Students
3. Search Student
4. Calculate Average
5. Save Data
6. Exit
Enter your choice: 2

------ Student Records ------
Student : Nanda
Python : 95
SQL : 92
DSA : 98

Student : Aarav
Python : 88
SQL : 84
DSA : 90
```

### 2. Calculate Average (Option 4)
```text
Enter your choice: 4
Enter the student name: Nanda
Nanda's average marks: 95.00
```

### 3. Add a Student (Option 1)
```text
Enter your choice: 1
Enter the name of the student:
Kishore
Enter the mark for Python (0-100):
90
Enter the mark for SQL (0-100):
85
Enter the mark for DSA (0-100):
92
Student Kishore marks added successfully
```
