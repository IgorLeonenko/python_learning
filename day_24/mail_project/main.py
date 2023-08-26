#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/names/invited_names.txt") as file:
  read_names = file.readlines()

names = []

for el in read_names:
  names.append(el.replace("\n", ""))

with open("Input/letters/starting_letter.txt") as start_letter:
  letter_content = start_letter.read()
  for name in names:
    new_letter = letter_content.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
      file.write(new_letter)
