# A program that opens all .txt files in a folder and searches 
# for any line that matches a user-supplied regular expression, 
# then prints the results to the screen. (i guess i'll do a function to it)

from pathlib import Path
import re 

#Welcome to user, and the phrase we're looking for
print('Hello Sir. Which phrare are we looking for?')
phrase = input('Type the phrase: ').strip()

pattern = re.compile(phrase)    #regex that were looking for line by line 


folder_path = Path('C:/Users/...')

#File Path, and the for/while loop statements that will open all the .txt files
for file_name in folder_path.glob('*.txt'):
    found_in_file = False

    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            match = pattern.search(line) 
            if match:
                if not found_in_file:
                    print(f'\n📄 File: {file_name}')
                    found_in_file = True

                print(f'Match: {match.group()}')
                print(f'Line: {line.strip()}')
                