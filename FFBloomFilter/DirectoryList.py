'''
Created on 2012/1/28

@author: bletchley
'''
import os
import FeedForwardBloomFilter

class DirList(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def ListAdd(self,path,ffbf):
        #path="C:\\somedirectory"  # insert the path to the directory of interest here
        dirList=os.listdir(path)
        for fname in dirList:
            filepath = path+'/'+fname
            if os.path.isfile(filepath) :
                ffbf.add(filepath)
                
            
    def ListCheck(self,path,ffbf,matchdata):
        #path="C:\\somedirectory"  # insert the path to the directory of interest here
        dirList=os.listdir(path)
        for fname in dirList:
            filepath = path+'/'+fname
            if os.path.isfile(filepath) and ffbf.check(filepath):
                matchdata.append(filepath)                    
                
    def ListReverCheck(self,path,ffbf,matchdata):
        #path="C:\\somedirectory"  # insert the path to the directory of interest here
        dirList=os.listdir(path)
        for fname in dirList:
            filepath = path+'/'+fname
            if os.path.isfile(filepath) and ffbf.match(filepath):
                matchdata.append(filepath)                    
                