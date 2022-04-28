from xml.etree.ElementInclude import LimitedRecursiveIncludeError
import requests

def getthepokemon(name):
    if name is None:
        return
    name = name.lower().strip()
    if name == '':
        return
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(name))

    print('Getting Pokemon Information...', end = '')
    
    if response.status_code == 200:
     print('Success!')
     return response.json()
    else:
     print('Fialed, Response code:',response.status_code)
     return


    
def get_pokemon_list(limit=2000, offset=0):
    print("Getting list of Pokemon...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    params = {
        'offset': offset,
        'limit': limit
        }
    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        print('Success!')
        poke_dict = response.json()
        return [p['name'] for p in poke_dict['results']]
    else:
        print('Fialed, Response code:',response.status_code)
        


def get_pokemmon_image_url(name):
    poke_dict = getthepokemon(name)
    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url