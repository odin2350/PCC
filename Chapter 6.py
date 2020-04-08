# Dictionaries
alien_0 = {'color': 'green', 'points': 5}
print("alien 0 color: " + alien_0['color'])
print("points for alien_0: " + str(alien_0['points']))
print('\n')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages)
print('\n)')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
 favorite_languages['sarah'].title() +
  ".")
print('\n')
  # Try it yourself
  # 6-1 Person
person = {
    'first_name': 'mike',
    'last_name': 'kuzov',
    'age': '50',
    'city': 'brooklyn'
    }
print(person['first_name'].title() +
 " " +
  person['last_name'].title()) 
print('\n')

print(
    person['first_name'].title() +
    " " +
    person['last_name'].title() +
    " is from " +
    person['city'].title() +
    ' and he is ' +
    person['age'] +
    " years old."
)
print('\n')
# 6-2 Favorite Numbers
favorite_numbers = {'mike': 3, 'G': 15, 'Z': 9}
for name in favorite_numbers:
  print(name.title() + "'s favorite number is " + str(favorite_numbers[name]))
print('\n')

lucky_numbers = {
    "mike": 3,
    'allan': 4,
    'alex': 1}
for lucky in lucky_numbers:
    if lucky == 'mike':
        print("Mike's lucky number is: " + str(lucky_numbers['mike']))
    elif lucky == 'allan':
        print("Allan's lucky number is: " + str(lucky_numbers['allan']))
    elif lucky == 'alex':
        print("Alex's lucky number is: " + str(lucky_numbers['alex']))
print('\n')
lucky_numbers['joey'] = '2'
print(lucky_numbers)
print('\n')
#creating the loop that go thru dictionary first value 'key_word' call for key in the dictionary
#key word goes in the loop thru dictionary test
#When call for the key_word we get the 'Key'
# when need value call for dictionary + key test[key_word] where key word is the key in the loop
test = {'key': 1, 'house': 2}
for key_word in test:
    print(key_word.title() + " value: " + str(test[key_word]))
    print(test[key_word])
    print(key_word)