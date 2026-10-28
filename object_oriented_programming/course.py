class Student:
    def __init__(self , name , course_study, year):
        self.name = name
        self.course_study = course_study
        self.year = year

    def introduce(self):
        print(f"I am {self.name} and i pursue {self.name } in the current year {self.year}")

student1 = Student("Dlaniger" , "It" , 2026)

print(student1.name)
print(student1.course_study)
print(student1.year)
student1.introduce()