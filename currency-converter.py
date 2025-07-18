import requests
from tkinter import *
from tkinter import ttk # It is sub-module in tkinter - So can't imported in upper line.
import tkinter.messagebox as tmsg


def converter():
    try:
        amount=float(amount_entry.get())
        from_curr=from_currency.get()
        to_curr=to_currency.get()
        api_key = "f0d51b48220510cc2f0c4fed"
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_curr}"
        response = requests.get(url)

        if response.status_code==200:
            data = response.json()
            rate=data['conversion_rates'][to_curr]
            converted=round(amount*rate,2)  # Main Calculation-

            result_label.config(text=f"{amount} {from_curr}={converted} {to_curr}")
            result_label.focus_set()
            to_currency.selection_clear()
            from_currency.selection_clear()
            amount_entry.selection_clear()

        else:
            tmsg.showerror("Error", "Invalid API response")



    except ValueError:
        tmsg.showwarning("Input Error", "Please enter a valid amount.")
    except Exception as e:
        tmsg.showerror("Error", str(e))


# Window Set-up
root = Tk()
root.title("Currency Converter")
root.geometry("410x330")
root.config(padx=20, pady=20,bg="#f0f8ff")
root.resizable(False, False)
root.iconbitmap("logo.ico")

# Heading
heading = Label(root, text="   💱 Currency Swap Tool", font=("Helevetica", 18, "bold"),bg="#f0f8ff",fg="#333")
heading.grid(row=0, column=0, columnspan=2, pady=10,padx=10)

# Amount Entry
amount_label =Label(root, text="Enter your Amount:",font=("Calibri", 13))
amount_label.grid(row=1, column=0, sticky="e", pady=15)

amount_entry = Entry(root, width=20,font=("Calibri", 11))
amount_entry.grid(row=1, column=1, pady=10)

# From Currency
from_label = Label(root, text="From Currency:",font=("Calibri", 13))
from_label.grid(row=2, column=0, sticky="e", pady=5)

from_currency =ttk.Combobox(root, values=["INR", "USD", "EUR", "GBP", "JPY"], state="readonly")
from_currency.grid(row=2, column=1, pady=10)
from_currency.set("INR")

# To Currency
to_label = Label(root, text="To Currency:",font=("Calibri", 13))
to_label.grid(row=3, column=0, sticky="e", pady=10)

to_currency = ttk.Combobox(root, values=["INR", "USD", "EUR", "GBP", "JPY"], state="readonly")
to_currency.grid(row=3, column=1, pady=10)
to_currency.set("USD")

# Convert Button
convert_btn = Button(root, text="Convert", command=converter,width=15,bg="#1e90ff",fg="white",font=("Calibri", 11))
convert_btn.grid(row=4, column=1, columnspan=2, pady=15)

# Result Label
result_label = Label(root, text="", font=("Calibri", 12, "bold"),fg="blue")
result_label.grid(row=5, column=1, columnspan=2, pady=10)

root.mainloop()