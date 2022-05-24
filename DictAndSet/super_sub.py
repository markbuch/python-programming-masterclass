animals = {'Turtle',
            'Horse',
            'Robin',Untitled document
            'Python',
            'Swallow',
            'Hedgehog',
            'Wren',
            'Aardvark',
            'Cat',
            }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(f'first is a superset of animals: {birds.issuperset(animals)}')

print(birds <= animals)
print(birds < animals)

print('*' * 80)
garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)
print(garden_birds <= birds) # is a subset?
print(garden_birds < birds)  # is it a proper subset
