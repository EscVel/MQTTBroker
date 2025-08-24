from socket import *
import ssl 
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"C:\Users\tanis\Desktop\cn mini project\yourdomain.crt", keyfile=r"C:\Users\tanis\Desktop\cn mini project\yourdomain.key")
serverPort = 17000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The subscriber is ready to receive") 
while True:
 connectionSocket, addr = serverSocket.accept()
 sentence = connectionSocket.recv(1024).decode()
 ACK = "acknowlegement"
 connectionSocket.send(ACK.encode())
 print("from publisher:", sentence)
 connectionSocket.close()
 
 
