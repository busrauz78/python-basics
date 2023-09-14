print('Hello this is basics file')
print('This file includes:\nMath Operators\n')

# MATH OPERATORS
print('MATH OPERATORS:')

# ** : Exponent
print('Exponent: 2**5:', 2**5)

# % : Modules/Remainder
print('Remainder of 23 % 7:', 23 % 7)

# // : Integer Division
print('Integer Division of 23 // 7:' ,23 // 7)

# / : Division
print('Division of 21 / 2:', 21 / 2)

# * : Multiplication
print('Division of 5 * 3:', 5 * 3)

# - : Subtraction
print('Division of 6 - 8:', 6 - 8)

# + : Addition
print('Division of 7 + 9:', 7 + 9)

print('\n')

# AUGMENTED ASSIGNMENT OPERATORS
print('AUGMENTED ASSIGNMENT OPERATORS:')

index = 10
print('Let\'s say index = 10')
index +=1
print('index+=1:', index)
index = 10
index -=1
print('index-=1:', index)
index = 10
index *=2
print('index*=2:', index)
index = 10
index /=2
print('index/=2:', index)
index = 10
index %=2
print('index%=2:', index)

greeting = 'Hello'
print('Let\'s say greeting = "Hello"')
greeting+= " World"
print('greeting+= " World" is:', greeting)

items=['item']
print('Let\'s say items=["item"]')
items *=3
print('items*=3 is:', items)

print('\n')
# END KEYWORD
print('END KEYWORD:')
phrases = ['printed', 'with', 'a', 'dash', 'in', 'between']
print('Let\'s say we have this array: phrases = ["printed", "with", "a", "dash", "in", "between"] and if we want to travel all array items with end operator')
for phrase in phrases:
  print('Phrase:', phrase, end=' END\n')
print('\n')

#SEP KEYWORD
print('SEP KEYWORD:')
print('If we want to print elements with comma:')
print('item1', 'item2', 'item3', sep=',')
print('\n')

#INPUT FUNCTION
print('INPUT FUNCTION:')
my_name = input('Hello! What is your name?')
print(f'Hello {my_name}. How are you?')
print('\n')

#LEN FUNCTION
print('LEN FUNCTION:')
print('Let\'s say we have this array: items=["item", "item", "item"]')
items=["item", "item", "item"]
print('Length of items array:', len(items))
print('Even we can calculate the length of the first element of that array:', len(items[0]))
print('\n')

#str, int, float FUNCTIONS
print('str, int, float FUNCTIONS:')
print('Let\'s make a string from any number: str(40)', str(40))
print('Let\'s make a integer from any string: int("40")', int('40'))
print('Let\'s make a float from any string: float("3.14")', float('3.14'))

print('\n')