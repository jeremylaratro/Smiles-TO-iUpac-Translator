import csv
import time
from STOUT import translate_forward, translate_reverse


# Simple_CLI is a simple command line interface for the great work done by the creators of the  Smiles-TO-iUpac-Translator (STOUT) and allows users a simple,
# interactive interface when needing to translate SMILES strings or IUPAC names. 


outputs = []

# add_output adds the output of each translation to a list
def add_output(output):
    outputs.append(output)
    return outputs

# add_file initiates prompt for writing translations to text, csv, both, or neither
def add_file():
    print("Would you like to write to (1) text file, (2) CSV file, (3) no file output, or (4) both?")
    output_ans = input()
    if output_ans == '1':
        with open('CLI_translations.txt', 'w') as f:
            f.write(', '.join(outputs))
            print("File written: \nCLI_translations.txt")
    if output_ans == '2':
        with open('CLI_translations.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(outputs)
            print("File written: \nCLI_translations.csv")
    if output_ans == '3':
        pass
    if output_ans == '4':
        with open('translations.txt', 'w') as f:
            f.write(', '.join(outputs))
        with open('translations.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(outputs)
            print("File written")

# restart allows user to restart and perform more translations, or exit
def restart():
    print("Translate another?: \n SMILES -> IUPAC (1) \n IUPAC -> SMILES (2) \n Exit (3)")
    cont = input()
    if cont == '1':
        SMILES_TR()
    if cont == '2':
        IUPAC_TR()
    if cont == '3':
        exit()

# SMILES_TR prompts user to enter SMILES string and outputs IUPAC name
def SMILES_TR():
# SMILES to IUPAC name translation
    print("Please enter the SMILES string:")
    SMILES = input()
    IUPAC_name = translate_forward(SMILES)
    print("IUPAC name of "+SMILES+" is: " + IUPAC_name)
    print("Completed")
    add_output(IUPAC_name)
    add_file()
    restart()

# IUPAC_TR prompts user to enter IUPAC name and outputs SMILES
def IUPAC_TR():
# IUPAC name to SMILES translation
    print("Please enter the IUPAC name:")
    IUPAC = input()
    smiles_translate = translate_reverse(IUPAC)
    print("SMILES of "+IUPAC+" is: " + smiles_translate)
    print("Completed")
    add_output(smiles_translate)
    add_file()
    restart()
    
#Allows user to input text file
def file_out():
    print("Please enter path to file:")
    file_path = input()
    file_in = open(file_path, "r")
    file_out_ = open(file_path.strip('.txt') + "_translated.txt", "w")
    print("Choose translation method: \n(1)SMILES -> IUPAC\n(2)IUPAC -> SMILES")
    tr_choice = input()
    start_time = time.time()
    if tr_choice == '1':
        for i, line in enumerate(file_in):
            smiles_translation = line.strip("''\n")
            IUPAC_name = translate_forward(smiles_translation)
            file_out_.write(IUPAC_name + "\n")
    if tr_choice == '2':
        for i, line in enumerate(file_in):
            iupac_translation = line.strip("''\n")
            SMILES_str = translate_reverse(iupac_translation)
            file_out_.write(SMILES_str + "\n")
    end_time = time.time()
    print("Total time: " + str(end_time - start_time) + "seconds")
    print("File written to " + file_path.strip('.txt') + "_translated.txt")
    file_in.close()
    file_out_.close()
    
# start prompts user to choose between SMILES to IUPAC or IUPAC to SMILES translation
def start():
    print("Input method:\n(1) Manual (CLI) \n(2) File")
    choice_inp = input()
    if choice_inp == '1':
        print("Would you like to convert: \n (1) SMILES -> IUPAC or \n (2) IUPAC -> SMILES?")
        choice = input()
        if choice == '1':
            SMILES_TR()
        if choice == '2':
            IUPAC_TR()
        else:
            print('Invalid, please ensure that there are no spaces and try again')
            return choose()
    if choice_inp == '2':
        file_out()


start()
