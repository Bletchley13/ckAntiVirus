'''
Created on 2012/1/28

@author: bletchley
'''

class BloomFilter(object):
    '''
    classdocs
    '''


    def __init__(self,size,hashNum):
        '''
        Constructor
        '''
        import array 
        import Hash    
        self.hashNum=hashNum
        self.size = size
        self.bf = array.array('i',range(self.size))
        self.hashClass = Hash.Hash(self.size)
        
        for index in range(0,self.size):
            self.bf[index]=0
        
    def add(self,content):
        self.hashClass.hash(content)
        val1 = self.hashClass.getHash()
        val2 = self.hashClass.getHash2()
        hashValue =val1
        for index in range(self.hashNum):
            self.bf[hashValue]+=1
            hashValue+=val2
            hashValue%=self.size
            
    def check(self,content):
        self.hashClass.hash(content)
        val1 = self.hashClass.getHash()
        val2 = self.hashClass.getHash2()
        hashValue =val1
        for index in range(self.hashNum):
            if self.bf[hashValue]==0 :
                return False
            hashValue+=val2
            hashValue%=self.size
        return True
    
    def clear(self):
        for index in range(0,self.size):
            self.bf[index]=0
