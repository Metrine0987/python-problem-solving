class Person:
    def __init__(self , name ,gender ,age):
     self.name = name
     self.gender =  gender
     self.age = age

class Teacher(Person):
    def __init__(self , name , gender , age , subject):
        super().__init__(name , gender , age)
        self.subject = subject

