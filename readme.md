# My Python Studies
![repo logo](<repo_icon.png>)

My Studies Following [Angela Yu's Course](https://www.udemy.com/course/100-days-of-code/).  100 different projects will be built.

All projects are available listed [at the end of this Readme](#Projects).

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
- `try` and `except`
    - `try` - This is where you write the code that could potentially raise an exception.
    - `except` - If an error occurs in the try block, the program jumps here to handle the error instead of crashing.
    
    - Example 1: Handling Division by Zero
python
```py
#Example 1: Handling Division by Zero
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- Example 2: Catching Multiple Exceptions
You can handle different errors with multiple except blocks:
```py
#Example 2: Catching Multiple Exceptions
try:
    number = int("abc")  # This will cause a ValueError
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- Example 3: Generic Exception Handling

If you’re unsure which exception might occur, you can catch all exceptions with a generic except:

```py
#Example 3: Generic Exception Handling
try:
    risky_code()
except Exception as e:
    print(f"An error occurred: {e}")
```

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
- `os` - Operational System
    - Clear terminal (example for Windows)
    ```py
    from os import system
    system("cls")
    ```
- `logging` - Logging
    ```py
    import logging
    
    logging.debug("Debug")
    logging.info("Info")
    logging.warning("Warning")
    logging.error("Error")
    logging.critical("Critical")
    ```

## Useful Tips and Links
- [Easy Debugger - Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
- [Easy Debugger - Thonny](https://thonny.org/)
- [ASCII Art Generator](https://ascii.co.uk/art)
- [Another ASCII Art Generator](https://patorjk.com/software/taag)
- [Emojipedia](https://emojipedia.org/)
- [PyPI - Python Package Index](https://pypi.org/)


## Projects
### Beginner
1. [Band Name Generator](https://github.com/ssh-juan/python-100-days/tree/master/day-01_band_name_generator)
    - Printing, Commenting, Debugging, String Manipulation and Variables
2. [Tip Calculator](https://github.com/ssh-juan/python-100-days/tree/master/day-02_tip_calculator)
    - Data Types, Numbers, Operations, Type Conversion, f-string
3. [Treasure Island - Game](https://github.com/ssh-juan/python-100-days/tree/master/day-03_treasure_island)
    - Conditional Statements, Logical Operators, Code Blocks and Scope
4. [Rock-Paper-Scissors - Game](https://github.com/ssh-juan/python-100-days/tree/master/day-04_rock_paper_scissors)
    - Randomization and Python Lists
5. [Password Generator](https://github.com/ssh-juan/python-100-days/tree/master/day-05_password_generator)
    - For Loops, Range and Code Block
6. [Escaping the Maze - Reeborg's World](https://github.com/ssh-juan/python-100-days/tree/master/day-06_escaping_the_maze_--comeback-after-day-15)
    - Functions, Code Blocks and While Loops
7. [Hangman Project](https://github.com/ssh-juan/python-100-days/tree/master/day-07_hangman_project)
    - Flow Chart Programming
8. [Caesar Cipher](https://github.com/ssh-juan/python-100-days/tree/master/day-08_caesar_cipher)
    - Functions with Inputs, Parameters and Arguments
9. [Blind Auction Program](https://github.com/ssh-juan/python-100-days/tree/master/day-09_blind-auction-program)
    - Dictionaries & Nesting
10. [Calculator App](https://github.com/ssh-juan/python-100-days/tree/master/day-10_calculator_app)
    - Functions with Outputs
11. [Blackjack Game](https://github.com/ssh-juan/python-100-days/tree/master/day-11_blackjack)
12. [Number Guessing Game](https://github.com/ssh-juan/python-100-days/tree/master/day-12_number_guessing_project)
    - Scope: Local Scope and Global Scope
13. [Debugging](https://github.com/ssh-juan/python-100-days/tree/master/day-13_debugging)
14. [Higher or Lower](https://github.com/ssh-juan/python-100-days/tree/master/day-14_higher_or_lower)

### Intermediate
15. [Coffee Machine Project](https://github.com/ssh-juan/python-100-days/tree/master/day-15_coffee_machine)
16. [OOP Coffee Machine Project](https://github.com/ssh-juan/python-100-days/tree/master/day-16_oop_object_oriented_programming)
    - OOP - Object Oriented Programming
17. [Quiz Game](https://github.com/ssh-juan/python-100-days/tree/master/day-17_quiz_game)
    - Creating Classes...+++