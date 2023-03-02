import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import tkinter as tk


def usd():
    try:
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date="
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        usd_rate = soup.find('rate').text
        number_label.config(text=usd_rate)
    except Exception as e:
        print("Error fetching USD rate:", e)

def eur():
    try:
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date="
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        eur_rate = soup.find('rate').text
        number_label.config(text=eur_rate)
    except Exception as e:
        print("Error fetching EUR rate:", e)


window = tk.Tk()
window.title("Курс валют")
window.geometry("300x200")
usd_button = tk.Button(window, text="USD", fg="white", bg="red", padx=10, pady=5, command=usd)
eur_button = tk.Button(window, text="EUR", fg="white", bg="red", padx=10, pady=5, command=eur)
usd_button.pack(pady=10)
eur_button.pack(pady=10)
number_label = tk.Label(window, text="0", font=("Helvetica", 48), fg="blue")
number_label.pack(pady=20)

window.mainloop()
