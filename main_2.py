# file = open("my_file.txt")  # Opening file.
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:  # Opening file with "with".
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:  # Write/Append in file.
#     file.write("\nNew text.")

# with open("new_file.txt", mode="w") as file:  # Opening non-existent file creates it.
#     file.write("New text.")

# with open("/Users/FranciscoGP/Desktop/my_file.txt") as file:  # Absolute Path
#     contents = file.read()
#     print(contents)

with open("../../../Desktop/my_file.txt") as file:  # Relative Path
    contents = file.read()
    print(contents)
