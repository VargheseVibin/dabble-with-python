with open("file1.txt") as file1:
    file1_lines = file1.read().splitlines()
print(file1_lines)

with open("file2.txt") as file2:
    file2_lines = file2.read().splitlines()
print(file2_lines)

common_nos = [n for n in file2_lines if n in file1_lines]
print(common_nos)
