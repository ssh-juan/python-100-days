# Function with Multiple Inputs
# Positional Arguments vs Keyword Arguments
# You can have multiple inputs in functions.
# All you need to do is separate then with a comma ','.

def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

print("----Positional Arguments----")
greet_with("Juan","Osasco")
greet_with("Osasco","Juan")

print("\n----Keywords Arguments----")
greet_with(name="Juan",location="Osasco")
greet_with(location="Osasco",name="Juan")