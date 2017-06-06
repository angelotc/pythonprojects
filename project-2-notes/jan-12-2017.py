#write a program that asks the user(repeatedly) for ap ath to a file
#and it tells the user how many lines of text are in the file

def count_lines_in_file(file_path:str) -> int:
    the_file = None
    try:
        #open(), when it fails, always raises an OSError
        the_file = open(file_path, 'r')
        
        line_count = 0
        #
        #
        for line in the_file:
            line_count+=1
            
        the_file.close()
        return len(all_lines)
    finally:
        print('hi')

def run_user_interface()->None:
    while True:
        path = input('What file? ')

        if path == '':
            break
        else:
            try:
                lines = count_lines_in_file(path)
                print('Lines in file: {}'.format(lines))
            except OSError:
                print('That file does not exist')
            except ValueError:
                print('That file does not contain text')


if __name__=='__main__':
    run_user_interface()
