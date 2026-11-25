# Python Backend Placement Preparation

Welcome to the **Placement Preparation** repository. This repository documents a structured, hands-on learning roadmap focused on mastering Python programming, core computer science concepts, and practical backend software development tools essential for technical interviews and software engineering roles.

---

## 📁 Repository Structure

```text
Placement_prep/
│
├── .gitignore
├── README.md
│
├── Day 1/
│   ├── calculator.py
│   ├── complexity_notes.md
│   └── README.md
│
├── Day 2/
│   ├── word_frequency.py
│   ├── sample.txt
│   └── README.md
│
├── Day 4/
│   ├── student_marks.py
│   ├── students.json
│   └── README.md
│
└── Day 5/
    ├── expense_tracker.py
    ├── expenses.csv
    └── README.md
```

---

## 🚀 Projects & Learning Roadmap

| Day | Project / Module | Key Technical Concepts | Artifacts & Tools | Details |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | **CLI Calculator & Complexity Notes** | Input parsing, arithmetic logic, defensive exceptions (`ValueError`, `ZeroDivisionError`), Big-O analysis | [`calculator.py`](Day%201/calculator.py), [`complexity_notes.md`](Day%201/complexity_notes.md) | [Day 1 README](Day%201/README.md) |
| **Day 2** | **Word Frequency Counter** | File I/O, string normalization, punctuation stripping, dictionary hash counting, lambda sorting | [`word_frequency.py`](Day%202/word_frequency.py), [`sample.txt`](Day%202/sample.txt) | [Day 2 README](Day%202/README.md) |
| **Day 4** | **Student Marks Manager** | JSON serialization (`json.dump`/`load`), nested data models, score validation (0–100), GPA calculation | [`student_marks.py`](Day%204/student_marks.py), [`students.json`](Day%204/students.json) | [Day 4 README](Day%204/README.md) |
| **Day 5** | **Expense Tracker** | CSV persistence (`DictReader`/`DictWriter`), tabular list-of-dicts, financial totals, input sanitization | [`expense_tracker.py`](Day%205/expense_tracker.py), [`expenses.csv`](Day%205/expenses.csv) | [Day 5 README](Day%205/README.md) |

---

## 🛠️ Quick-Start & Execution Guide

All tools are built using the **Python Standard Library** and require **no external third-party dependencies**.

### Prerequisites
- Python 3.8 or higher installed on your system.
- Verify installation:
  ```bash
  python --version
  ```

### Running Each Project

Each script is configured with dynamic path resolution, enabling execution either directly from the repository root or within the corresponding subfolder.

#### 1. Day 1: Calculator
```bash
# Run from repository root
python "Day 1/calculator.py"

# Or navigate to folder
cd "Day 1"
python calculator.py
```

#### 2. Day 2: Word Frequency Counter
```bash
# Analyze default sample.txt from root
python "Day 2/word_frequency.py"

# Or provide a custom text file
python "Day 2/word_frequency.py" path/to/your/file.txt
```

#### 3. Day 4: Student Marks Manager
```bash
# Run interactive CLI with JSON persistence
python "Day 4/student_marks.py"
```

#### 4. Day 5: Expense Tracker
```bash
# Run interactive CLI with CSV persistence
python "Day 5/expense_tracker.py"
```

---

## 📊 Sample Data Files

To facilitate immediate local testing and evaluation, sample data files are retained within the repository:
- **`Day 2/sample.txt`**: Sample prose discussing Python backend development for testing word counting and sorting.
- **`Day 4/students.json`**: Pre-seeded student records across Python, SQL, and DSA to demonstrate display, search, and average calculation features out-of-the-box.
- **`Day 5/expenses.csv`**: Pre-seeded expense records across categories (Dining, Transportation, Education, Utilities) to verify loading and total expenditure calculation.

---

## 🧩 Engineering Standards

1. **PEP 8 Compliance**: Clean indentation (4 spaces), descriptive naming conventions, and modular function structure.
2. **Defensive Programming**: Robust exception handling around user inputs, division operations, and file I/O operations.
3. **Cross-Platform Compatibility**: File paths are dynamically resolved using `os.path.abspath(__file__)` to ensure identical behavior on Windows, macOS, and Linux.
4. **Comprehensive Documentation**: Every day module contains dedicated documentation detailing features, concepts, requirements, and execution examples.
