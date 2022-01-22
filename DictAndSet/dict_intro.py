vehicles = {
	'dream': 'Honda 250T',
	'roadster': 'BMD R1100',
	'er5': 'Kawasaki ER5',
	'can-am': 'Bombardier Can-Am 250',
	'virago': 'Yamaha XV250',
	'tenere': 'Yamaha XT650',
	'jimny': 'Suzuki Jimny 1.5',
	'fiesta': 'Ford Fiesta Ghia 1.4',
}

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)

# Assign key/value pairs to a dictinary.
vehicles["starfigheter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virago (how to update a value in a dictionary)
vehicles["virago"] = "Yamaha XV535"

# delete a key/value from a dictionary
del vehicles["starfigheter"]
# del vehicles["f1"]

# Better option to delete a key/value pair
result = vehicles.pop("f1", "You wish! ")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()
# how to iterate over a dictionary.
# for key in vehicles:
# 	print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
	print(key, value, sep=", ")


