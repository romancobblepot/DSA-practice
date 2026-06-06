from collections import defaultdict
class Trie(object):

    def __init__(self):
        self.arr=[]
        self.prefix=defaultdict(list)
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.arr.append(word)
        for i in range(len(word)):
            self.prefix[word[:i+1]].append(word)
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.arr:
            return True
        return False
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if prefix in self.prefix:
            return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)