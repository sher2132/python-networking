# UDP Server
# Let’s create a simple UDP server that listens for incoming messages and echoes them back to the sender.
import socket
def start_udp_server():
    # Create a UDP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind the socket to the address and port
    server_address = ('localhost', 65432)
    print('Starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    while True:
        # Wait for a message
        print('waiting for a message')
        data, address = server_socket.recvfrom(4096)

        print('Received {} bytes from {}'.format(len(data),address))
        

