"""x = 5

def show():

    print x

show()

x = 5

def show():
    x = 42

    print x

show()

print x

x = 5

def show():

    global x

    x = 42

    print x

show()

print x

x = 5

def show():

    global x

    print x # Semantic error! The interpreter believes that x is a local variable.

    x = 42

    print x

show()

print x

a = [5, 2, 3, 1, 4]
a.sort()
print a

sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})


for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
     # Note trailing comma on previous line
    print repr(x*x*x).rjust(4)


s = str("asdf")
i = 10
print isinstacne(s, str)

l = [1,2,3]
l = list ([1,2,3)])

my_cat = Cat(4)
my_other_cat = Cat(8)

print type(my_cat)
print my_cat







class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn
chris = Person ('Chris', 123467890)
print chris.name
print chris._Person__ssn

#print chris.__dict__


class Person(object):

    def __init__(self, name):
        print "Hitting the __init__ method"
        self.name = name
        Person.person_count += 1
    def __del__(self):
        print "Hitting the __del__ method"

john = Person("John") #Adiing an attribute
john.age = 36
print john.age
# Modify the attribute
john.age = 35
print john.age
# Remove the attribute
del john.age"""





class Person:
    def __init__(self, name='', age=0, birthdate='', address=''):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.address = address

    def __str__(self):
        name_str = "Person Name: " + self.name + "\n"
        age_str = "Person Age: " + str(self.age) + "\n"
        birthday_str = "Person Birthday: " + self.birthdate + "\n"
        address_str = "Person Address: " + self.address  + "\n"

        final_str = name_str + age_str + birthday_str + address_str

        return final_str




tom = Person('Tom', 55, '12/1/1990', '123 Street')
kim = Person("Kim", 42, '1/24/72', '123 Street')
no_one = Person()

print tom
print kim
print no_one
