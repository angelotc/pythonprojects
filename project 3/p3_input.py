import urllib.parse
import urllib.request
import json
API_KEY = '8GqlyDqwlAYl56YM82jqJ5AEexh26q1i'
ROUTE_URL = 'http://open.mapquestapi.com/directions/v2/route?'
LATLONG_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'




def build_directions_search_url(locations:list)->'url':
    '''Takes a list of lattitude and longitude locations and returns a url
    with the elevations for each of those areas'''
    query_parameters = [('key', API_KEY), ("from", locations[0])]
    for location in locations[1:]:
        query_parameters.append((("to", location)))
    #print(ROUTE_URL + urllib.parse.urlencode(query_parameters))
    return ROUTE_URL + urllib.parse.urlencode(query_parameters)


def build_elevations_search_url(latlongs:list)-> 'url' :
    ''' Takes a list of lattitude and longitude locations and returns a url
    with the elevations for each of those areas.'''
    query_parameters = [('key', API_KEY), ("shapeFormat", 'raw')]
    url_latlong = ''
    for item in latlongs:
        url_latlong+= str(item) + ','
    #print(LATLONG_URL + urllib.parse.urlencode(query_parameters) +  '&latLngCollection=' + url_latlong[:-1])
    return LATLONG_URL + urllib.parse.urlencode(query_parameters) + '&latLngCollection=' + url_latlong[:-1]


def url_to_json(url:str)->str:
    '''Takes a url(string) and returns a json object(string).'''
    response = urllib.request.urlopen(url)
    json_object = json.loads(response.read().decode(encoding = 'utf-8'))
    response.close()
    return json_object
