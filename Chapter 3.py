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

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print("\n" + str(motorcycles))
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\n " + too_expensive.title() + " is too expensive for me.")

# Try it yourself

# 3-4 Guest List:

guests = ['dima', 'jack', 'mike']
print("Hello " + guests[0].title() + ', I gonna have a partty tomorow and you are invited.')
print("Hello " + guests[1].title() + ', I gonna have a partty tomorow and you are invited.')
print("Hello " + guests[2].title() + ', I gonna have a partty tomorow and you are invited.')

# 3-5 Changing Guest List:
guests = ['dima', 'jack', 'mike']
not_coming = guests.pop(-1)
print("Hello " + guests[0].title() + ', I gonna have a partty tomorow and you are invited.' + ' Unfortunatly ' + not_coming.title() + " can't make it this time.")
print("Hello " + guests[1].title() + ', I gonna have a partty tomorow and you are invited.' + ' Unfortunatly ' + not_coming.title() + " can't make it this time.")

guests.append('Joe')
print("Hello " + guests[0].title() + ', We are still having a blast tonight.')
print("Hello " + guests[1].title() + ', We are still having a blast tonight.')
print("Hello " + guests[2].title() + ', We are still having a blast tonight.')
# 3-6
print("\n" + str(guests))
guests.insert(0, 'Kate')
guests.insert(3, 'Jane')
guests.append('Sam')
print("Hello " + guests[0].title() + ', come to our new, bigger table.')
print("Hello " + guests[1].title() + ', come to our new, bigger table.')
print("Hello " + guests[2].title() + ', come to our new, bigger table.')
print("Hello " + guests[-3].title() + ', come to our new, bigger table.')
print("Hello " + guests[-2].title() + ', come to our new, bigger table.')
print("Hello " + guests[-1].title() + ', come to our new, bigger table.')

# 3-7
print("Hello guys sorry but we won't be abble to accomodate everyone only me and 2 more people")
print("Hello " + guests.pop() + " sorry but it won't be enough space for you.")
print("Hello " + guests.pop() + " sorry but it won't be enough space for you.")
print("Hello " + guests.pop() + " sorry but it won't be enough space for you.")
print("Hello " + guests.pop() + " sorry but it won't be enough space for you.")
print("what's up " + guests[0].title() + ' see you tonight.')
print("what's up " + guests[1].title() + ' see you tonight.')
print(guests)

# Organizing a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original again:')
print(cars)



