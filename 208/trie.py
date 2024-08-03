class Trie(object):
    @staticmethod
    def char_index(char):
        return ord(char.lower()) - ord('a')

    class Node(object):
        def __init__(self, val):
            self.val = val
            self.children = [None] * (Trie.char_index('z')+1)
            self.is_terminal = False


    def __init__(self):
        self.root = self.Node(None)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """ 
        node = self.root
        for c in word:
            c_index = Trie.char_index(c)
            if node.children[c_index] == None:
                node.children[c_index] = self.Node(c)

            node = node.children[c_index]

        node.val = word
        node.is_terminal = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            c_index = Trie.char_index(c)
            if node.children[c_index] == None:
                return False
            
            node = node.children[c_index]
        
        return node.is_terminal
    

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            c_index = Trie.char_index(c)
            if node.children[c_index] == None:
                return False
            
            node = node.children[c_index]
        
        return True
        


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))     # return True
print(trie.search("app"))       # return False
print(trie.startsWith("app"))   # return True
trie.insert("app")
print(trie.search("app"))       # return True