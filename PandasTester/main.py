import pandas

df = pandas.read_csv("scores.csv")

# print(df)
# print(df.Name)

dct = df.to_dict(orient="rows")
print(dct[0])
print(dct[0]["Name"])
print(df.Score.to_list())
print(df.Score.to_dict())

