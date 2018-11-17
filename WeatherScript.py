import requests
import json

r = requests.get('http://api.openweathermap.org/data/2.5/group?id=5376803,5350734,5404555,5355933,5392263,5378538,5322850,5327684,5383777,5344157,5367440,5346462,5322737,5382514&APPID=1fd72dd7a34bc3ecd8949e020b0921a2')

weather_data = r.json()

data = json.dumps(weather_data)

def printData():
        city = [] # Not used yet.... 
        for x in range(0,13):
                y =  weather_data['list'][x]['name']
                print y

printData()


