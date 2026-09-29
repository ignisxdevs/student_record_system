# B.Tech Semester-1 Academic Record System

## 1. Problem Statement

Managing and evaluating a student's Semester-1 academic performance manually can be time-consuming and may involve calculation errors. Students need a simple way to enter their academic details, calculate total marks and percentage, determine their grade, and understand their future academic target requirements.

The **B.Tech Semester-1 Academic Record System** addresses this problem by providing a console-based Python application that collects student details and marks, generates an academic report, calculates the percentage and grade, and provides a basic future academic forecast and target-gap calculation.

## 2. Scope of the Project

The scope of this project includes the following:

- Recording a student's roll number and name.
- Recording marks for four Semester-1 subjects:
  - Engineering Maths
  - Applied Physics
  - Python Programming
  - Basic Electronics
- Storing the student's marks using an array.
- Calculating total marks and percentage.
- Assigning a grade based on the calculated percentage.
- Displaying an official-style report card.
- Providing a future academic forecast based on the student's percentage.
- Calculating the percentage increase required to reach a user's target percentage.
- Handling invalid numeric input.
- Providing a simple menu-driven console interface.

The project is intended as a basic academic record and performance-assistance system. It does not include database storage, web-based access, authentication, or automated integration with an institution's official academic system.

## 3. Target Users

The primary target users are:

- **B.Tech students** who want to record and review their Semester-1 academic performance.
- **Students preparing for future academic targets** who want to compare their current percentage with a desired target.
- **Teachers or instructors** who want a simple demonstration of student record processing using Python.
- **Beginners learning Python** who can use the project to understand functions, modules, classes, arrays, loops, conditional statements, input/output, and basic calculations.

## 4. High-Level Features

### Student Record Management
- Enter student roll number.
- Enter student name.
- Enter marks for four subjects.
- Store marks in an integer array.

### Academic Calculation
- Calculate total marks obtained.
- Calculate percentage.
- Assign a final grade based on percentage.

### Report Card
- Display student details.
- Display individual/stored scores.
- Display total marks.
- Display percentage.
- Display final grade.

### Future Academic Prediction
- Provide a Semester-2 placement and honors forecast based on the current percentage.
- Display an appropriate academic status track.

### Target Percentage Analysis
- Accept a user's desired percentage.
- Calculate the gap between the current percentage and the target.
- Inform the user when the target has already been achieved or surpassed.

### Input Validation
- Detect invalid numeric input for roll numbers and marks.
- Display an error message and prevent invalid numeric input from being processed.
