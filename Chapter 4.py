magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())


magicians = ['alice', 'lavid', 'carolina']
for magician in magicians:
    print((magician.title()) + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

magicians = ['alice', 'lavid', 'carolina']
for magician in magicians:
    print((magician.title()) + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")


# Try it yourself

# 4-1 Pizza
pizzas = ['meat lover', 'mushroom', 'buffalo chicken']
for pizza in pizzas:
    print("My favorite pizza is " + pizza.title() + " pizza!!!")
print("I love pizza so so much!!!")

# 4-2 Animals
animals = ['mouse', 'dog', 'cat']
for animal in sorted(animals):
    print(animal)

animals = ['mouse', 'dog', 'cat']
for animal in sorted(animals):
    print(animal.title() + ' would make a great pet.')
print('All this animals that I lived with lol')

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,13):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
z=sum(digits)
print(min(digits))
print('Summery: ' + str(z))

squares = [value**2 for value in range(1,11)]
print(squares)

z = [value/2 for value in range(2,17,2)]
print(z)
print('\n')
# Try it yourself
# 4-3 Counting to Twenty:
numbers = [number for number in range(1,21)]
print(numbers)
print('\n')
# 4-4 One million(100)
numbers = [number for number in range(1,101)]
print(numbers)
print('\n')

# 4-5. Summing a Million(100)
numbers = [number for number in range(1,101)]
print(numbers)
print('Minimum ' + str(min(numbers)))
print('Maximum ' + str(max(numbers)))
print('Summary ' + str(sum(numbers)))
print('\n')

# 4-6. Odd Numbers
for number in range(1,21,2):
    print(number)

numbers = [number for number in range(1,21,2)]
print(numbers)
print('\n')

# 4-7. Threes
for tree in range(3,30):
    print(tree*3)

trees = [tree*3 for tree in range(3,30)]
print(trees)
print('\n')
# 4-8 Cubes
for cube in range(1,11):
    print(cube**3)
print('\n')

cubes = [cube**3 for cube in range(1,11)]
print(cubes)
# Working with Part of a List
print('\n')
print('\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print('\n')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# slicing specific players from the list of players 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[0:3]:
    print(player)
# slicing specific players from the list of players into a new list of new_players
new_players = [player for player in players[:3]]
print(new_players)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print('\n')

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Try it yourself

# 4-10 Slices
numbers = [number for number in range(1,21,2)]
print(numbers)
print("The first 3 items in the list are " + str(numbers[:3]))
middle = max(numbers)/min(numbers)
print("item from the middle of the range is  " + str(middle))
print("Some from the middle " + str(numbers[4:-3]))
print("The last 3 items in the list are " + str(numbers[-3:]))

# 4-11. My Pizzas, Your Pizzas
pizzas = ['meat lover', 'mushroom', 'buffalo chicken']
friends_pizzas = pizzas[:]
pizzas.append('cheesy')
friends_pizzas.append("herring")
print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(str(pizza) + " pizza.")

print("\nMy friend’s favorite pizzas are: ")
for pizza in friends_pizzas:
    print("\t" + str(pizza) + " pizza.\n")

# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print('\n')
print('\n')
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
print('\n')
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
print('\n')
# Try it yourself
# 4-13 Buffet
buffet = ('rice', 'pasta', 'mashed potatoes', 'grilled chicken', 'mushrooms')
for food in sorted(buffet, reverse = True):
    print(food)
print('\n')
print(sorted(buffet))
print('\n')
buffet= ('avocado', 'french fries', 'rice', 'pasta', 'mashed potatoes', 'grilled chicken', 'mushrooms')
for food in sorted(buffet):
    print(food)
print('\n')
