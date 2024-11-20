#Docstrings
#Basically a way for us to create little bits of documentation as we are coding along.

#Should be at the first line after function's declaration
def format_name(first_name, last_name):
    """Take as input "first and last name" and format it
      to return the title case version of the name."""
    first_name = first_name.title()
    last_name = last_name.title()

    return f"{first_name} {last_name}"

formatted_name = format_name("juAN","borGeS")
print(formatted_name)