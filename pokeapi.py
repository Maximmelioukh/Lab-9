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