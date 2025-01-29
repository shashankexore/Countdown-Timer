import time
import tkinter as tk
from threading import Thread

def start_countdown():
    try:
        t = int(entry.get())
        countdown_thread = Thread(target=countdown, args=(t,))
        countdown_thread.start()
    except ValueError:
        label.config(text="Enter a valid number")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        time.sleep(1)
        t -= 1
    label.config(text="Fire in the hole!!")

# Create GUI window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# UI Elements
label = tk.Label(root, text="Enter time in seconds", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

button = tk.Button(root, text="Start Countdown", command=start_countdown, font=("Arial", 12))
button.pack(pady=10)

# Run the application
root.mainloop()
