"""
FUNCTIONS
    Parameter/Argumen default
    Lebih dari 1 parameter
    Parameter return
    Keyword argumen
    *Args, **Kwargs
"""

def printNiceText(text = 'kosong'):
    print('-----')
    print(text)
    print('-----')

def hitung(a, b):
    print('Jumlah a dan b adalah ', a + b)

def hitung(a, b):
    return a+b
hasil1 = hitung(10, 20)

def printData(name, hobby):
    print("Name: " + name + " - Hobby: " + hobby)

def printNama(*args):
    for name in args:
        print(name)

def printData2(**kwargs):
    for key, value in kwargs.items():
        print(key + "- " + value)

printNiceText('sekolahkoding')
hitung(10,20)
print(hitung(hasil1, 50))
printData(hobby='nyanyi', name='hilman')
printNama('\nhilman', 'yasman', 'nona', 'arki')
printData2(name = 'hilman', age='21', hobby = 'nyanyi')