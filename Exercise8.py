"""def naive_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return naive_fib(n-1) + naive_fib(n-2)


def fib_helper(n):
    if n == 0:
        return 0
    else:
        return fib_improved(n, 0, 1)

def fib_improved(n, p0, p1):
    if n == 1:
        return p1
    else:
        return fib_improved(n-1, p1, p0 + p1)"""


# loop 0-40
    # start timer
    # call naive_fib
    # end timer

    # start timer
    # call fib_helper
    # end timer

    for str.count in [0, 40]:
        print(count)
        print('Yes' * count)
        print('Done counting.') # changed so indented


print "str.count(sub) : ", str.count(sub)

my_map = [[], [], []]

def replace_pixel(replacement_character, original_character, x, y):

    if x == -1 or y == -1:
        return

    if x >= len(my_map[0]):
        return

    if y >= len(my_map):
        return

    if my_map[x][y] == original_character:
        my_map[x][y] = replacement_character


    replace_pixel(replacement_character, original_character, x-1, y)
    replace_pixel(replacement_character, original_character, x+1, y)
    replace_pixel(replacement_character, original_character, x, y-1)
    replace_pixel(replacement_character, original_character, x, y+1)


for key, value in us_cities.items():
    data_list = value.split(" ")  # [##, (C|F)]
    if data_list[1] == "C":
        new_temp = to_fahrenheit(int(data_list[0]))
        print "In " + key + " it is " + data_list[0] + " degrees Celsius which is equivalent to " + str(new_temp) + " degrees fahrenheit."
        # to fahrenheit
    else:
        new_temp2 = to_celsius(int(data_list[0]))
        print "In " + key +

start = clock()
result = fib_naive(n)
stop = clock()
difference = (stop - start) * 1000 # clock returns a value in seconds.