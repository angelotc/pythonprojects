

#PROJECT3 // UI FUNCTIONS
# by Angelo Cortez 43373142

import json

from p3_outputs import *
from p3_input import *


#http://open.mapquestapi.com/directions/v2/route?key=8GqlyDqwlAYl56YM82jqJ5AEexh26q1i
##def build_url(s:str, max_results: int)->str:
##    query_parameters = [
##        ('key', MQ_API_KEY), ('latLngCollection', 'snippet')

def integer_input()->int:
    '''An integer whose value is at least 2, alone on a line,
    that specifies how many locations the trip will consist of.'''
    while True:
        x = int(input(
            'How many locations will the trip consist of?: '))
        if x<2:
            print('Locations must be more than 2.')
            continue
        
        else:
            return x


def output_integer_input()->int:
    ''' given an integer that is a number from 1-5, it will create a list with that length and
    input for each indice'''
    while True:
        x = int(input('How many outputs do you want to see?: '))
        if x>5 or x<0:
            print('Integer must be within a number from 1-5')
            continue
        else:
            return x
            break



def inputs(x: int)->[str]:
    '''given an integer, it will create a list of strings with that many values'''
    d = []
    for y in range(0,x):
        d.append(y)
    for i in d:
        d[i] = input('Input ' + str(int(i+1)) + ': ')
                                                               
    return d



def ui_main()-> 'json_object':
    integers = integer_input()
    locations = inputs(integers)
    url = build_directions_search_url(locations)
    try:
        json_object = url_to_json(url)
        #print(json_object)
    except urllib.error.URLError:
        print("\nMAPQUEST ERROR")
        ui_main()
    except urllib.error.HTTPError:
        print('HTTP ERROR')
        ui_main()
    except urllib.error.ContentTooShortError:
        print("CONTENT TOO SHORT")
        ui_main()
    finally:
        if RouteError in json_object['info']['messages']:
            print ('Error with the route given. Try again.')
            ui_main()
        else:
            output_integers = output_integer_input()
            outputs = inputs(output_integers)
            for i in outputs:
                
                if i == 'STEPS':
                    STEPS.output(json_object)
                elif i == 'TOTALDISTANCE':
                    TOTALDISTANCE.output(json_object)
                elif i == 'LATLONG':
                    LATLONG.output(json_object)
                elif i == 'TOTALTIME':
                    TOTALTIME.output(json_object)
                elif i == 'ELEVATION':
                    list_of_latlong = list_latlong(json_object)
                    #print(list_of_latlong)
                    url2 = build_elevations_search_url(list_of_latlong)
                    json_object2 = url_to_json(url2)
                    #print(json_object2)
                    ELEVATION.output(json_object2)
            print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
                    
                        


            
            
    
       
RouteError = 'We are unable to route with the given locations.'


            


        

            
if __name__ == '__main__':
    ui_main()
    
    
     
    
