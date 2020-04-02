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



