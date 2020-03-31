# methods
Every method is followed by a set of ( ) parentheses,
because methods often need additional information to do their work.
That information is provided inside the parentheses.

- .title() 
The title( ) function doesn’t need any additional information, so its parentheses are empty

- .upper( )
- .lower( )
- .rstrip( ) removeswhite white space at the end of the str
- .lstrip( ) on the left
- .strip() from both sides

## brakers
- \n new line
- \t add tab

## List
- square brackets [ ] indicate a list, and individual elements
in the list are separated by commas.

## Appending Elements to the End of a List
list.append('what you want to append)

## Inserting Elements into a List
You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

## Removing an Item Using the del Statement
If you know the position of the item you want to remove from a list, you can
use the del statement.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

## Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

## Removing an Item by Value
If you only know the value of the item you want to remove, you
can use the remove() method.
The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop to
determine if all occurrences of the value have been removed.

## Sorting a List Permanently with the sort() Method
Python’s sort() method makes it relatively easy to sort a list. Imagine we
have a list of cars and want to change the order of the list to store them
alphabetically. To keep the task simple, let’s assume that all the values in
the list are lowercase.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

### in reverse alphabetical order
cars.sort(reverse=True)

## Sorting a List Temporarily with the sorted() Function
To maintain the original order of a list but present it in a sorted order, you
can use the sorted() function. The sorted() function lets you display your list
in a particular order but doesn’t affect the actual order of the list.

print(sorted(cars))

## Printing a List in Reverse Order
To reverse the original order of a list, you can use the reverse() method.
reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list

## Finding the Length of a List
You can quickly find the length of a list by using the len() function.
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)


## Looping Through an Entire List

for loop

plural_object_name = [list]
FOR single_object_name IN plural_object_name:
    print(single_object_name)

## Using the range() Function
Using the range() Function
Python’s range() function makes it easy to generate a series of numbers.
For example, you can use the range() function to print a series of numbers
like this:
    for value in range(1,5):
        print(value)

## Using range() to Make a List of Numbers
If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers.
In the example in the previous section, we simply printed out a series of
numbers. We can use list() to convert that same set of numbers into a list:
numbers = list(range(1,6))
print(numbers)\

## Even numbers range
even_numbers = list(range(2,11,2))
print(even_numbers)

