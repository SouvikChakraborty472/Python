"""Write a Python program to test whether a passed letter is a vowel or not."""

text = input()
for element in text:
    if element in ('a','e','i','o','u','A','E','I','O','U'):
        print("text contain vowel")
        break
    print("text contain consonant")
    break