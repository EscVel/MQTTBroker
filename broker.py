from socket import *
import ssl

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"C:\Users\tanis\Desktop\cn mini project\yourdomain.crt", keyfile=r"C:\Users\tanis\Desktop\cn mini project\yourdomain.key")

serverPort = 16000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

serverName = "localhost"
clientPort = 17000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, clientPort))
print("The broker is ready to receive")
from socket import *


while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        print(f"Received from publisher: {sentence}")
        
        # Establish a new connection to the subscriber for each publisher connection
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(("localhost", 17000))
        
        capitalizedSentence = sentence.upper()
        clientSocket.send(capitalizedSentence.encode())
        
        modifiedSentence = clientSocket.recv(1024).decode()
        print(f"Modified sentence: {modifiedSentence}")
        
        connectionSocket.send(modifiedSentence.encode())
        
        connectionSocket.close()
        clientSocket.close()
    except Exception as e:
        print(f"Error occurred: {e}")
        # Ensure sockets are closed in case of an error
        if 'connectionSocket' in locals():
            connectionSocket.close()
        if 'clientSocket' in locals():
            clientSocket.close()


