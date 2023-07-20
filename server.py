import threading, os
import socket
#import rsa

hostname = socket.gethostbyname()
IPAddress = str(socket.gethostbyname(hostname))
port_num = str("Select port number: ")

#choice = input("Would you like to host the conncection or would you like to connect? Y or N: ")
#audience = int(print("How many people are joining: "))

def firstconnect():
    choice = input("Would you like to host the conncection or would you like to connect? Y or N: ")
    audience = int(print("How many people are joining: "))
    s_meetingcode = input("Please enter meeting code: ")

    n = audience
    choice  = choice.lower()

    Yesno = choice.startswith("y")

    while Yesno:
        server = socket.socket

        if choice.startswith("y"):
            try:
                print("Initiating connection with your terminal device")

                server = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
                server.bind((IPAddress, port_num))
                
                if audience > 0:
                    server.listen(n-1)
                else:
                    server.listen()
                
                Client_socket, Client_address = server.accept()
            except Exception as e:
                print("Connection error")
                print(" ")
                print(e)

    def send(c):
        while True:
            message = input("")

            c.send(message.encode())
            print("Me: ", message)
    
    def receive(c):
        print("Receipent: ", c.recv(1024).decode())

if __name__ == "__main__":
    firstconnect()

