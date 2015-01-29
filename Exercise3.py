miles_per_hour = raw_input("Please enter speed in miles per hour: ")

while miles_per_hour.isalpha() or (not miles_per_hour.isalpha() and float(miles_per_hour) <= 0):

    if miles_per_hour.isalpha():
        miles_per_hour = raw_input("Please enter speed in miles per hour: ")

    elif float(miles_per_hour) <= 0:
        miles_per_hour = raw_input("Please enter a number greater than 0: ")


miles_per_hour = float(miles_per_hour)

barleycorns_per_day = miles_per_hour * 189334.588235 * 24
furlongs_per_fortnight = miles_per_hour * 8 * 368
mach_number = miles_per_hour / 770
percentage_speed_of_light = miles_per_hour * 1.5191


print "Original speed in miles/hour is %.4f" % (miles_per_hour)
print "Converted to barleycorn/day is %.4f" % (barleycorns_per_day)
print 'Converted to furlongs per fortnight is %.4f' % (furlongs_per_fortnight)
print "Converted to Mach number is %.4f" % (mach_number)
print "Converted to the percentage of the speed of light is %.4f" % (percentage_speed_of_light)