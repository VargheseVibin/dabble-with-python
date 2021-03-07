from tkinter import *

window = Tk()
window.title("Mils to Kms Converter")
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)


def convert_miles_to_km():
    miles = input_miles.get()
    kms = (int(miles)*1.609)
    show_result(kms)


def show_result(kms):
    kms_val_label.config(text=kms)


input_miles = Entry(width=10)
input_miles.insert(END, string="0")
miles_label = Label(text="Miles", font=("Arial", 16))
is_eq_label = Label(text="is equal to", font=("Arial", 16))
kms_val_label = Label(text="0", font=("Arial", 16, "bold"))
kms_label = Label(text="Km(s)", font=("Arial", 16))
calc_button = Button(text="Calculate", command=convert_miles_to_km)


input_miles.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)
is_eq_label.grid(row=1, column=0)
kms_val_label.grid(row=1, column=1)
kms_val_label.config(padx=10, pady=10)
kms_label.grid(row=1, column=2)
calc_button.grid(row=2,column=1)
calc_button.config(padx=10, pady=10)



window.mainloop()