#Copyright(c) 2015 Jason Ritz
#Licensed under: The MIT License (MIT)
#Last updated 12/07/2015 - by Jason Ritz
#TauNet Server program to listen for connections and print any incomming message
import socket
import StringIO


conn = ""
host = ""
port = 6283
key = 'password'



# Encrypt/Decrypt the given string with the given key using the RC4 method
# as described on ciphersaber.gurus.org/faq.html
def cipher( message , key ):
    j = 0
    n = 20 #number of times to run the mixing operation 
    state = []
    output = []
    
    #RC4 Key setup phase
    for i in range (0, 256):
        state.append(i)
    
    
    #RC4 mixing operation. Do this n>1 times to be cipher saber 2 complient
    # n > 20 is prefered
    for i in range (0, n):
        for i in range(0, 256):
            j = (j + state[i] + ord( key[i % len(key)] )) % 256
            state[i] , state[j] = state[j] , state[i]
    
    #RC4 ciphering operation 
    i = 0
    j = 0
    for char in message:
        i = ( i + 1 ) % 256
        j = ( j + state[i] ) % 256
        state[i] , state[j] = state[j] , state[i]
        output.append(chr(ord(char) ^ state[(state[i] + state[j]) % 256]))

    
    return ''.join(output)


#set up listener and decrypt and print any incomming messages
ls = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ls.bind((host, port))
marker = True

while (marker == True):
    ls.listen(5)
    conn , addr = ls.accept()
    received_message = conn.recv(1024)
    sio = StringIO.StringIO(received_message)
    iv = sio.read(10)
    message = sio.read()
    sio.close()
    received_message = cipher(message, key+iv)
    print ("\n" + received_message + "\n")
    test_quit = received_message.split("\r\n")
    #if (test_quit[4] == 'q'):
        #marker = False
        #print "Program closed. Good bye"

        
ls.close()



