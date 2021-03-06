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
    
# Looping Through a Dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
#book
for key, value in user_0.items():
  print('\nKey: ' + key)
  print("Value: " + value)
#simple loop, by default return key can specify user_0.keys()
for keyValue in user_0:
    print("\nKey: " + keyValue)
    print("Value: " + user_0[keyValue])


favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',    }
for name, language in favorite_languages.items():
   print(name.title() +
         "'s favorite language is " +
          language.title() + ".")

#the same
for name in favorite_languages.keys():
  print(name.title())
print('\n') 

for person in favorite_languages:
    print(person.title())

favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(name.title())
  if name in friends:
     print("  Hi " + name.title() +
           ", I see your favorite language is " +
          favorite_languages[name].title() + "!")

# The keys() method isn’t just for looping: It actually returns a list of all the keys,
#and the line at simply checks if 'erin' is in this list.
#Because she’s not, a message is printed inviting her to take the poll:
if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")
print('\n')
favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',    }
for name in sorted(favorite_languages.keys(), reverse= True):
  print(name.title() + ", thank you for taking the poll.")
print('\n')

for name in sorted(favorite_languages.values()):
  print(name.title())
print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
test_2 = []
for test in favorite_languages.values():
    if test not in test_2:
        test_2.append(test)
print(test_2)
print(favorite_languages)
print('\n')

favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',    }
test3 = []
for name in sorted(favorite_languages.keys()):
    if name not in test3:
        test3.append(name)
    print(name.title())
print(str(test3).title())
print('\n')

# Try it yourself
# 6-4 Glossary 2
terms = {
    'python': 'programming language',
    'loop':'form (something) into a loop or loops; encircle.',
    'string':'In programming, a string is a contiguous (see contiguity) sequence of symbols or value',
    'integer': 'Integers are a commonly used data type in computer programming. For example, whenever a number is being incremented, such as within a "for loop" or "while loop," an integer is used.',
    'boolean':'In mathematics and mathematical logic, Boolean algebra is the branch of algebra in which the values of the variables are the truth values true and false,usually denoted 1 and 0 respectively.',
    }
for word,meaning in terms.items():
    print(word.title() + ' : ' + meaning.lower())
print('\n')

terms['java'] = 'programming language'
terms['c'] = 'programming language'
terms['microsoft'] = 'company'
terms['linux'] = 'OS'
terms['os'] = 'operation system'
print("I learned next things:\n")
for word,meaning in terms.items():
  print(word.title() + ": " + meaning.lower() + '\n')

# 6-5
rivers = {
    'amazon': 'south america',
    'yangtze': 'asia',
    'nile': 'egypt',
    'Amur':"egypt"
    }
for river,location in rivers.items():
    print(river.title() + ' runs thru ' + location.title() + ".")
print('\n')
for river,location in rivers.items():
    print("Country : " + location.title())
print('\n')
#6-6

# ask how can I make sure it compare both as lower without removing keys()
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
not_polled = ['mike','jen','joey','sam', 'Phil']
for poll in not_polled:
    if poll.lower() in favorite_languages.keys():
        print(poll + ' thank you for particapation.')
    else:
        print(poll + ' please answer the poll.')
print('\n')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print('\n')
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese']
}
print("Your ordered a " + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')
for topping in pizza['toppings']:
  print('\t' + topping)
print('\n')
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
  if len(languages) > 1:
    print("\n" + name.title() + "'s favorite languages are:")
  else:
      print("\n" + name.title() + "'s favorite language is:")
  for language in languages:
          print("\t" + language.title())


print('\n')
# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'ptincton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}
for username,user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())

print('\n')
# Try it yourself
# 6-7 People use 6-1
#Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live.
#You should have keys such as first_name, last_name, age, and city.
#Print each piece of information stored in your dictionary. 

mike = {
    'first_name': 'mike',
     'last_name': 'kuzov',
      'city': 'brooklyn',
      }
for data,person in mike.items():
  print(data + " " + person)

people = []

person = {
    'first_name': 'mike',
     'last_name': 'kuzov',
      'city': 'brooklyn',
      }
people.append(person)
print(people)

people = [{
    'first_name': 'mike',
     'last_name': 'kuzov',
      'city': 'brooklyn',
      },
      {
    'first_name': 'joey',
     'last_name': 'ronin',
      'city': 'paris',
       },
       {
    'first_name': 'chandler',
     'last_name': 'tribiany',
      'city': 'manhatten',
      }
]
print("here is the list of people that I know: ")
for person in people:
  name = person['first_name'].title() + ' ' + person['last_name'].title()
  city = person['city'].title()
  print(name + ", is from " + city)
# 6-8
pets = []

doggy = {
    'name': 'doggy',
    'breed': 'german shepard',
    'type': 'dog',
    'owner': 'mike'
}
pets.append(doggy)

kitty = {
    'name': 'kitty',
    'breed': 'rare',
    'type': 'cat',
    'owner': 'mary'
}
pets.append(kitty)

john = {
    'name': 'john',
    'breed': 'street',
    'type': 'hamster',
    'owner': 'ricky'
}
pets.append(john)
for pet in pets:
  name = pet['name'].title()
  breed = pet['breed'].lower()
  typez = pet['type'].lower()
  owner = pet['owner'].title()
  print(owner + ' has a ' + breed + ' ' + typez + ' which name is ' + name)
print('\n')
for pet in pets:
  print('\n' + "Here what I know about " + pet['name'].title())
  for key,value in pet.items():
    print(key.title() + ': ' + str(value).title())

