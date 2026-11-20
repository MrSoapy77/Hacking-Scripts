import os
from tkinter import *
from tkinter import messagebox

import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def tell_weather():

    # Read the key from the environment so it is never committed to git.
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        messagebox.showerror(
            "Error", "Set the OPENWEATHER_API_KEY environment variable first.")
        return

    city_name = city_field.get()

    try:
        # units=metric makes the API return Celsius directly.
        response = requests.get(
            BASE_URL,
            params={"q": city_name, "appid": api_key, "units": "metric"},
            timeout=10)
        x = response.json()
    except (requests.RequestException, ValueError):
        messagebox.showerror(
            "Error", "Could not reach the weather service. Check your connection.")
        return

    # The API returns cod as an int on success and a string on errors,
    # so compare as strings. Any non-200 (bad key, rate limit, unknown
    # city) has no "main" section to read.
    if str(x.get("cod")) == "200":

        clear_all()
        city_field.insert(0, city_name)

        y = x["main"]

        current_temperature = y["temp"]
        finalTemp = round(current_temperature, 2)

        current_pressure = y["pressure"]

        current_humidiy = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
        min2 = round(y["temp_min"], 2)
        max2 = round(y["temp_max"], 2)

        temp_field.insert(15, str(finalTemp) + " °C")
        atm_field.insert(10, str(current_pressure) + " hPa")
        humid_field.insert(15, str(current_humidiy) + " %")
        desc_field.insert(10, str(weather_description))
        min_field.insert(15, str(min2) + " °C")
        max_field.insert(15, str(max2) + " °C")

    elif str(x.get("cod")) == "404":

        messagebox.showerror(
            "Error", "City Not Found \n"
            "Please enter valid city name")

        city_field.delete(0, END)

    else:

        messagebox.showerror(
            "Error", x.get("message", "Unexpected response from the weather service."))


def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    min_field.delete(0, END)
    max_field.delete(0, END)

    city_field.focus_set()


if __name__ == "__main__":

    root = Tk()

    root.title("Weather Predicter")

    root.configure(background="light grey")

    root.geometry("745x685")

    headlabel = Label(root,
                      text="Weather Predictor",
                      fg='red',
                      bg='light pink',
                      font="Times 24",
                      padx="10",
                      pady="10")

    label1 = Label(root,
                   text="City name : ",
                   fg='red',
                   bg='light pink',
                   font="Times 16")

    label2 = Label(root,
                   text="Temperature :",
                   fg='red',
                   bg='light pink',
                   font="Times 16")

    label3 = Label(root,
                   text="atm pressure :",
                   fg='red',
                   bg='light pink',
                   font="Times 16")

    label4 = Label(root,
                   text="humidity :",
                   fg='red',
                   bg='light pink',
                   font="Times 16")

    label5 = Label(root,
                   text="description  :",
                   fg='red',
                   bg='light pink',
                   font="Times 16")
    label6 = Label(root,
                   text="Minimun Temp",
                   fg='red',
                   bg='light pink',
                   font="Times 16")
    label7 = Label(root,
                   text="Maximum Temp",
                   fg='red',
                   bg='light pink',
                   font="Times 16")

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=3, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    label4.grid(row=5, column=0, sticky="E")
    label5.grid(row=6, column=0, sticky="E")
    label6.grid(row=7, column=0, sticky="E")
    label7.grid(row=8, column=0, sticky="E")

    city_field = Entry(root, font="Calibri 18")
    temp_field = Entry(root, font="Calibri 18")
    atm_field = Entry(root, font="Calibri 18")
    humid_field = Entry(root, font="Calibri 18")
    desc_field = Entry(root, font="Calibri 18")
    min_field = Entry(root, font="Calibri 18")
    max_field = Entry(root, font="Calibri 18")

    city_field.grid(row=1,
                    column=1,
                    ipadx="150",
                    ipady="7",
                    padx="10",
                    pady="10")
    temp_field.grid(row=3,
                    column=1,
                    ipadx="150",
                    ipady="7",
                    padx="10",
                    pady="10")
    atm_field.grid(row=4,
                   column=1,
                   ipadx="150",
                   ipady="7",
                   padx="10",
                   pady="10")
    humid_field.grid(row=5,
                     column=1,
                     ipadx="150",
                     ipady="7",
                     padx="10",
                     pady="10")
    desc_field.grid(row=6,
                    column=1,
                    ipadx="150",
                    ipady="7",
                    padx="10",
                    pady="10")
    min_field.grid(row=7,
                   column=1,
                   ipadx="150",
                   ipady="7",
                   padx="10",
                   pady="10")
    max_field.grid(row=8,
                   column=1,
                   ipadx="150",
                   ipady="7",
                   padx="10",
                   pady="10")

    button1 = Button(root,
                     text="Submit",
                     bg="red",
                     fg="black",
                     command=tell_weather,
                     font="Times 18")

    button2 = Button(root,
                     text="Clear",
                     bg="red",
                     fg="black",
                     command=clear_all,
                     font="Times 18")

    button1.grid(row=2, column=1)
    button2.grid(row=10, column=1)

    root.mainloop()
