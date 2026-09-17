class Node:
    def __init__(self):
        self.children  = {}
        self.end = False
class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        c = self.head
        for i in word:
            if i not in c.children:
                c.children[i] = Node()
            c = c.children[i]
        c.end = True

    def search(self, word: str) -> bool:
        c = self.head
        for i in word:
            if i not in c.children:
                return False
            c = c.children[i]
        return c.end

    def startsWith(self, prefix: str) -> bool:
        c = self.head
        for i in prefix:
            if i not in c.children:
                return False
            c = c.children[i]
        return True
        
# head -> (False, {})
# insert - "dog"
# head.children{'d'} -> (True, {})
# 'd'.children{'o'}->(True, {})
# 'o'.children{'g'}->(True, {})
# 'g'

        