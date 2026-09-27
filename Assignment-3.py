class Student:
    def _init_(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department

    def calculate_result(self, m1=0, m2=0, m3=0):
        return (m1 + m2 + m3) / 3

    def get_student_type(self):
        return "General Student"

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Email: {self.__email}, Age: {self.age}, Dept: {self.department}, Type: {self.get_student_type()}")


class UndergraduateStudent(Student):
    def _init_(self, name, student_id, email, age, department, semester):
        super()._init_(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate"


class GraduateStudent(Student):
    def _init_(self, name, student_id, email, age, department, research_topic):
        super()._init_(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate"

s1 = UndergraduateStudent("Rahim", "101", "rahim@mail.com", 21, "CSE", "5th")
s2 = GraduateStudent("Karim", "201", "karim@mail.com", 24, "EEE", "AI")

s1.display_info()
print("Result:", s1.calculate_result(80, 85, 90))

s2.display_info()
print("Result:", s2.calculate_result(75, 88, 92))