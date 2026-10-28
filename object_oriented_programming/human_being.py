class Person:
    def __init__(self , name ,gender ,age):
     self.name = name
     self.gender =  gender
     self.age = age

class Teacher(Person):
    def __init__(self , name , gender , age , subject):
        super().__init__(name , gender , age)
        self.subject = subject

person1 = Person("Quinter" , "female" , 32)
teacher1 = Teacher("Felix" , "male" , 40, "Programming")


print(teacher1.name)