## List
#A list is a collection of items in a particular order.

bycicles = ['trek', 'cannodale', 'redline', 'specialized']
print(bycicles)
print(bycicles[0])
print(bycicles[0].title())
print(bycicles[1])
print(bycicles[3])
print(bycicles[-1])

message = " My first bycicle was a " + bycicles[1].title() + '.'
print(message.upper())
print(message)

# Try it yourself
#3-1
names = ['dima', 'jack', 'roger']
print(names[0].title())
print(names[1].title())
print(names[-1].title())

#3-2
print("Hello dear " + names[0].title() + ", please come in.")
print("Hello dear " + names[1].title() + ", please come in.")
print("Hello dear " + names[2].title() + ", please come in.")
print("Hello dear " + names[-3].title() + ", please come in.")

#3-3
cars = ['new', 'used']
print('I like ' + cars[0] + " cars but I only can afford " + cars[1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

