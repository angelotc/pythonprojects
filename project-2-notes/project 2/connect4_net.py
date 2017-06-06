#Angelo Cortez 43373142 and Ruowan Yang 74391124

from I32CFSP import *
from utilities import *



def read_host()->str:
    while True:
        host = input('Host: ')
        if host == '' or ' ' in host:
            print('That is not valid; please try again')
            read_host()
            break
        else:
            return port_and_name(host)

def port_and_name(s:str)-> None:
    while True:
        
        port = int(input('Port: '))
        if port < 0 or port > 65535:
            print('Ports are integers between 0 and 65535; please try again')
        else:
            
            try:
                c = connect( s, port)
                name = get_name()
                hello(c, name)
                main2(c)
                print('Attemping to connect to {} (port: {})').format(s, port)
                break
            except:
                print('Invalid connection. Try again.')
                read_host()





def get_name()-> str:
    while True:
        name = str(input('Please type a username (no spaces): ')).strip()
        if ' ' in name:
            print('There can be no spaces, try again')
        else:
            return name
            break
        
        
    
def main2(connection: PollingConnection):
    print('WELCOME TO CONNECT FOUR. \nYOU ARE RED.')
    currentgame = connect4.new_game()
    print_board(currentgame.board)
    c = connection
    while True:
        
        while True:
            yourmove = str(input('DROP or POP? (e.g. "DROP 1" or DROP "7"): ')).upper()
            if len(yourmove.split()) != 2:
                continue
            
            elif 7<int(yourmove.split()[1]) or int(yourmove.split()[1])<0:
                continue
            elif yourmove.startswith('DROP') or yourmove.startswith('POP'):
                break

        try:
            if yourmove.startswith('DROP'):
                write_line(c, yourmove)
                currentgame = connect4.drop(currentgame, int(yourmove[5]) - 1)
                if connect4.winner(currentgame)==1:
                    print_board(currentgame.board)
                    print('You win!')
                    close(c)
                    break
                
                elif connect4.winner(currentgame) ==2:
                    print_board(currentgame.board)
                    print('Computer wins!')
                    close(c)
                    break
            elif yourmove.startswith('POP'):
                write_line(c, yourmove)
                currentgame = connect4.pop(currentgame, int(yourmove[4]) - 1)
                if connect4.winner(currentgame)==1:
                    print_board(currentgame.board)
                    print('You win!')
                    close(c)
                    break
                
                elif connect4.winner(currentgame) ==2:
                    print_board(currentgame.board)
                    print('Computer wins!')
                    close(c)
                    break
                
        except:
            print('error')
            
                        
        response = read_line(c)
        
        if response == 'OKAY':
            AI_move = read_line(c)
            if AI_move.startswith('DROP') or AI_move.startswith('POP'):
                readyornot = read_line(c)
                currentgame = connect4.drop(currentgame, int(AI_move[5]) - 1)
                print_board(currentgame.board)
                if connect4.winner(currentgame)==1:
                    print('You win!')
                    close(c)
                    break
                
                elif connect4.winner(currentgame) ==2:
                    print('Computer wins!')
                    close(c)
                    break

        elif response == 'INVALID':
            readyornot = read_line(c)



if __name__ == '__main__':
    read_host()
    
