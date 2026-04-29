import tkinter as tk
from PIL import Image, ImageTk
import requests

window = tk.Tk()
window.title("Tkinter Test")
window.geometry("300x200")
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=20)

frame = tk.Frame(window)
frame.pack(pady=20)

def on_button_click():
   label.config(text="Button Clicked!")

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

label = tk.Label(window)
label.place(x=100, y=100)

image_path = "cortisol.jpeg"
opened_img = Image.open(image_path)

tkinter_img = ImageTk.PhotoImage(opened_img)

window.mainloop()