class Student:
    def __init__(self,std_name, marks):
        self.std_name =std_name
        self.marks = marks

    def display(self):
        print(self.std_name)
        print(self.marks)

s1 = Student("ayesha",30)
s1.display()