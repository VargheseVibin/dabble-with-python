fruits = ["Apple", "Pear", "Orange" ]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error:
        # print(f"Provided Index {error} does not exist in the List")
        print("F ruit Pie")
    else:
        print(fruit + " pie")

make_pie(4)