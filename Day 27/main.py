from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(height=100, width=230)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Labels
km_label = Label(text="0", font=("Arial", 12))
km_label.grid(column=1, row=1)

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

miles_label = Label(text="miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

km_text_label = Label(text="km", font=("Arial", 12))
km_text_label.grid(column=2, row=1)

# Button

def i_got_clicked():
    miles = int(entry.get())
    km = round(miles * 1.6)
    km_label['text'] = km


button = Button(text="Calculate", command=i_got_clicked)
button.grid(column=1, row=2)



window.mainloop()
