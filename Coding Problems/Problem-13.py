"""Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
    Return the string unchanged if the given string already begins with "Is"."""

Sentence = input()
search = Sentence.find("Is")
if search==0:
    print(Sentence)
else: print("Is " + Sentence)