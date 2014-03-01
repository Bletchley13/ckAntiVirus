'''
Created on 2012/2/3

@author: bletchley
'''
import socket
import json
import threading
import time

class Client(threading.Thread):
    '''
    classdocs
    '''
    size = 1024
    

    def __init__(self,bit_vector):
        '''
        Constructor
        '''            
        self.bit_vector = bit_vector
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.sock.connect(('localhost', 8001))    
        self.sock.send('getSerBF')  
        #print self.sock.recv(1024)  
        self.getFile(bit_vector)
        self.sock.close() 
    
    def sendFile(self,filename):
        json_data=open(filename)
        data = json.load(json_data)
        content=json.dumps(data, sort_keys=True, indent=4)
        size = len(content)
        print 'len',size
        self.connection.send(str(size))
        self.connection.send(content)
    
    def getFile(self,filename):
        process = 0
        size = self.sock.recv(1024)
        print size
        content = ''
        print 'start transmission'
        while int(size)-len(content)>0 :
            if int(size)-len(content)<1024 :
                chunk = int(size)-len(content)
            else :
                chunk =1024
            content+=self.sock.recv(chunk)
            #nprocess = int(len(content)*100/int(size))
            #if (nprocess%10)==0 and nprocess>process:
             #   procrss = nprocess
                #print procrss,' ',nprocess
                #print 'processing ',len(content),' ',len(content)*100/int(size)
            #print 'processing ',len(content),' ',len(content)*100/int(size)
        print 'trans complete'
        print filename
        data = json.loads(content)
        file = open(filename,'w')
        file.write(content)
        file.close()
        #print len(data)
        
        