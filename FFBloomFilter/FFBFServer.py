'''
Created on 2012/2/3

@author: bletchley
'''
import server
import threading
import BF_Operation

class FFBFServ(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        bit_vector='servBF'
        match_bit_vector='cliBF'
        all_signature='tmpfile'
        
        serv = server.Server(bit_vector) 
        serv.run()
        t = UpdateBF(all_signature,bit_vector)
        t.start()
        
    
class UpdateBF(threading.Thread):
    def __init__(self,all_signature,bit_vector):
        self.all_signature=all_signature
        self.bit_vector = bit_vector
        
        threading.Thread.__init__(self)
        self.operation = BF_Operation.BF_Operation()
        self.timer = threading.Event()
        
    def run(self):
        while True :
            self.timer.wait(200)
            print 'update bloom filter'
            self.operation.FFBF_INIT(self.all_signature, self.bit_vector)
            print 'finish update bloom filter'
            
bfser = FFBFServ()
