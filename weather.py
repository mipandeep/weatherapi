import urllib.request
import json
import sqlite3

conn = sqlite3.connect('weatherapi.sqlite3')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS WEATHERDATA (TemperatureInCelsius FLOAT NOT NULL  ,
                                                        TemperatureInFahrenheit FLOAT NOT NULL,
                                                        Humidity FLOAT ,
                                                        Pressure INT ,
                                                        temp_min_InCelsius FLOAT,
                                                        temp_min_InFahrenheit FLOAT,
                                                        temp_max_InCelcious FLOAT,
                                                        temp_max_InFahrenheit FLOAT,
                                                        windSpeed INT ,
                                                        weatherDegrees INT ,
                                                        weatherCondition VARCHAR(50) ,
                                                        weatherConditionDiscription VARCHAR(50) )''')

urlData = "https://api.openweathermap.org/data/2.5/weather?q=Winnipeg,Canada&appid=cb6ac7001aec44c5a80bb270d3e71e69"

webUrl = urllib.request.urlopen(urlData)
data = webUrl.read()
theJSON = json.loads(data)

temperatureInCelsius = theJSON["main"]["temp"]-273
temperatureInFahrenheit = (temperatureInCelsius * 1.8)+32
humidity = theJSON["main"]["humidity"]
pressure = theJSON["main"]["pressure"]
speed = theJSON["wind"]["speed"]
deg = theJSON["wind"]["deg"]
weathercondition = theJSON["weather"][0]["main"]
weatherconditiondiscription = theJSON["weather"][0]["description"]
temp_minInCelsius = theJSON["main"]["temp_min"]-273
temp_maxInCelsius = theJSON["main"]["temp_max"]-273
temp_minInFahrenheit = (temp_minInCelsius * 1.8)+32
temp_maxInFahrenheit = (temp_maxInCelsius * 1.8)+32

# query = ("INSERT INTO WEATHERDATA(ID,Temperature,Humidity,Pressure,WindSpeed) VALUES ( "+  (weatherconditiondiscription), (weatherconditiondiscription)  , (weatherconditiondiscription) ,(weatherconditiondiscription) ,(weatherconditiondiscription)+")")

query = "INSERT INTO WEATHERDATA(TemperatureInCelsius,TemperatureInFahrenheit,Humidity,Pressure,temp_min_InCelsius,temp_min_InFahrenheit,temp_max_InCelcious,temp_max_InFahrenheit,windSpeed,weatherDegrees,weatherCondition,weatherConditionDiscription) " \
        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?); "

cur.execute(query, (temperatureInCelsius,temperatureInFahrenheit, humidity,pressure,temp_minInCelsius,temp_minInFahrenheit,temp_maxInCelsius,temp_maxInFahrenheit,speed,deg,weathercondition,weatherconditiondiscription))

# cur.execute(query)
conn.commit()


def printResults(data):

    theJSON = json.loads(data)

    if "lon" in theJSON["coord"]:
        print(theJSON["coord"]["lon"])
        print("----------------\n")

    lat = theJSON["coord"]["lat"]
    print(theJSON["coord"]["lat"])
    print("----------------\n")

    weathercondition = theJSON["weather"][0]["main"]
    print(theJSON["weather"][0]["main"])
    print("----------------\n")

    weatherconditiondiscription = theJSON["weather"][0]["description"]
    print(theJSON["weather"][0]["description"])
    print("----------------\n")

    temperature = theJSON["main"]["temp"]
    print(theJSON["main"]["temp"])
    print("----------------\n")

    humidity = theJSON["main"]["pressure"]
    print(theJSON["main"]["pressure"])
    print("----------------\n")

    pressure = theJSON["main"]["humidity"]
    print(theJSON["main"]["humidity"])
    print("----------------\n")

    temp_min = theJSON["main"]["temp_min"]
    print(theJSON["main"]["temp_min"])
    print("----------------\n")

    temp_max = theJSON["main"]["temp_max"]
    print(theJSON["main"]["temp_max"])
    print("----------------\n")

    speed = theJSON["wind"]["speed"]
    print(theJSON["wind"]["speed"])
    print("----------------\n")

    deg = theJSON["wind"]["deg"]
    print(theJSON["wind"]["deg"])
    print("----------------\n")

def main():

    urlData = "https://api.openweathermap.org/data/2.5/weather?q=Winnipeg,Canada&appid=cb6ac7001aec44c5a80bb270d3e71e69"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))

    if(webUrl.getcode()== 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("received error, cannot parse results")

if __name__ == "__main__":
    main()