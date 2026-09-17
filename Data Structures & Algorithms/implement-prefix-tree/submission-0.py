class Node:
    def __init__(self):
        self.children  = {}
        self.end = False
class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        def insertinnode(word, i,node):
            if i==len(word):
                node.end =True
                return 
            if word[i] in node.children:
                insertinnode(word,i+1, node.children[word[i]])
            else:
                node.children[word[i]] = Node()
                insertinnode(word,i+1, node.children[word[i]])
        insertinnode(word,0,self.head)

    def search(self, word: str) -> bool:
        def searchinnode(word,i,node):
            if i==len(word):
                return node.end
            if word[i] not in node.children:
                return False
            else:
                return searchinnode(word,i+1,node.children[word[i]])
        return searchinnode(word,0,self.head)

    def startsWith(self, prefix: str) -> bool:
        def startswithnode(prefix, i, node):
            if i==len(prefix):
                return True
            if prefix[i] not in node.children:
                return False
            return startswithnode(prefix,i+1,node.children[prefix[i]])
        return startswithnode(prefix,0,self.head)
        
# head -> (False, {})
# insert - "dog"
# head.children{'d'} -> (True, {})
# 'd'.children{'o'}->(True, {})
# 'o'.children{'g'}->(True, {})
# 'g'

        