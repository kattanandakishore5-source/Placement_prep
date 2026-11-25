# Day 2: Word Frequency Counter

## Project Description
A Python tool that analyzes text files to determine word occurrences and display the most frequent terms. It reads text data, strips out punctuation symbols, converts characters to uniform lowercase, counts word occurrences using a dictionary, and outputs the top 10 most frequent words sorted in descending order.

---

## Features
- **Punctuation Stripping**: Cleans commas, periods, quotes, and punctuation using `str.maketrans` and `string.punctuation`.
- **Case Normalization**: Converts all text to lowercase to prevent duplicate counts (e.g., "Python" and "python" are counted together).
- **Frequency Mapping**: Computes accurate term counts using Python dictionary hashing.
- **Top-N Ranking**: Sorts terms by count descending using a lambda comparator and extracts the top 10 results.
- **Flexible Path Resolution**: Runs smoothly both from the repository root and from the `Day 2` directory, with optional custom file path argument support.

---

## Python Concepts Demonstrated
- **File Handling**: Safe file streaming using the context manager `with open(..., "r", encoding="utf-8")`.
- **String Manipulation**: `str.translate()`, `str.maketrans()`, `str.lower()`, and `str.split()`.
- **Dictionaries & Hash Maps**: Key-value frequency counting using `dict.get()`.
- **Sorting with Lambdas**: `sorted(iterable, key=lambda x: x[1], reverse=True)`.
- **List Slicing & Enumeration**: Extracting the top 10 elements via `[:10]` and displaying numbered output with `enumerate(..., start=1)`.
- **Robust Path Handling**: Resolving relative paths with `os.path.dirname(os.path.abspath(__file__))`.

---

## Requirements
- Python 3.8 or higher.
- Standard Library only (`os`, `string`, `sys` — no external packages required).

---

## How to Execute the Program

### From the Repository Root (uses default `sample.txt`)
```bash
python "Day 2/word_frequency.py"
```

### From the `Day 2` Directory
```bash
cd "Day 2"
python word_frequency.py
```

### With a Custom Text File
```bash
python "Day 2/word_frequency.py" path/to/your/custom_file.txt
```

---

## Example Usage

Using the included `sample.txt`:
```text
===== WORD FREQUENCY COUNTER =====
Top 10 Most Frequent Words:

1. python: 6
2. and: 5
3. for: 4
4. backend: 4
5. is: 2
6. programming: 2
7. development: 2
8. with: 2
9. data: 2
10. structures: 2
```
