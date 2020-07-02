# def greet_user():
#     """Display a simple greeting."""
#     print("Hello user!")
# greet_user()
# print('\n')
# #def greet_nuser(name,last_name):
# #    """Display a simple greeting."""
# #    print("Hello " + name + " " + last_name + ".")
# #name = input("Please enter your name: ")
# #last_name = input("Please enter your last name: ")
# #greet_nuser(name,last_name)

# print('\n')

# def greet_user(username):
#     """Display a simple greeting."""
#     print("Hello, " + username.title() + "!")
# greet_user('mike')
# print('\n')

# #8-1. Message: Write a function called display_message() that prints one sentence
# #telling everyone what you are learning about in this chapter. Call the
# #function, and make sure the message displays correctly.
# def display_message():
#     """simple message"""
#     print("I'm learning about functions in the moment")
# display_message()

# #8-2. Favorite Book: Write a function called favorite_book() that accepts one
# #parameter, title. The function should print a message, such as One of my
# #favorite books is Alice in Wonderland. Call the function, making sure to
# #include a book title as an argument in the function call.
# def favorite_book(title):
#     """printing favorite book"""
#     print("My favorite book is  " + title.title())
# favorite_book("Alice in Wonderland")
# print('\n')


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet('crocodile', 'jimmy')
# describe_pet(pet_name = "Max",animal_type = "rat")
# print('\n')


# def describe_pet(pet_name,lucky_number="one", animal_type='dog'):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + "and it's lucky number is: " + lucky_number + ".")
# describe_pet(pet_name='willie')
# print('\n')
# #8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# #text of a message that should be printed on the shirt. The function should print
# #a sentence summarizing the size of the shirt and the message printed on it.
# #Call the function once using positional arguments to make a shirt. Call the
# #function a second time using keyword arguments.

# def make_shirt(size,tshirt_text):
#     """Print size amd chose text for the tshirt order"""
#     print(" You ordered T-shirt size: " + size.upper() + " and asked to print text on it: " + tshirt_text.capitalize())
# make_shirt(size = "xl", tshirt_text = "Message")
# print('\n')

# #8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# #by default with a message that reads I love Python. Make a large shirt and a
# #medium shirt with the default message, and a shirt of any size with a different
# #message.
# def make_shirt(size="large",tshirt_text="I love Python"):
#     """Print size amd chose text for the tshirt order"""   
#     print(" You ordered T-shirt size: " + size.capitalize() + " and asked to print text on it: " + tshirt_text)
# make_shirt()
# make_shirt(size="Medium")
# make_shirt(size="Small",tshirt_text="I love Frogs")

# print('\n')
# #8-5. Cities: Write a function called describe_city() that accepts the name of
# #a city and its country. The function should print a simple sentence, such as
# #Reykjavik is in Iceland. Give the parameter for the country a default value.
# #Call your function for three different cities, at least one of which is not in the
# #default country.
# def describe_city(city_name,country):
#     """Name of the city and in which country it's located"""
#     print('\nI love ' + city_name)
#     print('But ' + city_name + ' located in ' + country + '.')
#     print("and because of the covid19 there is no direct flies to " + country + '.')
# describe_city(city_name="Reykjavik",country="Iceland")
# print('\n')
# print('\n')
# #Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# print('\n')
# print('\n')
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# print('\n')
# print('\n')
# def build_person(first_name, last_name, age = ''):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age= 27)
# print(musician)


#Makinga album
# def make_album(artist_name,album_title,track_number = ""):
#   """duild a dictionary from given info"""
#   album = {"Artist_name": artist_name,"album_title": album_title}
#   if track_number:
#     album['number of tracks'] = track_number
#   return album

# album_promt = "what is the albums name: "
# artist_name_prompt = "What is the artist name: "
# track_prompt = "How many track does it have: "

# print("\n What is the album info: ")
# print("When you want to stop at any moment type: q.")

# while True:
#   album_name= input(album_promt)
#   if album_name == 'q':
#     break
#   artist_name=input(artist_name_prompt)
#   if artist_name == 'q':
#     break
#   track_num=input(track_prompt)
#   if track_num == 'q':
#     break
#   print(make_album(album_name,artist_name,track_num))


# def greet_users(names):
#   """Print a simple greeting"""
#   for name in names:
#     msg = " Hello, " + name.title() + "!"
#     print(msg)
# usernames = ["hannah", "ty","margot"]
# greet_users(usernames)


# unprinted_designs = ["iphone case",'dodecahedron',"robot pendant"]
# completed_models = []

# #simulate printing each design,untin none are left
# #Move each design to complete_models after printing

# while unprinted_designs:
#   current_design = unprinted_designs.pop()
#   #simulate printing
#   print("Print model: " + current_design)
#   completed_models.append(current_design)

# #Display all completed models
# print('\nThe following models have been printed: ')
# for completed_model in completed_models:
#   print(completed_model)

def print_models(unprinted_designes,completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        #Simulating creating a 3d print
        print("Printing model: " + current_design.upper())
        completed_models.append(current_design)

def show_completed_models(complete_models):
    """ Show all the printed models"""
    print("\nThe following models have been printed:")
    for complete_model in complete_models:
        print(complete_model.capitalize())

unprinted_designes = ['iphone case', 'galaxy s10 case', 'fruit bowl']
completed_models = []
print_models(unprinted_designes,completed_models)
show_completed_models(completed_models)