import requests
import json
#API CALL
resp=requests.get('https://api.currencyapi.com/v3/latest?apikey=MrlfIugPXbWwLEW3kIfcihZVJXCIPn1E6gncTaOc')
data=resp.text   #converted to string
data_new=json.loads(data) #converv to dict class
# print(data_new)
to_print=list(data_new['data'].keys())
print('The list of currency symbols: \n',to_print)
#INPUTS
base=input("Enter the base currency: ")
conv=input("Enter the converted currency: ")
amount=int(input('Enter the amount to be converted: '))
#FETCHING VALUES FROM API JSON(DICT CLASS) FILE
base_v=data_new['data'][base]['value']
conv_v=data_new['data'][conv]['value']
#CALCULATION
ans = amount * (conv_v / base_v)
print(ans)
