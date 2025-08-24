from socket import *
import ssl
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"C:\Users\tanis\Desktop\cn mini project\yourdomain.crt", keyfile=r"C:\Users\tanis\Desktop\cn mini project\yourdomain.key")
serverName = "localhost"
serverPort = 16000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("enter")
clientSocket.send(sentence.encode())
print("sent")
clientSocket.close()