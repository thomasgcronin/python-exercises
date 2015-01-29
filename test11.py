"""my_dict = {
    'Christopher': 'S',
    'Bob': 'Z',
    'Nate': 'M',
    'Michael': 'Z',
    'Guy': 'H',
    'Sariah': 'M'
}

# Inline function definition
# A list of 3 callable functions
# print sorted(my_dict.values())

# def get_value(k):
#     return my_dict[k]

# print sorted(my_dict, key=my_dict.get)  # Still sorts by value by indexing with get,

# but since we're sorting the dict,
# it returns a list of keys.
def f(x):

    Same as declaring lambda x: x[1]

    return x[1]

# print sorted(my_dict.items(), key=lambda x: x[1])
# print sorted(my_dict.items(), key=f)

# print f(my_dict.items())
iterator = my_dict.iteritems()
print iterator

for pair in iterator:
    print pair

def f(n):
    return lambda x: x + n


def f2(n):
    def g(x):
        return x + n
    return g

var = f(7)


print var(10)
print var(33)


class Cat:
   def __init__(self, paws):
       self.paws = paws

   def meow(self):
       return "Meow! I have %s paws!" % self.paws



my_cat = Cat(4)
my_other_cat = Cat(8)

cats = [my_cat, my_other_cat]

for current_cat in cats:
    print current_cat
    print current_cat.meow()

class Person:
    def __init__(self, name, age, birthday, address):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.address = address

    def __str__(self):
        name_str = "Name: " + self.name + "\n"
        age_str = "Age: " + str(self.age) + "\n"
        birthday_str = "Birthday: " + self.birthday + "\n"
        address_str = "Address: " + self.address + "\n"

        final_str = name_str + age_str + birthday_str + address_str

        return final_str

dave = Person("Dave", 20, "October 25", "36 Helm Ave")

print(dave)




class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)


    def __eq__(sef, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)





morning = Tme (6, 30, 00)
afternoon = Time (13, 00, 00)



print morning < afternoon
print afternoon < morning


class Parent(object):
    #base class is a parent and one tht doesn't have any other class

    def implicit(self):

        print "PARENT implicit()"

class Child(Parent):

    pass

dad = Parent()

son = Child()

dad.implicit()


class Animal(object):


#Base class for all other animals


    def __init__(self, name):
        self.name = name

    def talk(self):
        raise Notimplementederror

class Human(Animal):
    def talk(self):
        print "I am a human!"

class Horse(Animal):
    def __init__(self, name, legs):
    super(Horse, self).__init__(name)
    self.legs = legs

    def talk(self):
        print "Neigh!"

class Centaur(Human, Horse):
    pass


class Person(object):
    pass

    def __init__(self, name, age ,school):
        self.name = name

    def teach(self):
        raise Notimplementederror


class Employee(Person):
    def teach(self):

    def __init__(self, name, age, school):
        super(self).__init__(name, age, school)
        print "My Name is John. I am 23 years old. I am teaching at ABC Primary School."

class Student(Person):
    def study(self):

        def __init__(self, name, age, school):
        super(self).__init__(name, age, school)
        print: "My name is Peter. I am 9 years old. I am studying at ABC Primary school.Z


class Person:
    def __init_(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school



class Student(Person):

    def __str__(self):
        return "My name is %s . I am %s years old. I study at %s." % (self.name, self.age, self.school)

class Employee(Person):

    def __str__(self):
        return "My name is %s . I am %s years old. I teach at %s." % (self.name, self.age, self.school)




peter = Student("Peter", 9, ABC Primary School")
john = Employee("John", 23, ABC Primary Scho0l")


print peter
print john



class Employee(object):
    pass

    #{{{Modules/Python/Code/composition.py}}

    {{{Modules def __init__(self, name, age ,):
        self.name = name

    def teach(self):
        raise Notimplementederror

        print "My name is Morgan Williams. I am 24 years old and I am a software developer"



class Job():
    def teach(self):

    def __init__(self, name, age, school):
        super(self).__init__(title, wage, company, description)
        #constructor




class Person:
    def __init_(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school



class job():

    def __init__(self, title, wage, company, description):
        self.title = name
        self.wage = name
        self.company = age
        sel
        return "This job is a %s . You earn %s . We are called %s.  You will %s" % (self.title, self.wage, self.wage, self.school, self.description)

class employee(Person):
        self.job = name
        self.name = name
        self.age = age

    def __str__(self):
        return "My name is %s . I am %s years old. ." % (self.name, self.age)




Morgan = Employee("Morgan", 24, ABC, software developer")
ABC = Employee("software developer", 55k/yr, ABC develop software")
#instance



print peter
print john


class Job:

    def __init__(self, title, wage, company, description):
        #constructor, method
        self.title = title
        self.wage = wage
        self.company = company
        self.description = description

    def __str__(self):
        return self.title


class Employee:

    def __init__(self, name, age, title, wage=0, company='', description=''):
        self.job = Job(title, wage, company, description)
        self.name = name
        self.age = age
        #data atributes

    def __str__(self):
        return "My name is %s and I am %s years old and I am a %s" % (self.name, self.age, self.job)

        classes and descriptor string

larry = Employee('Larry', 52, 'Plumber', 52000, "Larry's Plumbing", "Plumbs things.")
#instnce
print larry"

class Point():

    def__init__(selfself, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return str((self.__x, self.__y))

    def sum(self):
        return self.__x + self.__y

point = Point(5, 8)

point.x = 17

print point
print point.sum()

class Person(object):

    def accessible(self):

        print "You can see me!"
        self.__inaccessible()

    def __inaccessible(self):

        print "You can NOT see me!"

person = Person()

person.accessible()

class Num:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum_nums(self):
        sum = compute_sum()
        pritn sum()

    def __compute_sum(selfself):
        return self.x + self.y

num = Num(6, 9)
num.print_sum()

class A(object):
    def __init__(self, param1):
        self.param1 = param1

    def method1(self):
        raise Exception('Cannot call this method directly!')


class B(A):
    def method1(self):
        print "This is %s's method1" % self.param1


class C(A):
    def method1(self):
        print "This is %s's method1" % self.param1


if __name__ == "__main__":
    letters = [B('B'), C('C'), B('B'), C('C'), B('B'), C('C'), B('B'), C('C')]
    #instantiation

    for element in letters:
        element.method1()

class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastes_like(self):
        return "%s is type %s\n\thas %s calories\n\tand tastes like %s" % (self.name, self.__class__.__name__, self.calories, self.taste)


class HotDog(Food):
    taste = "extremely processed meat"


class Hamburger(Food):
    taste = "grilled goodness"


class ChickenPatty(Food):
    taste = "chicken"


dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Mickey Mouse shaped Chicken Tenders', 170))

for course in dinner:
    print course.tastes_like()"""

class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastes_like(self):
        return "%s is %s\nhas %s calories\nand tastes like %s" % (self.name, self.__class__.__name__, self.calories, self.taste)


class fortune_chicken(Food):
    taste = "fresh,tasty, tender chicken bits with a sweet glaze vegetable glaze"


class lo_mein(Food):
    taste = "noodles and vegetables"


class peking_ravioli(Food):
    taste = "noodles and pork"


dinner = []
dinner.append(fortune_chicken('Batter-fried chicken nuggets with a sweet and sour glaze, green peppers, onions, and ginger', 230))

dinner.append(lo_mein('Nutritious steamed noodles with carrots, water chestnuts with teriyaki glaze', 260))

dinner.append(peking_ravioli('Delicious little steamed noodles with pork_casserole inside', 170))

for course in dinner:
    print course.tastes_like()


