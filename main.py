# Module 10: Modules & Packages (Importing our 3 custom modules)
import student_model
import calculations
import future_predictor

# Module 1 & 2: Strings, Print output, and Variables
print("=" * 45)
print("   B.TECH SEMESTER-1 ACADEMIC RECORD SYSTEM   ")
print("=" * 45)

# Module 7: Core Data Structures (List storing subjects)
subjects = ["Engineering Maths", "Applied Physics", "Python Programming", "Basic Electronics"]

# Module 8: Control Flow (While loop)
while True:
    print("\nMenu:")
    print("1. Enter Student Details & Marks")
    print("2. Exit Program")

    # Module 4: Input / Output
    user_choice = input("Enter choice (1 or 2): ").strip()

    if user_choice == "1":
        # Module 4: Input and Module 6: Type Conversion (str to int)
        try:
            roll = int(input("\nEnter Roll Number: "))
            name = input("Enter Student Name: ").strip()

            # Module 12: Instantiating the object from student_model module
            student = student_model.Student(roll, name)

            print(f"\nEnter marks (out of 100) for {len(subjects)} subjects:")
            total = 0

            # Module 8: For Loop iterating over subject list
            for sub in subjects:
                mark = int(input(f"Enter marks for {sub}: "))
                student.add_mark(mark)
                total += mark  # Module 3: Compound Assignment Operator

            # Output Report
            print("\n" + "-" * 35)
            print("       OFFICIAL REPORT CARD")
            print("-" * 35)
            student.display_details()

            # Module 11: Displaying stored scores from array
            print("Scores from Array :", student.marks_array.tolist())
            print(f"Total Obtained     : {total} / {len(subjects) * 100}")

            # Module 9 & 10: Calling functions from calculations module
            percentage = calculations.compute_percentage(total, len(subjects))
            grade = calculations.assign_grade(percentage)

            print(f"Percentage         : {percentage}%")
            print(f"Final Grade        : {grade}")

            # Module 10 & 13: Calling future predictor module
            future_predictor.forecast_future(percentage)

            # Optional target checker input
            target = float(input("\nEnter your dream percentage goal for B.Tech: "))
            future_predictor.calculate_target_gap(percentage, target)
            print("-" * 35)

        except ValueError:
            print("Error: Invalid numeric input! Please enter integer marks and roll numbers.")

    elif user_choice == "2":
        # Module 8: Loop termination
        print("\nExiting program. Best wishes for your B.Tech journey!")
        break

    else:
        print("Invalid option! Please enter 1 or 2.")