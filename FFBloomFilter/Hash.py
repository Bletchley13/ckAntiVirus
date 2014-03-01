'''
Created on 2012/1/28

@author: bletchley
'''
import hashlib

class Hash(object):
    '''
    classdocs
    '''
    

    def __init__(self,mod):
        '''
        Constructor
        '''
        #print "nerClass"
        self.mod = mod
    
    def hash(self,fname):
        #print 'test'
        #print self.mod
        self.Hvalue=self.hash1(fname)
        self.Hvalue2=self.hash2(fname)
        #return (self.hash1(content)+index*self.hash2(content))%self.mod
    def getHash(self):
        return self.Hvalue
    
    def getHash2(self):
        return self.Hvalue2
    
    def hash1(self,file):
        md5 = hashlib.md5()
        with open(file,'rb') as f: 
            for chunk in iter(lambda: f.read(8192), ''): 
                md5.update(chunk)
        #print md5.hexdigest()
        return md5.hexdigest()
    
    def hash2(self,file):
        sha1 = hashlib.sha1()
        with open(file,'rb') as f: 
            for chunk in iter(lambda: f.read(8192), ''): 
                sha1.update(chunk)
        #print sha1.hexdigest()
        return sha1.hexdigest()

