import socket
import threading
import signal
import sys
import logging

logging.basicConfig(level=logging.INFO)


def handle_client(connection, client_address):
    try:
        logging.info('Connection from %s', client_address)
        while True:
            data = connection.recv(1024)
            if data:
                logging.info('Received from %s: %r', client_address, data)
                connection.sendall(data)  # Echo data back
            else:
                logging.info('No more data from %s', client_address)
                break
    except Exception as e:
        logging.error('Error handling client %s: %s', client_address, e)
    finally:
        connection.close()


def signal_handler(sig, frame):
    logging.info('Shutting down server...')
    sys.exit(0)


def start_threaded_tcp_server():
    signal.signal(signal.SIGINT, signal_handler)

    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to localhost and an available port (using port 0)
    server_address = ('127.0.0.1', 0)
    server_socket.bind(server_address)

    # Retrieve the dynamically assigned port via getsockname()
    host, port = server_socket.getsockname()
    logging.info('Server is waiting for connections at %s:%s', host, port)

    # Listen for incoming connections
    server_socket.listen(5)

    while True:
        try:
            connection, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connection, client_address), daemon=True)
            client_thread.start()
        except Exception as e:
            logging.error('Error in server loop: %s', e)


# Start the server
if __name__ == '__main__':
    start_threaded_tcp_server()