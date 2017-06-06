#echo client
import socket

# USER INTERFACE
#functions to solve parts of the problem

def read_host()->str:
    while True:
        host = input('Host: ').strip()
        if host == '':
            print('That is not valid; please try again')
        else:
            return host
    
        
#keep asking until legitimate


def read_port() -> int:
    while True:
        try:
            port = int(input('Port: '))
            if port < 0 or port > 65535:
                print('Ports are integers between 0 and 65535; please try again')
            else:
                return port

        except ValueError:
            print('Ports are integers; please try again')

def read_message() -> str:
    return input('Message: ')

def print_response(response)-> None:
    return input('Response: ' + response)



# Welcome to the Echo Client!
# Host:
# [error message]
# Host: woodhouse.ics.uci.edu
# Port: Boo
# [error message]
# Port: 5151
# Connecting to woodhouse.ics.uci.edu on port 5151...
# [connect to the server]
# Connected!
# Message: Hello
# [sent to the server]
# [response read from the server]
# Response: Hello
# Message: How are you?
# [sent to the server]
# [response read from the server]
# Response: How are you?
# Message:


#SOCKET/SERVER STUFF...
def connect(host: str, port: int) -> 'Connection':
    echo_socket = socket.socket()
    echo_socket.connect((host, port))

    echo_socket_in = echo_socket.makefile('r')
    echo_socket_out = echo_socket.makefile('w')
    
    
    return echo_socket, echo_socket_in, echo_socket_out

def send_message(connection: 'Connection', message: str) -> None:
    echo_socket, echo_socket_in, echo_socket_out = connection
    connection[2].write(message + '\r\n')

def send_message( connection: 'Connection', message: str) -> None:
    echo_socket, echo_socket_in, echo_socket_out = connection
    
    echo_socket_out.write(message + '\r\n')
    echo_socket_out.flush()

def receive_response( connection: 'Connection') -> str:
    echo_socket, echo_socket_in, echo_socket_out = connection
    
    return echo_socket_in.readline()[:-1]

## HIGH-LEVEL FUNCTION THAT ORCHESTRATES EVERYTHING
def run_user_interface() -> None:
    print('Welcome to the Echo Client!')
    host = read_host()
    port = read_port()
    print ('Connecting to {} on port {} ...'.format(host, port))

    connection = connect(host, port)
    
    
    print('Connected!')

    while True:
        message = read_message()

        if message == '':
            break
        
        send_message(connection, message)
        response = receive_response(connection)
        print_response(response)

    
if __name__ == '__main__':
    run_user_interface()
