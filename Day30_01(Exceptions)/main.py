height = float(input("Height(in meters):"))
weight = int(input("Weight(in kilograms):"))

if height > 2.5:
    raise ValueError("Height cannot be over 2.5m for humans")

bmi = weight / (height ** 2)
print(bmi)
