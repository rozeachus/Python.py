"""From code academy:

scrabble_score
Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).

To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values."""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  count = 0
  for w in word: 
    count = count+score[w.lower()]
  return count

print scrabble_score("nuts")
  
"""Here is my explanation
Well, score needs no explanation, was already there

def scrabble_score(word): > this start our function, and put one parameter: word

count=0 > this sets the variable count to an int, and in fact, 0

for w in word > this will pass each letter in the word

count = count + score[w.lower()] > w.lower will convert the letter to lowercase, that way we can put the correct score and dodge any errors. score[i.lower()] will go look trough our list, score, with i as the letter. It then takes the number and add it to our total.

return count > this will return our variable

print scrabble_score ("POTATOES") > this is my own test with all caps to be sure it works."""
