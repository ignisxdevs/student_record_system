# B.Tech Semester-1 Academic Record System

## 1. Project Title

**B.Tech Semester-1 Academic Record System**

## 2. Overview of the Project

The B.Tech Semester-1 Academic Record System is a Python-based console application for entering and managing a student's Semester-1 academic record.

The program allows the user to enter a student's roll number, name, and marks for four subjects:

- Engineering Maths
- Applied Physics
- Python Programming
- Basic Electronics

After entering the marks, the program generates an official report card showing the student's details, scores, total marks, percentage, and final grade. It also provides a future academic forecast and calculates the percentage gap between the student's current percentage and a desired target percentage.

The project is organized into custom Python modules for student data, calculations, and future prediction.

## 3. Features

- Enter student roll number and name.
- Enter marks for four Semester-1 subjects.
- Store student marks using Python's `array` data structure.
- Display the student's details and stored marks.
- Calculate the total marks obtained.
- Calculate the percentage up to two decimal places.
- Assign a final grade based on the percentage.
- Provide a Semester-2 placement and honors forecast.
- Compare the current percentage with a user's target percentage.
- Handle invalid numeric input with an error message.
- Provide a simple menu to enter records or exit the program.

### Grade Criteria

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 75% - 89.99% | A |
| 60% - 74.99% | B |
| 40% - 59.99% | C |
| Below 40% | Fail |

### Future Forecast Criteria

| Percentage | Forecast Status |
|---|---|
| 85% and above | Honors Eligibility Track |
| 65% - 84.99% | Core Competency Track |
| Below 65% | Remedial Support Track |

## 4. Technologies/Tools Used

- **Python 3**
- **Python Standard Library**
- `array` module for storing integer marks
- Python functions for calculations and forecasting
- Python classes and objects for student information
- Custom Python modules:
  - `main.py`
  - `student_model.py`
  - `calculations.py`
  - `future_predictor.py`
- Console/terminal for program execution and testing

No external Python packages are required.

## 5. Project Structure

```text
B.Tech-Semester-1-Academic-Record-System/
│
├── main.py
├── student_model.py
├── calculations.py
├── future_predictor.py
└── README.md
```

### Module Description

- **`main.py`** - Main program, menu, user input, report-card output, and calls to the other modules.
- **`student_model.py`** - Contains the `Student` class and stores student marks in an integer array.
- **`calculations.py`** - Contains functions for percentage calculation and grade assignment.
- **`future_predictor.py`** - Provides the future academic forecast and target-percentage gap calculation.
- **`README.md`** - Project documentation and instructions.

## 6. Steps to Install & Run the Project

### Step 1: Install Python

Install **Python 3** on your computer.

Verify the installation by opening a terminal/command prompt and running:

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

### Step 2: Place the Project Files Together

Keep the following files in the same project folder:

```text
main.py
student_model.py
calculations.py
future_predictor.py
README.md
```

### Step 3: Open the Project Folder

Open a terminal or command prompt in the project folder.

### Step 4: Run the Program

Run:

```bash
python main.py
```

Or, on systems where Python 3 is invoked with `python3`:

```bash
python3 main.py
```

### Step 5: Use the Menu

When the program starts, it displays:

```text
Menu:
1. Enter Student Details & Marks
2. Exit Program
```

Enter `1` to enter a student's details and marks.

Enter `2` to exit the program.

## 7. Instructions for Testing

### Test Case 1: Valid Student Record

Run the program and select option `1`.

Example input:

```text
Enter Roll Number: 101
Enter Student Name: Rahul
Enter marks for Engineering Maths: 90
Enter marks for Applied Physics: 80
Enter marks for Python Programming: 95
Enter marks for Basic Electronics: 85
Enter your dream percentage goal for B.Tech: 90
```

Expected calculation:

```text
Total Obtained     : 350 / 400
Percentage         : 87.5%
Final Grade        : A
```

The program should also display the corresponding future forecast and target-gap message.

### Test Case 2: A+ Grade

Enter marks such that the percentage is at least 90%.

Example:

```text
95
92
90
96
```

Expected result:

```text
Final Grade        : A+
```

### Test Case 3: Fail Grade

Enter marks that produce a percentage below 40%.

Example:

```text
30
35
25
30
```

Expected result:

```text
Final Grade        : Fail
```

### Test Case 4: Invalid Numeric Input

When the program asks for a roll number or marks, enter invalid text instead of a number.

Example:

```text
Enter Roll Number: abc
```

Expected result:

```text
Error: Invalid numeric input! Please enter integer marks and roll numbers.
```

### Test Case 5: Target Percentage

After the report card is displayed, enter a target percentage greater than the current percentage.

For example, if the current percentage is `75%` and the target is `85%`, the program should report:

```text
Goal: You need an increase of 10.00% to reach your target of 85.0%.
```

If the target is already achieved, the program should indicate that the target has been achieved or surpassed.

### Test Case 6: Exit

At the menu, enter:

```text
2
```

Expected result:

```text
Exiting program. Best wishes for your B.Tech journey!
```

## 8. Notes

- Marks are entered as integer values out of 100 for each subject.
- The application is designed to run in a terminal/command prompt.
- All four Python source files should remain in the same directory so that the custom modules can be imported correctly.
