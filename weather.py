from cProfile import label
from cgitb import text
import json
from json.tool import main
from multiprocessing import Condition
import tkinter as tk
import requests
from tkinter import font 
import time 
def getWeather(canvas) :
    city = textfield.get()
    api = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&q=' + city +' &appid=b18ea7d12863214eef4a0e89c428f225'
    json_data = requests.get(api).json()
    Condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)

    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 19080))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 19080))

    final_info = Condition + '\n' + str(temp) + '°C'
    final_data = '\n' + 'MAX TEMP:  ' + str(max_temp) + '\n' + 'MIN TEMP: ' + str(min_temp) + '\n' +  'pressure: ' + str(pressure) + '\n' + 'humidity: ' + str(humidity) + '\n' + 'wind speed:' + str(wind) + '\n' + 'sunrise: ' + sunrise + '\n' + 'sunset: ' + sunset

    label1.config(text = final_info)
    label2.config(text = final_data)



canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('weather app')

f = ('poppins', 15, 'bold')

t = ('poppins', 35, 'bold')

textfield = tk.Entry(canvas, font = t )

textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather) 

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f )
label2.pack()

canvas.mainloop()

