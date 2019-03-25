'''One module that implements the I32CFSP and all socket handling. If you're going to connect, read, write, etc., via a socket, you would do that in functions written in this module. But this module shouldn't do anything other than that.
'''
import connectfour
import connectfour_same_actions
import socket
from collections import namedtuple

GameConnection = namedtuple('GameConnection', ['socket', 'socket_in', 'socket_out'])
def connect() -> GameConnection:
    '''connect to game and return a GameConnection'''
    while True:
        try:
            connect_four_socket = socket.socket()
            specified_host = input("Please type in a host.").strip()
            specified_port = int(input("Please type in a port."))
            connect_address = (specified_host, specified_port)
            connect_four_socket.connect(connect_address)
            connect_four_socket_in = connect_four_socket.makefile("r")
            connect_four_socket_out = connect_four_socket.makefile("w")
            return GameConnection(
               socket = connect_four_socket,
               socket_in = connect_four_socket_in,
                socket_out = connect_four_socket_out)            
        except ValueError:
            print("Please try again.")
            connect_four_socket.close()
            
        except ConnectionRefusedError:
            print("Connection didn't work")
            connect_four_socket.close()
        except Exception as e:
            if str(e) == "[Errno 8] nodename nor servname provided, or not known":
                print("Please type valid port or host next time. ")
            connect_four_socket.close()

            
def connect_username(connection: GameConnection):
    '''prompts user for username and connects user'''
    username = input("Please enter your desired username.")
    while True:
        if len(username.split()) == 1:
            write_line(connection, 'I32CFSP_HELLO ' + username)
            break
        else:
           username = input("Please enter a valid username without spaces. ")
        


def write_line(connection: GameConnection, line: str) -> None:
    '''write in socket file'''
    connection.socket_out.write(line + "\r\n")
    connection.socket_out.flush()
def read_line(connection: GameConnection) -> str:
    '''read from socket file'''
    return connection.socket_in.readline().strip("\n")

def close_socket(connection: GameConnection):
    connection.socket_in.close()
    connection.socket_out.close()
    connection.socket.close()


