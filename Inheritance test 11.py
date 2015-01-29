class Person(object):

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school


class Student(Person):

    def __init__(self, name, age, school, locker_number):
        self.locker_number = locker_number
        # super(Student, self).__init__(name, age, school)
        self.name = name
        self.age = age
        self.school = school

    def __str__(self):
        return "My name is %s. I am %s years old. I am studying at %s. My locker number is %s" % (self.name, self.age, self.school, self.locker_number)


class Employee(Person):

    def __str__(self):
        return "My name is %s. I am %s years old. I am teaching at %s." % (self.name, self.age, self.school)


peter = Student("Peter", 9, "ABC Primary School", 1234)
john = Employee("John", 23, "ABC Primary School")

print peter
print john