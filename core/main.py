import requests

input_amount = float(input("Enter  the amount of your currency :"))
base_currency = input("Enter  the amount of your currency :")
target_currency = input("Enter  the amount of your currency :")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {"ids": base_currency, "vs_currencies": target_currency}

response = requests.get(url, params=params)

data = response.json()

base_target_amount = data[base_currency][target_currency]

result = input_amount * base_target_amount

print("result:", result)
