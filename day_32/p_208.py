from logging import root


class TrieNode():
    def  __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        current = self.root
        
        for character in word:
            

    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        