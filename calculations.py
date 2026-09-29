# Module 9: Functions in Python
def compute_percentage(total_marks, subject_count):
    # Module 3: Arithmetic Operators (/ and *)
    # Module 5: Precedence & Associativity - Parentheses ( ) run first, then division, then multiplication
    max_marks = subject_count * 100
    percentage = (total_marks / max_marks) * 100
    return round(percentage, 2)


def assign_grade(percentage):
    # Module 8: Conditional statements (if-elif-else)
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"