import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # Add some padding on both axes for better visibility

# Create Label and Modify Text
my_label = tkinter.Label(text="This is a Label", font=("Arial", 15, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Label"
my_label.config(text="New Label again modified")
my_label.config(padx=10, pady=10)

# Button
def button_clicked():
    my_label.config(text="Button is clicked!")



button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


# Entry
input = tkinter.Entry(width=40)
input.grid(column=3, row=3)
print(input.get())  # Although nothing gets printed here!

# Another Button
button1 = tkinter.Button(text="Click Me(SecondButton)", command=button_clicked)
button1.grid(column=2, row=0)



window.mainloop()
