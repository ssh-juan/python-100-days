#Functions with Outputs
#Functions which allows you to have an output once the function is completed

#Function to make all first letters of input into Capital Letters.
def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()

    return f"{first_name} {last_name}"

formatted_name = format_name("juAN","borGeS")
print(formatted_name)