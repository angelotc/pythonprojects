# Subject: API's in depth
import json
import urllib.request
import urllib.parse

response  = urllib.request.urlopen('http://open.mapquestapi.com/directions/v2/route?key=8GqlyDqwlAYl56YM82jqJ5AEexh26q1i&from=Irvine%2CCA&to=Los+Angeles%2CCA')
data = response.read()
response.close()
string_data = data.decode(encoding = 'utf-8')
obs = json.loads(string_data)

# URL encoding (percent encoding)
# * spaces are replaced with +
# * other special characters are replaced with %, followed by the character by the
#
#     
#       *decimal (base 10): 0123456789
#       *hexadecimal (base 16):0123456789ABCDEF
#           (3D)16 = (13*1) + (3*16) = 61(10)
#
#
#
# WEB API (Application Programming Interface for the web)
#
# 1. Ask the user for their query
# 2. Build a URL to talk to the YT API to get hte information
# 3. Convert that info from JSON into something we can use
# 4. Find and print the titles and descriptions
#


BASE_YOUTUBE_URL ='https:\\wwww.googleapis.com/youtube/v3/search?'


# URL encoding (percent encoding)
# * spaces are replaced with +
# * other special characters are replaced with %, followed by the character by the
#
#     
#       *decimal (base 10): 0123456789
#       *hexadecimal (base 16):0123456789ABCDEF
#           (3D)16 = (13*1) + (3*16) = 61(10)
#
#
#
# WEB API (Application Programming Interface for the web)
#


def read_search_query() -> str:
    return input('Query: ')

def build_search_url(query: str) -> str:
    query_parameters = [
        ('key', YOUTUBE_API_KEY), ('type', 'video'),
        ('part', 'snippet'), ('maxResults', 10),
        ('q', query)
    ]
    return BASE_YOUTUBE_URL + '?' + urllib.parse.urlencode(query_parameters)

def get_youtube_result(url: str) -> '???':
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-e')
        return json_text

    finally:
        if response != None:
            response.close()
            
YOUTUBE_API_KEY = 'AIzaSyBXYtvuhA_edW_FPyzr5gS__Oi6xWGwF5I'

if __name__ == '__main__':
    
