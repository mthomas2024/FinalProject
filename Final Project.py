import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#Global holders
imageFile = None

#Create Window
root = Tk()
root.title("Building Plans Conversion 2")
root.geometry("750x500")

#Display Instructions
title = Label(text="Converter App 2")
title.place(relx=.55, rely=.1, anchor=CENTER)


# Picture Frame
pic = ttk.Frame(root, width=300, height=200)
pic.grid(column=0, row=0)
pic.configure(borderwidth="2")
pic.configure(relief="groove")

# Listbox to display conversion results
results_list = Listbox(root, width=40)
results_list.place(relx=.25, rely=.60, anchor=CENTER)

# Radio Boxes
v = IntVar()
tk.Label(root, text="Convert Measurement").place(relx=.6, rely=.4, anchor=W)

tk.Radiobutton(root, text="Inches to Meters", variable=v, value=0).place(relx=.6, rely=.45, anchor=W)
tk.Radiobutton(root, text="Meters to Inches", variable=v, value=1).place(relx=.6, rely=.5, anchor=W)


class Converter:
    def __init__(self, master):
        global imageFile

        imageFile = "building.png"

        frame = pic
        img = Image.open(imageFile)
        photo = ImageTk.PhotoImage(img.resize((300, 200)))
        lblImage = ttk.Label(frame, image=photo)
        lblImage.image = photo
        lblImage.place(relx=.5, rely=.5, anchor=CENTER)

        self.label_value = tk.Label(master, text="Enter a value and\nchoose conversion:")
        self.label_value.place(relx=.55, rely=.3, anchor=CENTER)

        self.value = tk.Entry(master)
        self.value.place(relx=.8, rely=.3, anchor=CENTER)

        self.button_clear = tk.Button(master, text="Clear", command=self.btnClear)
        self.button_clear.place(relx=.5, rely=.8, anchor=CENTER)

        self.button_calculate = tk.Button(master, text="Convert", command=self.btnConvert)
        self.button_calculate.place(relx=.3, rely=.8, anchor=CENTER)

        self.button_exit = tk.Button(master, text="Exit", command=quit)
        self.button_exit.place(relx=.7, rely=.8, anchor=CENTER)

    def btnClear(self):
        self.value.delete(0, tk.END)
        self.label_value.config(text="Enter a value and\nchoose conversion:")

    def btnConvert(self):
        value = self.value.get()
        if value.replace('.', '', 1).isdigit():  # is numeric?
            value = float(value)
            if value >= 0:  # is positive?
                selection = v.get()
                if selection == 0:  # picked first option?
                    result = round(value * 0.0254, 2)
                    self.label_value.config(text=f"{value} inches is {result} meters")
                    self.label_value.place(relx=.8, rely=.6, anchor=CENTER)
                else:
                    result = round(value * 39.3701, 2)
                    self.label_value.config(text=f"{value} meters is {result} inches")
                    self.label_value.place(relx=.8, rely=.6, anchor=CENTER)
            else:
                self.label_value.config(text="Error: Value must be positive.")
        else:
            self.label_value.config(text="Error: Invalid input. Please enter a valid number.")

    def results_list_add(self, result):
        results_list.insert(tk.END, result)

    def results_list_clear(self):
        results_list.delete(0, tk.END)


def save_results_to_file():
    with open("measures.txt", "w") as file:
        items = results_list.get(0, tk.END)
        for item in items:
            file.write(item + "\n")
    status_label.config(text=f"Saved {len(items)} records to file.")


app = Converter(root)

# Button to save results and to file
def add_to_list():
    app.results_list_add(app.label_value.cget("text"))

button_save_to_file = tk.Button(root, text="Save to File", command=save_results_to_file)
button_save_to_file.place(relx=.3, rely=.9, anchor=CENTER)

button_save_results = tk.Button(root, text="Save Results", command=add_to_list)
button_save_results.place(relx=.5, rely=.9, anchor=CENTER)

button_clear_list = tk.Button(root, text="Clear Results", command=app.results_list_clear)
button_clear_list.place(relx=.7, rely=.9, anchor=CENTER)

status_label = tk.Label(root, text="")
status_label.place(relx=.5, rely=.95, anchor=CENTER)

root.mainloop()
