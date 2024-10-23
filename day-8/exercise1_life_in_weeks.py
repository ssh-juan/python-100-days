# Life in Weeks

# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# **Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!

def life_in_weeks(age):
    weeks_lived = age * 52
    ninety_years_week = 90 * 52
    
    weeks_left = ninety_years_week - weeks_lived
    
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(23)