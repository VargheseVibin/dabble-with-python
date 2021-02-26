from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_dict_rec_fmt = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn_dict_rec_fmt = original_data.to_dict(orient="records")
else:
    to_learn_dict_rec_fmt = data.to_dict(orient="records")

#to_learn_dict_def_fmt = data.to_dict()

# print(to_learn_dict_def_fmt)
# print(to_learn_dict_rec_fmt)


def show_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict_rec_fmt)
    # print(current_card["French"])
    # print(current_card["English"])
    canvas.itemconfig(lang_card, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(lang_card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def word_is_known():
    to_learn_dict_rec_fmt.remove(current_card)
    data = pandas.DataFrame(to_learn_dict_rec_fmt)
    data.to_csv("./data/words_to_learn.csv", index=False)
    show_next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
lang_card = canvas.create_image(400, 263, image=card_front_img)     # (400,263 because the canvas needs to loaded at
                                                                    # center, hence 0.5 image size)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=show_next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=word_is_known)
known_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
show_next_card()


window.mainloop()

