import requests
import json
# respone_API = requests.get('https://animechan.vercel.app/api/random').text  # random QUOTES Api
# respone_API = requests.get('https://animechan.vercel.app/api/quotes').text  # random QUOTES Api
# respone_API = requests.get('https://animechan.vercel.app/api/quotes/character?name=soma').text  # anime character  QUOTES Api
respone_API = requests.get('https://animechan.vercel.app/api/quotes/anime?title=shokugeki').text  # anime title QUOTES Api
# respone_API = requests.get('https://animechan.vercel.app/api/available/anime').text  # ALl  QUOTES Api
# print(respone_API )
# gives response code of API if .text is not mention if text mention it gives data of api

parseJson = json.loads(respone_API)   # convert into dict
print(parseJson)
print(type(parseJson))

# method one for list iteration
# for i in parseJson:
#     print(i)

# method two for list iteration through dict
for i in parseJson:
    for key,value in i.items():
        print(f"{key} = {value}")
    print('-----------------------------------------------------------------')

# This below code is for random anime

# anime = parseJson['anime'][0]      # extract the value from api
# character = parseJson['character'][0]
# quote = parseJson['quote'][0]
# print(f"Anime : {anime}")
# print(f"Character : {character}")
# print(f"Quote : {quote}")