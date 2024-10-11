import requests
import json
import pyttsx3
import time
def create_message():
    Request = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
    JsRequest = json.loads(Request.text)
    bit_coin_UpTime=JsRequest['time']['updated']
    bit_coin_price = JsRequest['bpi']['USD']['rate']
    ansForSound = 'The price of Bitcoin at time {} is equal to {}'.format(bit_coin_UpTime , bit_coin_price)
    return ansForSound
def sey_text():
    ttsENGIN= pyttsx3.init()
    ttsENGIN.say(create_message())
    ttsENGIN.runAndWait()
while True:
    sey_text()
    time.sleep(100)
