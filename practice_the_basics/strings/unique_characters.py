from collections import Counter

# --------------
def unique_chars(word):
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

# --------------
def unique_chars_(word):
    c = {}
    for x in word:
        c[x] = c.get(x,0)+ 1 
    return c

# --------------
def unique_chars__(word):
    c = Counter(word)
    return c

# --------------
def unique_chars(word):
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

# --------------
def build_dict(word):
    c = dict()
    for x in word:
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
    return c 

def unique(unique_dict):
    for ch in unique_dict:
        if unique_dict[ch] == 1:
            return ch
    return None

def unique_chars___(word):
    return unique(build_dict(word))

# --------------
def unique_char(string):
    c = {}
    for ch in string:
        c[ch] = c[ch] + 1 if ch in c else 1

# {'b': 1, 'a': 3, 'n': 2}


















