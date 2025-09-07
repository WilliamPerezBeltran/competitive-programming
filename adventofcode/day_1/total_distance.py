WORDLIST_FILENAME = "data.txt"

a = list()
b = list()
with open(WORDLIST_FILENAME,'r') as infile:
    for line in infile:
        z = line.split()
        a.append(int(z[0]))
        b.append(int(z[1]))

aco = 0
while a and b:
    z = min(a)
    y = min(b)
    aco += abs(z-y)
    a.remove(z)
    b.remove(y)
    
print(aco)
