# UDP Client
# This program sends a message to a UDP server and prints the server's response.

import socket


def start_udp_client():
    # Create a UDP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define server address and port
    server_address = ('localhost', 6532)  # Update the port if your server uses a different one

    # Message to send to the server
    message = b'This is the message. It will be repeated.'

    try:
        # Send data
        print('Sending: {!r}'.format(message))
        sent = client_socket.sendto(message, server_address)

        # Receive response
        print('Waiting for a response...')
        data, server = client_socket.recvfrom(4096)  # Buffer size set to 4096 bytes
        print('Received: {!r}'.format(data.decode('utf-8')))  # Decode bytes to string for display

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket
        print('Closing socket')
        client_socket.close()


# Start the UDP client
if __name__ == "__main__":
    start_udp_client()