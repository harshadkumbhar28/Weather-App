from tkinter import *
from tkinter import ttk  # For Combo Box

import requests


def GetData():
    City = CityName.get()
    Data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q="
        + City + "&appid""=3e0749c296346681f4266ed27acc2d6f").json()
    WeatherLabel1.config(text=Data["weather"][0]["main"])
    WeatherDescriptionLabel1.config(text=Data["weather"][0]["description"])
    TemperatureLabel1.config(text=str(int(Data["main"]["temp"] - 273.15)))
    PressureLabel1.config(text=Data["main"]["pressure"])


window = Tk()

window.title("Weather App")  # For App Title
window.config(bg="green")  # For Background Color
window.geometry("500x600")  # Use to set Dimension of Box

LabelName = Label(window, text="~~~Weather App~~~",
                  font=("Times New Roman", 30, "italic bold"))
LabelName.place(x=25, y=50, height=50, width=450)

ListName = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
            "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
            "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
            "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
            "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
            "National Capital Territory of Delhi", "Puducherry"]

CityName = StringVar()
ComboBox = ttk.Combobox(window, values=ListName,
                        font=("Times New Roman", 20, "bold"), textvariable=CityName)
ComboBox.set("Select States")
ComboBox.place(x=25, y=120, height=50, width=450)

DoneButton = Button(window, text="Done",
                    font=("Times New Roman", 20, "bold"), command=GetData)
DoneButton.place(x=200, y=190, height=50, width=100)

WeatherLabel = Label(window, text="Weather Climate",
                     font=("Times New Roman", 20))
WeatherLabel.place(x=25, y=260, height=50, width=210)
WeatherLabel1 = Label(window, text="",
                      font=("Times New Roman", 20))
WeatherLabel1.place(x=250, y=260, height=50, width=210)

WeatherDescriptionLabel = Label(window, text="Weather Description",
                                font=("Times New Roman", 17))
WeatherDescriptionLabel.place(x=25, y=330, height=50, width=210)
WeatherDescriptionLabel1 = Label(window, text="",
                                 font=("Times New Roman", 17))
WeatherDescriptionLabel1.place(x=250, y=330, height=50, width=210)

TemperatureLabel = Label(window, text="Temperature",
                         font=("Times New Roman", 20))
TemperatureLabel.place(x=25, y=400, height=50, width=210)
TemperatureLabel1 = Label(window, text="",
                          font=("Times New Roman", 20))
TemperatureLabel1.place(x=250, y=400, height=50, width=210)

PressureLabel = Label(window, text="Pressure",
                      font=("Times New Roman", 20))
PressureLabel.place(x=25, y=470, height=50, width=210)
PressureLabel1 = Label(window, text="",
                       font=("Times New Roman", 20))
PressureLabel1.place(x=250, y=470, height=50, width=210)

window.mainloop()
