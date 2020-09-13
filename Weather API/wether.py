import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=YOUR_API_KEY&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['main']
# print(formatted_data)
print(json_data)
