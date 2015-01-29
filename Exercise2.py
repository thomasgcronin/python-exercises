gallons_of_gas = raw_input("Please enter the number of gallons of gasoline: ")

while gallons_of_gas.isalpha() or (not gallons_of_gas.isalpha() and float(gallons_of_gas) <= 0):

    if gallons_of_gas.isalpha():
        gallons_of_gas = raw_input("Please enter the number of gallons of gasoline: ")

    elif float(gallons_of_gas) <= 0:
        gallons_of_gas = raw_input("Please enter the number of gallons of gasoline: ")


gallons_of_gas = float(gallons_of_gas)

gallons_to_liters = float(gallons_of_gas) * 3.7854118
barrels_of_oil_required = float(gallons_of_gas) * .005128
pounds_of_co2_produced = float(gallons_of_gas) * 20.0
gallons_of_gas_ethan = float(gallons_of_gas) * 1.5191
gallons_of_gas_dollars = float(gallons_of_gas) * 4


print "%d gallons of gas is equal to %.3f liters" % (gallons_of_gas, gallons_to_liters)
print "%d gallons of gas requires %.3f barrels of oil" % (gallons_of_gas, barrels_of_oil_required)
print '%d gallons of gas produces %.2f liters of CO2' % (gallons_of_gas, pounds_of_co2_produced)
print "%d gallons of gas is equal to %.3f gallons of energy equivalent ethanol" % (gallons_of_gas, gallons_of_gas_ethan)
print "%d gallons of gas costs %.2f dollars" % (gallons_of_gas, gallons_of_gas_dollars)


