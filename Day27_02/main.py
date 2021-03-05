import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Create Label and Modify Text
my_label = tkinter.Label(text="This is a Label", font=("Arial", 15, "bold"))
my_label.pack()

my_label["text"] = "New Label"
my_label.config(text="New Label again modified")


# Button
def button_clicked():
    my_label.config(text="Button is clicked!")
    my_label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = tkinter.Entry(width=40)
input.pack()
print(input.get())  # Although nothing gets printed here!




window.mainloop()
