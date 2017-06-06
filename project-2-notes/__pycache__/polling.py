# polling.py
#
# Polling protocol implementation (i.e., everything about how to communicate
# with Polling server and interpret its responses, and *nothing* about
# interacting with the user).




from collections import namedtuple
import socket

PollingConnection = namedtuple(
    'PollingConnection',
    ['socket', 'input', 'output'])


class PollingProtocolError(Exception):
    pass


HELLO = 1
NO_USER = 2


def connect(host: str, port: int)-> 'PollingConnection':
    polling_socket = socket.socket()
    polling_socket.connect((host, port))

    polling_socket_in = polling_socket.makefile('r')
    polling_socket_out = polling_socket.makefile('w')

    return PollingConnection(
        socket =polling_socket,
        input = polling_socket_in,
        output = polling_socket_out)


def hello(connection: PollingConnection, username: str)-> HELLO or NO_USER:
    write_line(connection, 'POLLING_HELLO '+ username)
    #totally not what I ultimately want, but useful for now...

    response = _read_line(connection)

    if response == 'HELLO':
        return HELLO
    elif response.startswith('NO_USER'):
        return NO_USER
    else:
        raise PollingProtocolError()
    
_SHOW_DEBUG_TRACE = True


# Private functions

def write_line( connection: PollingConnection, line:str) -> None:
    connection.output.write(line + '\r\n')
    connection.output.flush()
    if _SHOW_DEBUG_TRACE:
        print('SENT: '+ line)

def _read_line(connection: PollingConnection) -> str:
    line =  connection.input.readline()[:-1]

    if _SHOW_DEBUG_TRACE:
        print('RCVD: ' + line)
        
    return line

