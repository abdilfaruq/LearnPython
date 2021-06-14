# FILE I/O

file = open('data.txt', 'a+')

def add_to_list(newText):
    file.write('\n' + newText)
    ask_user()

def ask_user():
    add_to_list(input('Ketik disini '))

ask_user()