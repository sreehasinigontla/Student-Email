# 📧 Student Email and Identifier Validation System

## 📌 Project Overview

The **Student Email and Identifier Validation System** is a Python-based application designed to validate student email addresses and registration identifiers using predefined formatting rules.

The system identifies malformed separators, invalid character groups, missing components, and incorrect registration ID formats.

It generates a validation report showing valid and invalid student records along with specific error messages.

## 🎯 Objectives

- Validate student email addresses.
- Validate student registration identifiers.
- Check email separators and components.
- Identify invalid characters.
- Detect missing email components.
- Validate registration ID prefixes.
- Check year and student number formats.
- Identify malformed separators.
- Generate validation reports.
- Display valid and invalid student records.

## 📋 Validation Rules

### 1. Email Format

Sample valid email:

`student@gmail.com`

Rules:

- Must contain exactly one `@` symbol.
- Username must not be empty.
- Domain name must not be empty.
- Domain must contain a dot.
- Username cannot start or end with a dot.
- Consecutive dots are not allowed.
- Invalid special characters are not allowed.
- Domain extension must contain at least two alphabetic characters.

### 2. Registration ID Format

Sample valid registration ID:

`STU-2026-00123`

Rules:

- Prefix must be `STU`.
- Year must contain exactly four digits.
- Student number must contain exactly five digits.
- Exactly two hyphens must be present.
- All three components must be available.

## 🚀 Features

1. Multiple student record validation.
2. Email address validation.
3. Registration ID validation.
4. Missing component detection.
5. Invalid character detection.
6. Separator validation.
7. Prefix validation.
8. Year format validation.
9. Student number validation.
10. Detailed validation report generation.

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## 🐍 Python Concepts Used

- Variables and Data Types
- Strings
- String Methods
- Lists
- Dictionaries
- Conditional Statements
- For Loops
- While Loops
- Functions
- User Input and Output
- String Operations

## 📁 Project Structure

```text
Student-Email-Identifier-Validation/
│
├── student_validation.py
├── README.md
├── problem_statement.txt
├── objectives.txt
├── assumptions.txt
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
│
└── output_screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Download or clone the GitHub repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Run the following command:

```bash
python student_validation.py
```

**Step 6:** Enter the number of students.

**Step 7:** Enter each student's name, email address, and registration ID.

**Step 8:** View the validation report.

## 🧪 Test Cases

| Test Case | Input / Condition | Expected Result |
|---|---|---|
| TC01 | student@gmail.com | Valid email |
| TC02 | studentgmail.com | Missing @ separator |
| TC03 | student@@gmail.com | Multiple @ separators |
| TC04 | @gmail.com | Username missing |
| TC05 | student@ | Domain missing |
| TC06 | student@gmail | Missing domain dot |
| TC07 | student@gmail.com with spaces | Invalid email |
| TC08 | STU-2026-00123 | Valid registration ID |
| TC09 | STU202600123 | Missing separators |
| TC10 | ABC-2026-00123 | Invalid prefix |
| TC11 | STU-26-00123 | Invalid year |
| TC12 | STU-2026-123 | Invalid student number |

## 📊 Expected Output

The program displays:

- Student name.
- Student email address.
- Registration ID.
- Email validation status.
- Registration ID validation status.
- Missing component errors.
- Invalid character errors.
- Malformed separator errors.
- Total number of students.
- Valid student count.
- Invalid student count.

## 📝 Conclusion

The Student Email and Identifier Validation System provides a simple and efficient method for checking student information using Python.

It validates email addresses and registration identifiers based on predefined formatting rules and identifies missing components, invalid characters, and malformed separators.

This project demonstrates the practical application of Python string operations, conditional statements, loops, lists, dictionaries, and functions in a real-world student information validation system.

---

**Project Name:** Student Email and Identifier Validation System

**Subject:** Python Activity-Based Learning

**Programming Language:** Python 3

**Project Type:** Case Study
