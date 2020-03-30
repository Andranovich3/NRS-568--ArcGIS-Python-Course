scrabbleScores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}

def wordScore(x): # Define the function that will calculate the score
    score = 0 # Set score to zero each time to prevent overscoring
    for letter in x:
        letter = letter.lower() # Converts the letter to lowercase (like the dictionary) to avoid missing a score
        score = score + scrabbleScores[letter] # Increments the score based on the letter's point value
    return str(score) # Essential for print message

scrabbleWord = raw_input("Please enter a legal Scrabble word: ")

if scrabbleWord.isdigit(): # Checks to see if the input is a number instead of a word
    print "'" + scrabbleWord + "'" + " is not a word, dummy."
else:
    print "Your score is: " + wordScore(scrabbleWord)
