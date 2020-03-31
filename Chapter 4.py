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
new_players = [player for player in players[0:3]]
print(new_players)



