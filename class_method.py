class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print("School Name:", cls.school)

Student.show_school()
