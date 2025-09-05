
class LoadFile():
    WORDLIST_FILENAME = "words.txt"
    def load_words(self):
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(self.WORDLIST_FILENAME, 'r')
        # line: string
        line_string = inFile.readline()
        print("  ", len(line_string), "words loaded.")
        return line_string 

# x = LoadFile()
# print(x.load_words())
