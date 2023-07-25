import random


class WordFinder:
    """Class that accepts a file and returns a random word from it. The word_list argument has to be the full path to the file
    i.e. user/path/filename"""

    def __init__(self, word_list):
        "Retrieve the file and create the list of words"

        with open(word_list) as file:
            self.words = file.read().splitlines()

        self.total_words = len(self.words)

        print(f'{self.total_words} words read from file')

    def random_word(self):
        "Return a random word from the word list"
        return random.choice(self.words)


wf = WordFinder(
    '<path to file>')

print(wf.random_word())
print(wf.random_word())
print(wf.random_word())
print(wf.random_word())
print(wf.random_word())
print(wf.random_word())
print(wf.random_word())

"""New subclass to handle cases of blank lines or # symbols in the submitted file"""


class SpecialWordFinder(WordFinder):
    """This class is an extension of the WordFinder class that deals with special cases in the file"""

    def __init__(self, word_list):
        "Inherits the parent __init__ function to create the necessary variables"
        super().__init__(word_list)

        # List comprehension which filters out all the blank words or special characters
        self.words = [word for word in self.words if word.isalpha()]


sfw = SpecialWordFinder(
    '<path to file>')

print(sfw.random_word())
print(sfw.random_word())
print(sfw.random_word())
print(sfw.random_word())
print(sfw.random_word())
print(sfw.random_word())
print(sfw.random_word())
