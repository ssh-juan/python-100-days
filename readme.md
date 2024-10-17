# My Studies about Python
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
- ROUND A NUMBER = `round(number, ndigits)`  
- CONVERT TO LOWERCASE = `.lower()` (Example: `input().lower()`)  
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