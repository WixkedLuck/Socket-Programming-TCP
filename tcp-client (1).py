'''

TCP Client

'''

from socket import *

serverName = 'localhost'
serverPort = 15000

clientSocket = socket()
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

# function to encode message using utf-8
def encode_message(message):
    return message.encode('utf-8')


try:

    sentence = input('Enter lowercase sentence: ')
    # call function to encode user input
    encoded_sentence = encode_message(sentence)
    #  send to server as encoded message
    clientSocket.send(encoded_sentence)
    #print encoded message sent to server
    print(f"Sent encoded message: {list(encoded_sentence)}")

    # get the responce from the server side
    recieved_encoded_message = clientSocket.recv(1024)
    # print encoded version of message sent from server side
    print(f"Received Server side encrpyted version of message: {list(recieved_encoded_message)}")

finally:
    # close off connections
    clientSocket.close()

