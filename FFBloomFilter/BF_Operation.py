'''
Created on 2012/1/28

@author: bletchley
'''
import FeedForwardBloomFilter
import array
import time
import DirectoryList
import filecmp

class BF_Operation(object):
    def __init__(self):
        self.hashNum = 10
        self.bitSize = 1024*1024
    
    def FFBF_INIT(self,path,outBF):
        ffbf =  FeedForwardBloomFilter.FFBloomFilter(self.bitSize,self.hashNum)
        Dir = DirectoryList.DirList()
        Dir.ListAdd(path,ffbf)
        ffbf.serialize(outBF)
    
    def FFBF_SCAN(self,path,inBF,outBF):
        ffbf =  FeedForwardBloomFilter.FFBloomFilter(self.bitSize,self.hashNum)
        ffbf.parsing(inBF)
        Dir = DirectoryList.DirList()
        ffbf.clear()
        matchdata = []
    
        Dir.ListCheck(path,ffbf,matchdata)
        #print matchdata
        #print len(matchdata)
        ffbf.serialize(outBF)
        return matchdata

    def FFBF_HIT(self,path,outBF):
        ffbf =  FeedForwardBloomFilter.FFBloomFilter(self.bitSize,self.hashNum)
        ffbf.parsing(outBF)
        rmatchdata = []
        Dir = DirectoryList.DirList()
        Dir.ListReverCheck(path,ffbf,rmatchdata)
        print rmatchdata
        print len(rmatchdata)
        return rmatchdata
    
    def FFBF_VERIFY(self,matchdata,rmatchdata):
        match=[]
        for item in matchdata:
            for item2 in rmatchdata:
                if filecmp.cmp(item, item2):
                    match.append(item+':'+item2)
        return match
    
'''    
if __name__ == '__main__':
    #parameter
    bit_vector='inBF'
    match_bit_vector='outBF'
    all_signature='tmpfile'
    match_signature='testfiles'
    
    #server site
    FFBF_INIT(all_signature,bit_vector)
    
    #client site
    matchdata = FFBF_SCAN(match_signature,bit_vector,match_bit_vector)
    
    #serversite
    rmatchdata = FFBF_HIT(all_signature,match_bit_vector)
    
    #exactly match
    match=FFBF_VERIFY(matchdata,rmatchdata)
    
    print len(match)
    for item in match:
        print item
'''
    
    
    
    
    
