#In this chapter you’ll learn about the different
#kinds of data you can work with in
#your Python programs. You’ll also learn how
#to store your data in variables and how to use
#those variables in your programs.

message = "Hello World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

#Strings

"This is a string"
'This is a string as well'

'I told my friemd,"Python is my favorite language!"'
"THe language 'Python' is named after Monty Python, not the snake."
"One of Python's strenghts is it's diverse and supportive community"

name = 'ada lovelace'
print(name.title())

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

print('\n')
print(full_name.title)


print('Hello, ' + full_name.title() + '!')

message = 'Hello, ' + full_name.title() + '!'
print('\n' + message)

print("Python")
print('\tPython')

print('hello')

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)


#Try it yourself

#2-3
name = "Jack"
print("\nHello " + name + ' would you like to learn some Python today?')

#2-4
name_1 = 'dima'
print('\n' + name_1.title())
print(name_1.upper())
print(name_1.lower())

#2-5

author = "James Cameron"
quote = "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
print(author.title() + "- '" + quote.lower() + "'")

# 2-6
author = "James Cameron"
quote = "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
result = author.title() + "- '" + quote.lower() + "'"
print('\n' + result)

# 2-7
first_name = ' mark'
last_name = 'twen '
name = first_name + last_name
print('Hello' + name)
print('Hello' + name.lstrip())
print('Hello' + name.rstrip())
print('Hello' + name.strip())

## Numbers

d = 2 + 3
print(d)
d = 2 ** 3
print(d)

z = 0.1 +0.3
print(z)


age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

favorite_number = 3
print('my favorite number is ' + str(favorite_number))