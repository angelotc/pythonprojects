#Angelo Cortez 43373142 and Ruowan Yang 74391124


from collections import namedtuple
import socket
import connect4


HELLO = 1
NO_USER = 2

PollingConnection = namedtuple('PollingConnection',
                               ['socket', 'input', 'output'])
                               
class PollingProtocolError(Exception):
    pass



def connect(host: str, port: int)-> 'PollingConnection':
    polling_socket = socket.socket()
    polling_socket.connect((host, port))

    polling_socket_in = polling_socket.makefile('r')
    polling_socket_out = polling_socket.makefile('w')

    return PollingConnection(
        socket =polling_socket,
        input = polling_socket_in,
        output = polling_socket_out)

def hello(connection: PollingConnection, username: str) -> HELLO or NO_USER:
    write_line(connection, 'I32CFSP_HELLO ' + username)
    

    response = read_line(connection)

    if response.startswith('WELCOME '):
        write_line(connection, 'AI_GAME')
        response2 = read_line(connection)
        


def write_line( connection: PollingConnection, line:str) -> None:
    connection.output.write(line + '\r\n')
    connection.output.flush()
    if _SHOW_DEBUG_TRACE:
        print('SENT: '+ line)

def read_line(connection: PollingConnection) -> str:
    line =  connection.input.readline()[:-1]

    if _SHOW_DEBUG_TRACE:
        print('AI: ' + line)
        
    return line

_SHOW_DEBUG_TRACE = True

def read_lines(connection: PollingConnection) -> [str]:
    line =  connection.input.readlines()[:-1]

    if _SHOW_DEBUG_TRACE:
        print('RCVD: ' + line)
        
    return line

def close ( connection: PollingConnection) -> None:
    connection.input.close()
    connection.output.close()
    connection.socket.close()





