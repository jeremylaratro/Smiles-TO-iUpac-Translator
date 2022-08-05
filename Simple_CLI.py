import csv

from STOUT import translate_forward, translate_reverse


outputs = []
def SMILES_TR():
# SMILES to IUPAC name translation

    print("Please enter the SMILES string:")
    SMILES = input('')
    IUPAC_name = translate_forward(SMILES)
    print("IUPAC name of "+SMILES+" is: "+IUPAC_name)
    print("Completed")
    outputs.append(smiles_translate)
    print("Write to text file? \nYes(1) \n No(2)")
    file_c = input()
    if file_c == '1':
        with open('translations.txt', 'w') as f:
            f.write(', '.join(outputs))
    print("Translate another?: \n SMILES -> IUPAC (2) \n IUPAC -> SMILES (2) \n Exit (3)")
    cont = input()
    if cont == '1':
        SMILES_TR()
    if cont == '2':
        IUPAC_TR()
    if cont == '3':
        exit()


def IUPAC_TR():
# IUPAC name to SMILES translation
    print("Please enter the IUPAC name:")
    IUPAC = input()
    smiles_translate = translate_reverse(IUPAC)
    print("SMILES of "+IUPAC+" is: " + smiles_translate)
    print("Completed")
    outputs.append(smiles_translate)
    print("Write to text file? \nYes(1) \n No(2)")
    file_c = input()
    if file_c == '1':
        with open('translations.txt', 'w') as f:
            f.write(', '.join(outputs))
    print("Translate another?: \n IUPAC -> SMILES (1) \n SMILES -> IUPAC (2) \n Exit (3)")
    cont = input()
    if cont == '1':
        SMILES_TR()
    if cont == '2':
        IUPAC_TR()
    if cont == '3':
        exit()

def choose():
    print("Would you like to convert: \n (1) SMILES -> IUPAC or \n (2) IUPAC -> SMILES?")
    choice = input()
    if choice == '1':
        SMILES_TR()
    if choice == '2':
        IUPAC_TR()
    else:
        print('Invalid, please ensure that there are no spaces and try again')
        return choose()
choose()

