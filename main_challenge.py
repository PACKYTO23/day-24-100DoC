#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []

with open("Input/Names/invited_names.txt") as name_data:
    names_raw = name_data.readlines()
    for name in names_raw:
        clean_name = name.strip()
        names_list.append(clean_name)

for name in names_list:
    with open("Input/Letters/starting_letter.txt") as letter_data:
        letter_raw = letter_data.read()
        final_letter = letter_raw.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(final_letter)
