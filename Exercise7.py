"""def to_fahrenheit(temp):
    return temp * 9/5 + 32

def to_celsius(temp):
    return (temp - 32) * 5 / 9

us_cities = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}

for key, value in us_cities.items():
    data_list = value.split(" ")  # [##, (C|F)]
    if data_list[1] == "C":
        new_temp = to_fahrenheit(int(data_list[0]))
        print "In " + key + " it is " + data_list[0] + " degrees Celsius which is equivalent to " + str(new_temp) + " degrees fahrenheit."
        # to fahrenheit
    else:
        new_temp2 = to_celsius(int(data_list[0]))
        print "In " + key + " it is " + data_list[0] + " degrees fahrenheit which is equivalent to " + str(new_temp2) + " degrees celsius. "
        # to celsius"""



def c2f(celsius):
    return celsius * 9/5 + 32

def f2c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


us_cities = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}

for key, value in us_cities.items():
    data_list = value.split(" ")  # [##, (C|F)]
    if data_list[1] == "C":
        new_temp = c2f(int(data_list[0]))
        print "In " + key + " it is " + data_list[0] + " degrees Celsius which is equivalent to " + str(new_temp) + " degrees fahrenheit."
        # to fahrenheit
    else:
        new_temp2 = f2c(int(data_list[0]))
        print "In " + key + " it is " + data_list[0] + " degrees fahrenheit which is equivalent to " + str(new_temp2) + " degrees celsius. "
        # to celsius