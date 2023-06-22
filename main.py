import secrets # Main Sauce
import os # Search Directory
secretsGenerator = secrets.SystemRandom() #Uses systems strongest available random generator

def secure_generator(files):
    secure_choice = secretsGenerator.choice(files)
    return secure_choice

Directory = input("Enter Directory Path: ") + '/'

ls = os.listdir(Directory)
if ls != []:
    print('Files: ', end='')
    print(*ls, sep='\n')
    print('')
    print(f'Secure File Choice: {secure_generator(ls)}')
else:
    print('Invalid path or Directory Empty... Exiting.')