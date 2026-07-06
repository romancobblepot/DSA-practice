import random
class RandomizedSet(object):

    def __init__(self):
        self.set={}
        self.mapp={}
        self.arr=[]
        self.len=0
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        else:
            self.mapp[val]=self.len
            self.len+=1
            self.arr.append(val)
            self.set[val]=val
            return True
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            i=self.mapp[val]
            last=self.arr[-1]
            self.arr[-1],self.arr[i]=self.arr[i],self.arr[-1]
            self.arr.pop()   
            self.len-=1         
            del self.set[val]
            del self.mapp[val]
            self.mapp[last]=i
            return True
        return False
    def getRandom(self):
        """
        :rtype: int
        """
        k=random.randrange(self.len)
        return self.arr[k]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()