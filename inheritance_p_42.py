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
"""

class Point:
    "A class implementation of 2-Dimensional point."

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '( % d, % d)' % (self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y


point1 = Point(16, 0)
point2 = Point(-11, 22)

print point1 + point2  # (2, 6)
print point1 - point2  # (14, 4)