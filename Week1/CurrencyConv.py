import requests
import json

# API Call to fetch currency data(symbols and values) from currencyapi.com
response_API = requests.get(
    "https://api.currencyapi.com/v3/latest?apikey=MrlfIugPXbWwLEW3kIfcihZVJXCIPn1E6gncTaOc"
)

data_json = response_API.text  # Fetched data converted to string(json)
data_dict = json.loads(data_json)  # Converts the string to dictionary format
country_list = list(data_dict["data"].keys())
print("The list of currency symbols: \n", country_list)

# Taking inputs from user
base = input("Enter the base currency: ")
conv = input("Enter the converted currency: ")
amount = int(input("Enter the amount to be converted: "))

# Fetching specific values of country from dictionary data_dict
base_v = data_dict["data"][base]["value"]
conv_v = data_dict["data"][conv]["value"]

# Calculation part
ans = amount * (conv_v / base_v)
print(ans)
