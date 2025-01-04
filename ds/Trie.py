class Trie():

    def __init__(self):
        self.prefix_count = 0
        self.child = [None]*26
        self.word_end = False
        
    def insert(self, word):
        curr = self
        for c in word:
            index = ord(c)-ord("a")
            if curr.child[index] == None:
                curr.child[index] = Trie()
            curr = curr.child[index]
            curr.prefix_count += 1
        curr.word_end = True

        
    def search(self, word):
        curr = self
        for c in word:
            index = ord(c)-ord("a")
            if curr.child[index] == None: return False
            curr = curr.child[index]
        return curr.word_end
        
    def startsWith(self, prefix):
        curr = self
        for c in prefix:
            index = ord(c)-ord("a")
            if curr.child[index] == None: return False
            curr = curr.child[index]
        return curr.prefix_count > 0
        