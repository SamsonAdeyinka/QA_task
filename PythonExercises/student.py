class Student():
    def __init__(self, english = 25, maths = 25, science = 25):
        self.maths = maths
        self.english = english
        self.science = science

    def get_average (self):
        average = (self.english + self.maths + self.science) / 3
        print(average)

student_1 = Student()
student_1.maths = 45
student_1.get_average()

student_2 = Student()
student_2.maths = 100
student_2.get_average()
