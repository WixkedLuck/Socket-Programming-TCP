'''

TCP Server

'''

from socket import *

serverPort = 15000

serverSocket = socket()
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(2)

print('The server is ready to receive...')
# function to decode message received
def decode_message(encoded_message):
    return encoded_message.decode('utf-8')

while True:
    connectionSocket, addr = serverSocket.accept()
    # received on port 1024
    encoded_message = connectionSocket.recv(1024)
    # call function decode_message with encoded_message
    decoded_message = decode_message(encoded_message)
    # print out encoded recieved message
    print(f"Received encoded message: {list(encoded_message)}")
    #print out decoded version of message
    print(f"Decoded message: {decoded_message}")

    # send the encoded version back to client side
    connectionSocket.send(encoded_message)
    print(f"Send back encoded message: {list(encoded_message)}")
    #close off connections
    connectionSocket.close()

