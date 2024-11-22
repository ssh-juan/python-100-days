# My Python Studies
Following [Angela Yu's Course](https://www.udemy.com/course/100-days-of-code/)

### "Our brain is for thinking, not for storing"

### Python Primitive Data Types
1. Strings
2. Integers
3. Floats
4. Booleans

## Main Functions
- PRINT = `print()`
- PRINT FORMATTED (f-Strings)= `print(f"I am {age} years old")`
- INPUT = `input()`  (Obs.: the input will always be a String)
- LENGTH = `len()`  
- TO INT = `int()`  
- TO STR = `str()`  
- TO FLOAT = `float()`  
- TO BOOLEAN = `bool()`  
- COUNT - `count()`
    - Return the number of times the value appears in the **list**.
```python
#Counts how many times '9' appears in the list
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
```
- ROUND A NUMBER = `round(number, ndigits)`  
- CONVERT TO LOWERCASE = `.lower()` (Example: `input().lower()`)  
- CONVERT FIRST LETTERS TO CAPITAL LETTERS = `.title()` (Example: `input().title()`)  
- Lists - `fruits = [item1, item2]`
- ADD ONE ITEM IN A LIST = `.append()` (Example: `states_of_usa.append("New Jersey")`)
- ADD SOME ITEMS IN A LIST = `.extend()` (Example: `states_of_usa.extend(["Georgia","Connecticut"])`)
    - **List x Array** = A List is more flexible and can have multiple types of data (int, str, float, etc). An array is more restricted and can only have one type of data.
```python
#Indentation is crucial in Python for conditionals
if condition:
    do this
else:
    do this
```
```python
#Indentation is crucial in Python for conditionals
if condition:
    do this
elif another condition:
    do this
else:
    do this
```
- FOR LOOPS - There are 2 types of 'for' loops: 'for' using lists and 'for' using range
1. FOR LISTS
```python
for item in list_of_items:
    #do something
    #for the 'item', we give a name for a single item
```
2. RANGE - `range(a, b, c)`
    - Creates a range from 'a' to 'b' (obs.: **NOT INCLUDING** the last number 'b'). Has to be used in conjunction with another function.
    - 'c' is optional. Is a "step" function that will jump characters from the number you input in.
        - Example: `range(1, 10, 3)` - It will steps 3 by 3. Result will be: `1, 4, 7, 10`

  - FOR LOOP WITH RANGE
```python
for number in range(a, b)
    print(number)
```
- SUM - `sum()`
    - Get the sum from a List
- MAX - `max()`
    - Get the maximum value from a List
- `def` - Defining Functions
    - [Functions Documentation](https://docs.python.org/3/library/functions.html)
```python
def my_function():
    #Do this
    #Then do this
    #Finally do this
```
- Functions with Inputs
    - In the example below `something` is the **Parameter**, and it's value inputted is **Argument** (the value of data)
```python
def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this
```
- Functions with Multiple Inputs
```python
def my_function(a, b, c):
    #Do this with 'a'
    #Then do this with 'b'
    #Finally do this 'c'
```
- Functions with Outputs
    - Functions which allows you to have an output once the function is completed.
```py
def my_function():
    result = 3 * 2

    return result
```
- WHILE LOOP
```python
while something_is_true:
    #do something repeatedly
```
- FOR LOOP x WHILE LOOP:
    - FOR LOOPS: Really good when you need to iterate over something and you need to do something with **EACH THING** that you're iterating over.
    - WHILE: Good to just simply wants to carry out a functionality until a certain condition.
        - While loops are more dangerous, due to possible Infinite Loops.

## Mathematical Operators
- ADDITION: `+`  
- ADDITION OF ACTUAL VALUE: `+=`  
- SUBTRACTION: `-`  
- SUBTRACTION OF ACTUAL VALUE: `-=`  
- MULTIPLICAÇÃO: `*`  
- DIVISÃO: `/` (sempre vai ser 'float')  
- DIVISÃO: `//` (remove todas as casas após a vírgulas, vira um 'int')  
- POTENCIAÇÃO: `**`  
- REMAINDER: `%` (Check the remainder, how many is remaining after that division)  
- MODULO EQUALS - `%=`

## Conditional Operators
- AND - `and`  
- OR - `or`  
- NOT - `not`  

## Comparison Operators
| Operator | Meaning |
| --- | --- |
| > | Greater Than |
| < | Less Than |
| >= | Greater than or Equal to |
| <= | Less than or Equal to |
| == | Equal to |
| != | Not Equal to |

## Dictionaries
- Structure - Key: Value
```py
empty_dictionary = {}
```

## Main Libraries Used
- `random` - Randomisation
    - RANDOM CHOICE ON A LIST = `random.choice(list_name)`
    - RANDOM INTEGER = `random.randint(a, b)` Range from 'a' to 'b'
    - RANDOM FLOAT INTERVAL = `random.uniform(a, b)` Range from 'a' to 'b'
    - RANDOM FLOAT 0 TO 1 = `random.random()` Range from 0 to 1
    - RANDOM SHUFFLE - `random.shuffle(list_name)` Shuffles the order of the list

## Useful Tips
- There's a tip for an IDE called "Thonny". It helps to debug code easier for newbies.
- [ASCII Art Generator](https://ascii.co.uk/art)

## Projects
1. Band Name Generator
    - Printing, Commenting, Debugging, String Manipulation and Variables
2. Tip Calculator
    - Data Types, Numbers, Operations, Type Conversion, f-string
3. Treasure Island - Game
    - Conditional Statements, Logical Operators, Code Blocks and Scope
4. Rock-Paper-Scissors - Game
    - Randomisation and Python Lists
5. Password Generator
    - For Loops, Range and Code Block
6. Escaping the Maze - Reeborg's World
    - Functions, Code Blocks and While Loops
7. Hangman Project
    - Flow Chart Programming
8. Caesar Cipher
    - Functions with Inputs, Parameters and Arguments
9. [Blind Auction Program](https://github.com/ssh-juan/python-100-days/tree/master/day-09_blind-auction-program)
    - Dictionaries & Nesting
10. [Calculator App](https://github.com/ssh-juan/python-100-days/tree/master/day-10_calculator_app)
    - Functions with Outputs
11. [Blackjack Game](https://github.com/ssh-juan/python-100-days/tree/master/day-11_blackjack)