import requests
import json
import pyttsx3
Request = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
JsRequest = json.loads(Request.text)
bit_coin_UpTime=JsRequest['time']['updated']
bit_coin_price = JsRequest['bpi']['USD']['rate']
print ('The price of Bitcoin at time {} is equal to {}'.format(bit_coin_UpTime , bit_coin_price))
ansForSound = 'The price of Bitcoin at time {} is equal to {}'.format(bit_coin_UpTime , bit_coin_price)
ttsENGIN= pyttsx3.init()
ttsENGIN.say(ansForSound)
ttsENGIN.runAndWait()