inputString = "hi dee hi how are you mr dee"
wordCount = dict() # Creates a new, empty dictionary to hold keys:inputs

def countTheseWords(x): # Defines the function "countTheseWords"
    words = x.split() # Splits the input into a list (words) by individual item

    for i in words:
        if i in wordCount:
            wordCount[i] += 1 # Checks to see if i is in the dictionary, increments it by 1
        else:
            wordCount[i] = 1
    return wordCount # Essential to getting a print statement with counts

print(countTheseWords(inputString))
