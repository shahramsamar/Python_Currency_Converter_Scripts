# importing needed modules
import requests
import json
import pyttsx3

# creating tts engine for pyttsx
engine = pyttsx3.init()

# requesting bitcoin chart price from coindesk api
r = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')

# creating json/dictionary object out of json string
data = json.loads(r.text)

# fetching bitcoin price inside the dictionary keys
btc_price = data['bpi']['USD']['rate']

# converting the data type of the price to integer format
btc_price = int(float(btc_price.replace(',', '')))

# making the order to say a sentence
engine.say("bitcoin price is {}".format(btc_price))

# showing the text as output in console
print("bitcoin price is {}".format(btc_price))

# signaling the engine to read the income text
engine.runAndWait()