from tkinter import *
from tkinter import font
import requests


def fetchweather():
    city = citytext.get()
    link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&units=metric&appid=22515dbe8047cf659da74a1cae281c2e"
    response = requests.get(link)
    json = response.json()
    location_label["text"]="{} , {}".format(json["name"],json["sys"]["country"])
    temp_label["text"]="Temperature: {} °C".format(json["main"]["temp"])

app = Tk()
app.title("Weather")
app.geometry("700x350")


citytext = StringVar()
city_entry = Entry(app, textvariable=citytext)
city_entry.pack()

searchbutton = Button(app, text="Search", width=10,
                      height=4, command=fetchweather)
searchbutton.pack()

location_label = Label(app,text=" ",font=("bold",20))
location_label.pack()

temp_label = Label(app,text=" ",font=("bold",20))
temp_label.pack()


app.mainloop()
