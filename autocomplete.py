# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].


# pseudocode
# - add word:
# -pefrorm linear serch over word
#  
class TrieNode:
    __slots__ = ['value', 'children', 'is_word', 'weight']
    def __init__(self, value:str='', is_word=False):
        self.value = value
        self.children = {}
        self.is_word = is_word
        self.weight = -1

    def add(self, word_part, weight: int=-1):
        if len(word_part) == 0:
            self.is_word = True
            self.weight = weight
            return
        first_char = word_part[0]
        # return xisted or create new hash
        node = self.children.setdefault(first_char, TrieNode(first_char))
        node.add(word_part[1:], weight)

    def find_all(self, word_part, path=""):
        if self.is_word:
            yield path + self.value, self.weight
        if len(word_part) > 0:
            char = word_part[0]
            node = self.children.get(char)
            if node is not None:
                yield from node.find_all(word_part[1:], path + self.value)
        else:
            for node in self.children.values():
                yield from node.find_all("", path + self.value)

cl = TrieNode()
cl.add('king')
cl.add('kind')
cl.add('klue')
for word, weight in cl.find_all('ki'):
    print(word)

            
