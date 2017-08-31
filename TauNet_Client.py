#Copyright(c) 2015 Jason Ritz
#Licensed under: The MIT License (MIT)
#Last updated 12/07/2015 - by Jason Ritz
#TauNet client program to send messages to other TauNet users 

import socket
import os

send_port = 6283
send_text = 'x'
key = "password"
to_user = "user"

address_of = {'tdulcet': 'tealdulcet.ddns.net', 'patter5':'megmurry.ddns.net',
'relsqui':'cupcake.chiliahedron.com', 'pyrrh':'souffle.chiliahedron.com',
'mancat':'inchworm.mindtax.net', 'dom':'mahan.mindtax.net',
'brodie':'solar.noip.me', 'paolo2':'pirr.ddns.net',
'mrme':'mrme.ddns.net', 'home':'127.0.0.1', 'manpreet20':'manpreet.ddns.net',
'huyng90':'huyng90.ddns.net', 'rhatchet':'pi.arenjae.com', 'natreed':'natreed.ddns.net',
'leng':'lengpi.ddns.net', 'aldridge85':'csjosh.ddns.net', 'etsai':'etsai.ddns.net',
'jbucklin':'jbucklin.ddns.net', 'po8':'po8.org', 'mantron':'mantron.ddns.net',
'jojen2':'itsjonnyjyo.ddns.net', 'seven':'192.168.2.7', 'nine':'192.168.2.9',
'cort':'wyeast.ddns.net', 'rubear':'131.252.211.242', 'echo':'barton.cs.pdx.edu'}



#send encrypted message created with the prep_message function
def send_message(ip, port, message):
    ss = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    ss.connect((ip, port))
    ss.sendall(message)
    ss.close()
    return 0



#encrypt message to send and add the iv as the first 10 bytes
def prep_message(send_text, to_user):
    iv = os.urandom(10)
    send_text = add_header(send_text, to_user)
    message = cipher(send_text, key+iv)
    send_text = iv + message
    return send_text



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



def add_header(message, to_user):
    version = "version: 0.2\r\n"
    to = to_user + "\r\n\r\n"
    sender = user_name + "\r\n"
    return version + "from: " + sender + "to: " + to + message




user_name = raw_input("\nEnter your user name:  ")

while (send_text != 'q'):
    to_user = raw_input("\nEnter the user name to send to:  ")
    send_text = raw_input("\nEnter your message:  ")
    message = prep_message(send_text, to_user)
    if (to_user not in address_of):
        print "No user by that name. Please try again\n"
    else:
        send_ip = address_of[to_user]
        send_message(send_ip, send_port, message)
    

    

print "\ngood bye"

