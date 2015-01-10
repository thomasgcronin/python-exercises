user_input_1 = raw_input("Please enter the first integer: ")
while not user_input_1.isdigit():
    user_input_1 = raw_input("Not an integer. Please enter an integer: ")

user_input_2 = raw_input("Please enter the second integer: ")
while not user_input_2.isdigit() or user_input_2 == "0":

    if not user_input_2.isdigit():
        user_input_2 = raw_input("Not an integer. Please enter an integer: ")

    elif user_input_2 == "0":
        user_input_2 = raw_input("Please enter an integer other than 0: ")

integer_1 = int(user_input_1)
integer_2 = int(user_input_2)

my_sum = integer_1 + integer_2
my_sum2 = integer_1 - integer_2
my_product = integer_1 * integer_2
my_quotient = integer_1 / integer_2
my_quotient2 = integer_1 % integer_2


print "The sum of %d and %d is %d" % (integer_1, integer_2, my_sum)
print "The difference of %d and %d is %d" % (integer_1, integer_2, my_sum2)
print "The product of %d and %d is %d" % (integer_1, integer_2, my_product)
print "The quotient of %d and %d is %d with remainder %d" % (integer_1, integer_2, my_quotient, my_quotient2)