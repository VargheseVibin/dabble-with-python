import pandas

with open(file="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", mode="r") as c_file:
    census_data_frame = pandas.read_csv(c_file)
    print(census_data_frame.index)
    print(census_data_frame.columns)

    gray_squirrel_list = census_data_frame[census_data_frame["Primary Fur Color"] == "Gray"]
    gray_squirrel_count = len(gray_squirrel_list)
    red_squirrel_list = census_data_frame[census_data_frame["Primary Fur Color"] == "Cinnamon"]
    red_squirrel_count = len(red_squirrel_list)
    black_squirrel_list = census_data_frame[census_data_frame["Primary Fur Color"] == "Black"]
    black_squirrel_count = len(red_squirrel_list)

    primary_fur_color_data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
                                   "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]}

    primary_fur_color_data_frame = pandas.DataFrame(primary_fur_color_data_dict)
    primary_fur_color_data_frame.to_csv("squirrel_count.csv")
