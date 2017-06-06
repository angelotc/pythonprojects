

def nested_build(nested_list: [str or [str]])-> str:
    d= ''
    for item in nested_list:
        if type(item) == str:
            d += item + ' '
        else:
            d += nested_build(item)
    return d[:-1]

i = ['boo', ['is', 'happy', ['today']]]



def square(n: str)-> int:
    return int(n) ** 2

def read_and_square()->None:
    while True:
        number = int(input('Number: '))
        if number!=exit:
            try:
                square = powers.square(number)
                print('{} squared = {}\n'.format(number, squared))
            except:
                print(number + ' cannot be squared')
        else:
            break


def ask_for_floats()-> (float, float):
    while True:
        try:
            floats = input('Enter two floats: ')
            split = floats.split(',')
            if len(split) == 2:
                return (float(split[0]), float(split[1]))
            else:
                print('Try again.')
        except:
            print('Try again.')

ask_for_floats()
