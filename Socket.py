import socket

try:
    #Example code that might raise an exception
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_socket.bind(('localhost', 65432))
     server_socket.listen(1)
except socket.error as e:
     print('Socketerror: {}'.format(e))
except Exception as e:
     print('other error: {}'.format(e))