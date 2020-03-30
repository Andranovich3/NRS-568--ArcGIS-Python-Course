age = raw_input("What is your age? ") # Takes in user input without defining variable type

if str(age).isdigit(): # Checks to see if input is a digit (only works with strings)
    retire = 65 - int(age) # If yes, converts the entered age into a retire distance
    print "You are " + str(retire) + " years from retirement!"
else: # Rejection statement is the entered input is not a digit/number
    print "'" + age + "'" + " is not a number, dummy."
