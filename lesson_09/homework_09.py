class Student:
    def __init__(self, name, surname, age, grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade

    def greet(self):
        return f"Hello, my full name is {self.name} {self.surname}"

    def change_grade(self, new_grade=100):
        self.grade=new_grade
        return f"My new grade is {new_grade}"

student = Student ("Olha", "Biriukova", 40, 90)

print(student.greet())
print(student.change_grade(100))