
import socket
def start_tcp_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Bind the socket to the address and port
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)
    print('Starting up on {} port {}'.format(*server_address))
    # List for incoming connections
    server_socket.listen(1)
    while True:
        # Wait for a connection
        print('Wait for a connection')
        connection, client_address = server_socket.accept()
        try:
            print('Connection from', client_address)
            # Receive the data in small chunk and retransmit it
            while True:
                data = connection.recv(16)
                print('Received {!r}'.format(data))
                if data:
                    print('Sending data back to the client')
                    connection.sendall(data)
                else:
                    print('No more data from', client_address)
                    break
        finally:
            # Clean up the connection
            connection.close()
# Start the TCP server
start_tcp_server()