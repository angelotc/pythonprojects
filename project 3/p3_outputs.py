###CLASSESoutput
class STEPS:
    def output(self:'json object'):
        print('\nDIRECTIONS')
        for item in self['route']['legs'][0]['maneuvers']:
            print(item['narrative'])



class ELEVATION:
    def output(self:'json object'):
        '''creates output string that converts feet elevation to rounded meters'''
        print('\nELEVATIONS') 
        for item in self['elevationProfile'][:]:
            for key,value in item.items():
                if key == 'height':
                    print(round(value*3.28084))

            

class TOTALTIME:
    def output(self:'json object'):
        time_in_minutes = round(self['route']['time']/60)
        print('\nTOTAL TIME: {} minutes'.format(time_in_minutes))
        
class TOTALDISTANCE:
    def output(self:'json object'):
        distance = round(self['route']['distance'])
        print('\nTOTAL DISTANCE: {} miles'.format(distance))

    

class LATLONG:
    def output(self:'json object'):
        print('\nLATLONGS')
        locations = self['route']['locations']
        for location in locations:
            lat = location['displayLatLng']['lat']
##            type(lat)
            lng = location['displayLatLng']['lng']
##            type(long)
            print(str_latlong(lat, 'lat') + str_latlong(lng, 'lng'))



def list_latlong(self:'json object')-> [str]:
    xD = []
    locations = self['route']['locations']
    for location in locations:
        xD.append(location['displayLatLng']['lat'])
        xD.append(location['displayLatLng']['lng'])
    return xD



def str_latlong(i:float, s:'lat or lng')-> str:
    '''takes in a float value of lattitude/longitude and returns into a printable
        format'''
    if s == 'lat':
        if i < 0:
            return "{0:.2f}".format(abs(i)) + 'S '
        else:
            return "{0:.2f}".format(abs(i)) + 'N '
    elif s == 'lng':
        if i < 0:
            return "{0:.2f}".format(abs(i)) + 'W '
        else:
            return "{0:.2f}".format(abs(i)) + 'E '
