guests = ['dima', 'jack', 'mike']
guests.insert(0, 'Kate')
guests.insert(3, 'Jane')
guests.insert(-1, 'Sam')
print("Hello " + guests[0].title() + ', come to our new, bigger table.')
print("Hello " + guests[1].title() + ', come to our new, bigger table.')
print("Hello " + guests[2].title() + ', come to our new, bigger table.')
print("Hello " + guests[-3].title() + ', come to our new, bigger table.')
print("Hello " + guests[-2].title() + ', come to our new, bigger table.')
print("Hello " + guests[-1].title() + ', come to our new, bigger table.')



numbers = [number for number in range(1,21,2)]
print(numbers)
middle = max(numbers)/min(numbers)
print(middle)