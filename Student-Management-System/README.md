# Student Management System

A simple command-line Student Management System built using Python. It allows users to add, view, search, update and delete student records, calculate academic results, and identify students with the highest and lowest average.

## Features
- Add student records
- View all students
- Search by Student ID
- Update student information and marks
- Delete student records
- Calculate total, average, grade and pass/fail status
- Find highest and lowest average
- Save records in a JSON file
- Load saved records automatically

## Requirements
- Python 3.9 or later
- No external Python packages are required

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

The program will create `data/students.json` automatically when data is saved.

## Project Structure

```text
Student-Management-System/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   └── students.json
└── report/
    └── Project_Report.docx
```

## Data Storage
Student records are stored locally in JSON format. No internet connection or external database is required.

## Notes
This project is intended as an academic Python project demonstrating programming fundamentals, functions, data structures, file handling, validation and basic problem solving.
