# Module 11: Array data structure for storing integer scores
import array

# Module 12: Object-Oriented Programming (Class, __init__, and Methods)
class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        # 'i' typecode specifies signed integers
        self.marks_array = array.array('i', [])

    def add_mark(self, score):
        self.marks_array.append(score)

    def display_details(self):
        print("Roll Number :", self.roll_number)
        print("Student Name:", self.name)