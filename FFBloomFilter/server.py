'''
Created on 2012/2/3

@author: bletchley
'''
import socket
import threading
import json

class Server(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self,bit_vector):
        '''
        Constructor
        '''
        self.bit_vector=bit_vector
        self.port = 8001
        print 'server initial'
    
    def run(self):  
        print 'server listen on port 8001'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        sock.bind(('localhost', self.port))  
        sock.listen(5)  
        
        while True:  
            self.connection,address = sock.accept()  
            try:  
                self.connection.settimeout(5)
                print address  
                buf = self.connection.recv(1024)  
                if buf == 'getSerBF':  
                    #self.connection.send('send servBF to client')
                    self.sendFile(self.bit_vector)
                if buf == 'putCliBF' : 
                    self.connection.send('get cliBF from server') 
                else:  
                    self.connection.send('please go out!')  
            except socket.timeout:  
                print 'time out'  
            self.connection.close() 
            
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
            nprocess = len(content)*100/int(size)
            if (nprocess%10)==0 and nprocess>process:
                procrss = nprocess
                print 'processing ',len(content),' ',len(content)*100/int(size)
            #print 'processing ',len(content),' ',len(content)*100/int(size)
        print 'trans complete'
        data = json.loads(content)
        print len(data)
           
           