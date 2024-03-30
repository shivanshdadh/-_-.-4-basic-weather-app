
from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=61e9cfdf916050255cdac4ae93b72b4c").json()
    W_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_celsius = round(data["main"]["temp"] - 273.15, 1)  # Convert temperature to Celsius and round to 1 decimal place
    temp_label1.config(text=str(temp_celsius) + " °C")
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather Tech")
win.config(bg="#2C3E50")  # Dark background color
win.geometry("500x570")

name_label = Label(win, text="Basic Weather App", font=("Arial", 30, "bold"), bg="#2C3E50", fg="white")  # Dark background color, white text
name_label.place(x=25, y=50, height=50, width=450)
city_name = StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
com = ttk.Combobox(win, values=list_name, font=("Arial", 14), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

W_label = Label(win, text="Weather Climate", font=("Arial", 20), bg="#2C3E50", fg="white")  # Dark background color, white text
W_label.place(x=25, y=210, height=50, width=210)
W_label1 = Label(win, text="", font=("Arial", 20), bg="#2C3E50", fg="white")  # Dark background color, white text
W_label1.place(x=250, y=210, height=50, width=210)

wb_label = Label(win, text="Weather description", font=("Arial", 17), bg="#2C3E50", fg="white")  # Dark background color, white text
wb_label.place(x=25, y=280, height=50, width=210)
wb_label1 = Label(win, text="", font=("Arial", 17), bg="#2C3E50", fg="white")  # Dark background color, white text
wb_label1.place(x=250, y=280, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Arial", 20), bg="#2C3E50", fg="white")  # Dark background color, white text
temp_label.place(x=25, y=350, height=50, width=210)
temp_label1 = Label(win, text="", font=("Arial", 20), bg="#2C3E50", fg="white")  # Dark background color, white text
temp_label1.place(x=250, y=350, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Arial", 20), bg="#2C3E50", fg="white")  # Dark background color, white text
per_label.place(x=25, y=420, height=50, width=210)
per_label1 = Label(win, text="", font=("Arial", 20), bg="#2C3E50", fg="white")  # Dark background color, white text
per_label1.place(x=250, y=420, height=50, width=210)

done_button = Button(win, text="Done", font=("Arial", 20, "bold"), bg="#2980B9", fg="white", command=data_get)  # Dark blue button with white text
done_button.place(y=490, height=50, width=100, x=200)

win.mainloop()
