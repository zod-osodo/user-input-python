# user_input.py

# Ask for user's name and store it in a variable called "name"
name = input("What is your name? ")

# Ask for user's age and store it in a variable called "age"
age = input("How old are you? ")

# Ask for user's location and store it in a variable called "location"
location = input("Where do you live? ")

# Print out a personalized message using the user's name, age, and location
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))