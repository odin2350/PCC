# if Statements
cars = ['audi', 'Bmw', 'subaru', 'toyota']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title()) 

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!\n")

# check later
#answer = input()
#if answer != 42:
#    print("That is not the correct answer. Please try again!")
#else:
#    print("That's the right answer")
 
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print('You can come in in the bar.')
else:
    print("your group can't come in.")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('your pizza is on the way\n')

#banned_users = ['andrew', 'carolina', 'david']
#user = input()
#if user not in banned_users:
#    print(user.title() + ", you can post a response if you wish.")
#else:
#    print(user.title() + " sorry but you are banned, please speak with administrator")

# Try it yourself
# 5-1

fruit = 'tomatoe'
print("Is fruit == 'tomatoe'? I predict True.")
print( fruit == 'tomatoe')
print("is fruit == 'cucamber'? I predict false")
print(fruit == 'cucamber')

fruits = ['tomatoe', 'banana', 'apple']
if 'apple' in fruits:
    print('Yeah it is a fruit')

#fruits = ['tomatoe', 'banana', 'apple']
#selected = str(input())
#if selected not in fruits:
#    print('Yeah ' + selected.lower() + ' is not a fruit')
#else:
#    print("yep " + selected.lower() + " is a fruit")

# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.

age= 12
if age < 4:
    print("Your admision cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 21
if age < 4:
    price = 0
elif age < 18:
    priee = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + '.')


age = 120
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age >= 120:
    price = "Congrats on being the oldest customer, administration is coming to check your id"
elif age >= 65:
    price = 5
else:
    price = 10
if age in range(0,120):
    print("Your admission cost is $" + str(price) + '.')
else:
    print(price)
print('\n')

#trying if with for loop
requested_toppings = ['mushrooms', 'extra cheese']
for topping in requested_toppings:
    if topping in requested_toppings:
        print("Adding " + topping)
print("Your order is in the oven.")
print('\n')

# checking if condition one by one
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")      
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Your order is in the oven." + '\n')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("Finished making your pizza!"+ '\n')

# But what if the pizzeria runs out of green peppers
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!" + '\n')

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?" + '\n')

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Finished making your pizza!" + '\n')

# Try it yourself
# 5-8 Hello Admin
usernames = ['user_1', 'user_2','mike','allan', 'cat', 'admin']
for user in usernames:
    if user == 'admin':
        print("Hello boss")
    else:
        print("Greetings " + str(user.title()) + " fellow human")
print('\n')

#5-9 no users
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello boss")
        else:
            print("Greetings " + str(user.title()) + " fellow human")
else:
    print('I need to find more fellow humans')
print('\n')

# 5-10  Checking Usernames
current_users = ['user_1', 'user_2','mike','allan', 'cat', 'admin']
new_users = ["user_3",'admin','user_5','USER_2']
for new_user in new_users:
    if str(new_user).lower() in str(current_users).lower():
        print(new_user + ' You need to enter a new user name')
    else:
        print(new_user + ' You can register this user name.')


