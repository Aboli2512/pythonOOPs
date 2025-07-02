class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

    def method1(self):
        pass


class Student(Person):

    def __init__(self,name, surname , age):
        self.surname = surname
        Person.__init__(self, name, age)
        print(self.name, self.surname, self.age)

    def method2(self):
        pass

p = Student('Aboli', 'Chaudhari', 25)