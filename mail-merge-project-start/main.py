#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
clean_names = []
with open("Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name.strip("\n")
        clean_names += [name]

with open("Input/Letters/starting_letter.docx") as temp_letter:
    temp_letter = temp_letter.read()
    print(temp_letter)
    temp_letters = [temp_letter for name in clean_names]

new_letters = []
#Replace the [name] placeholder with the actual name.
for name, letter in zip(clean_names, temp_letters):
    letter = letter.replace('[name]', name)
    # Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode="w") as completed_letter:
        completed_letter.write(letter)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp