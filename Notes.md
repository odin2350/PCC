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
- .strip from both sides

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
u motorcycles.insert(0, 'ducati')
print(motorcycles)

## Removing an Item Using the del Statement
If you know the position of the item you want to remove from a list, you can
use the del statement.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
