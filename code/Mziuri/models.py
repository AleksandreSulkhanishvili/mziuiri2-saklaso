class Member:
    def __init__(self, name, age, status, subject) -> None:
        self.name = name
        self.age = age
        self.subject = subject
        self.status = status

class Teacher(Member):
    def __init__(self, name, age, status, subject, salary) -> None:
        super().__init__(name, age, status, subject)
        self.__salary = salary

    def calculate_yearly_salary(self):
        return self.salary * 12

class Student(Member):
    def __init__(self, name, age, status, grade) -> None:
        super().__init__(name, age, status)
        self.grade = grade
    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}, status: {self.status}, grade: {self.grade}"


lizi = Student("lizi", 14, 'student', 95.7)
shotiko = Teacher("shotiko", 21, 'teacher', "python", 100000)

print(lizi.__str__())