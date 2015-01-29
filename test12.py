"""class Person(object):

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

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
            self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()

son.override()

son.altered()

class Car:


    def __init__(self, num_wheels, sw_color, sw_diameter):
        self.num_wheels = num_wheels
        self.steering_wheel = SteeringWheel(sw_color, sw_diameter)

class SteeringWheel:

    def __init__(self, sw_color, sw_diameter):
        self.color = sw_color
        self.diameter = sw_diameter




my_car = Car(4, "Black", 10)
your_car = Car(3, "White", 12)
print my_car.num_wheels
print my_car.steering_wheel

print my_car.steering_wheel.color
print my_car.steering_wheel.diameter"""


class Car:


    def __init__(self, model):
        if "Honda"nand "Civic" and"1998":

            self.num

