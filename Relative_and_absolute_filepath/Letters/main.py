place = "[names]"

with open("./python_mini_projects/Mail_merge/Names/invited_names.txt") as names_file:
          names = names_file.read()
          
          
with open("./python_mini_projects/Mail_merge/Letters/starting_letter.txt") as letter_files:
    letter_contents = letter_files.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(place,stripped_name)
        with open("./python_mini_projects/Mail_merge/ReadyToSend/letter_for_{stripped_name}.txt",mode = "w") as completed_letter:
            completed_letter.write(new_letter)
        