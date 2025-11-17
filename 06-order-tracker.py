# 06-order-tracker.py
import tkinter as tk
from tkinter import ttk
import datetime

root = tk.Tk()
root.title("CraftHaven - Order Tracker")
root.geometry("600x400")
root.configure(bg="#fffaf0")

title = tk.Label(root, text="Order Tracker", font=("Arial", 20, "bold"), bg="#fffaf0", fg="#d84315")
title.pack(pady=20)

frame = tk.Frame(root, bg="#fffaf0")
frame.pack()

tk.Label(frame, text="Order ID:", bg="#fffaf0").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1)

status_label = tk.Label(root, text="", font=("Arial", 14), bg="#fffaf0", fg="#e91e63")
status_label.pack(pady=20)

def track():
    order_id = entry.get()
    if order_id:
        statuses = ["Processing", "Shipped", "Out for Delivery", "Delivered"]
        status = random.choice(statuses)
        date = datetime.datetime.now().strftime("%d %b %Y")
        status_label.config(text=f"Order #{order_id}\nStatus: {status}\nExpected: {date}")
    else:
        status_label.config(text="Please enter Order ID")

tk.Button(root, text="Track Order", command=track, bg="#d84315", fg="white", font=("Arial", 12), padx=20).pack(pady=20)

root.mainloop()
