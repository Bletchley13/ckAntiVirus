'''
Created on 2012/2/4

@author: bletchley
'''
import client
import BF_Operation

class FFBFCli(object):
    '''
    classdocs
    '''
    bit_vector='inBF2'
    match_bit_vector='outBF2'
    match_signature='testfiles'

    def __init__(self):
        '''
        Constructor
        '''
        ''' update BF '''
        cli = client.Client(self.bit_vector) 
        #cli.run()
        self.run()
        
    def run(self):
        self.operation = BF_Operation.BF_Operation()
        matchdata = self.operation.FFBF_SCAN(self.match_signature,self.bit_vector,self.match_bit_vector)
        print matchdata
        
cli = FFBFCli()
