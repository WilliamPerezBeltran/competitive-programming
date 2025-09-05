"""
1.Ask the user for their name and print how many letters it has.
2.Convert a sentence to uppercase, lowercase, and title case.
3.Given the word "radar", check if it is a palindrome.
4.Count how many times the letter "a" appears in the string "banana".
5.Replace all spaces in a sentence with underscores.
6. Reverse a string without using slicing. Do it with a loop.
7. Split a sentence into words and sort them alphabetically.
8. Join a list of words into one string separated by commas.
9. Create a function that takes a string and returns only the unique characters.
10. Remove spaces at the beginning and end of the string " Python ".
11. Write a function that takes a sentence and returns the longest word.
12. Check if two words are anagrams, for example "listen" and "silent".
13. Count how many vowels a sentence has.
14. Encrypt a word using Caesar cipher, shifting letters by n positions.
15. Convert a number into text, for example 123 becomes "one two three".
"""


# 1.Ask the user for their name and print how many letters it has.
def name(name):
    return len(name)

# 2.Convert a sentence to uppercase, lowercase, and title case.
def sentence(sentence):
    return sentence.title()

# 3.Given the word "radar", check if it is a palindrome.
def palindrome(word):
    return word == word[::-1]

# 4.Count how many times the letter "a" appears in the string "banana".
def many_times(word):
    return word.count("a")

# 5.Replace all spaces in a sentence with underscores.
def replace_sentence(sentence):
    return sentence.replace(" ","_")

# 6. Reverse a string without using slicing. Do it with a loop.
def reverse_string(s):
    return "".join([s[x] for x in range(len(s)-1,-1,-1)])

# 7. Split a sentence into words and sort them alphabetically.
def split_order(sentence):
    return sentence.split().sort()

# 8. Join a list of words into one string separated by commas.
def join_sentence(sentence):
    return ","join(sentecen)

# 9. Create a function that takes a string and returns only the unique characters.
def unique_characters(string):
    c = {}
    for x in word:
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
    for ch in c:
        if c[ch] == 1:
            return ch
    return None

# 10. Remove spaces at the beginning and end of the string " Python ".
def split_order(sentence):
    return sentence.strip()

# 11. Write a function that takes a sentence and returns the longest word.
def split_order(sentence):
    mayor_len = None   
    for x in sentence:
        if len(x) > mayor:
            mayor_len = len(x)
            mayor = x

    return sentence.split().sort()

# 12. Check if two words are anagrams, for example "listen" and "silent".
def split_order(sentence):
    return sentence.split().sort()

# 13. Count how many vowels a sentence has.
def split_order(sentence):
    return sentence.split().sort()

# 14. Encrypt a word using Caesar cipher, shifting letters by n positions.
def split_order(sentence):
    return sentence.split().sort()

# 15. Convert a number into text, for example 123 becomes "one two three".
def split_order(sentence):
    return sentence.split().sort()






























