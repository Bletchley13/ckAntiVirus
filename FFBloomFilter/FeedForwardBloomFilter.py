'''
Created on 2012/1/28

@author: bletchley
'''
import array 
import Hash
import json

class FFBloomFilter(object):
    '''
    classdocs
    '''


    def __init__(self,size,hashNum):
        '''
        Constructor
        '''
            
        self.hashNum=hashNum
        self.size = size
        self.bf1 = array.array('i',range(self.size))
        self.bf2 = array.array('i',range(self.size))
        self.hashClass = Hash.Hash(self.size)
        
        for index in range(0,self.size):
            self.bf1[index]=0
            self.bf2[index]=0
        
    def add(self,fname):
        self.hashClass.hash(fname)
        val1 = int(self.hashClass.getHash(),16)
        val2 = int(self.hashClass.getHash2(),16)
        hashValue =val1%self.size
        for _ in range(self.hashNum):
            self.bf1[hashValue]+=1
            hashValue+=val2%self.size
            hashValue%=self.size
            
    def check(self,fname):
        #self.clear()
        self.hashClass.hash(fname)
        val1 = int(self.hashClass.getHash(),16)
        val2 = int(self.hashClass.getHash2(),16)
        hashValue =val1%self.size
        for _ in range(self.hashNum):
            if self.bf1[hashValue]==0 :
                return False
            hashValue+=val2%self.size
            hashValue%=self.size
            
        hashValue =val1%self.size
        for _ in range(self.hashNum):
            self.bf2[hashValue]+=1
            hashValue+=val2%self.size
            hashValue%=self.size
        return True
    
    def match(self,fname):
        self.hashClass.hash(fname)
        val1 = int(self.hashClass.getHash(),16)
        val2 = int(self.hashClass.getHash2(),16)
        hashValue =val1%self.size
        for _ in range(self.hashNum):
            if self.bf2[hashValue]==0 :
                return False
            hashValue+=val2%self.size
            hashValue%=self.size
        return True
    
    def clear(self):
        for index in range(0,self.size):
            self.bf2[index]=0
    
    def serialize(self,path):
        data = [self.bf1.tolist(),self.bf2.tolist()]
        content=json.dumps(data, sort_keys=True, indent=4)
        file = open(path,'w')
        file.write(content)
        file.close()
        
    def parsing(self,path):
        json_data=open(path)
        data = json.load(json_data)
        self.bf1 = array.array('i',data[0])
        self.bf2 = array.array('i',data[1])
        
        #bf2 = array.array(data[1])
        
