import requests 

location= input("Enter your city: ")
url=f"http://api.weatherapi.com/v1/forecast.json?key=ebf1fd2fa7ca497eb41100000262410&q={location}"

response=requests.get(url)

#print(response.status_code)

if response.status_code == 200:
    data=response.json()
    print(data["current"]["temp_c"])
    print(data["current"]["condition"]["text"])
    print(f"In {location}, the weather is {data["current"]["condition"]["text"]} and the temperature is {data["current"]["temp_c"]} degrees Celsius")
else: 
    print("Something went wrong")