# Local dan Global VAR


"""
name = "hilman"

def printName():
    global name
    name = name + " cheesky"
    print("akses dari dalam " + name)

printName()
print("akses dari luar " + name)
"""

name = "hilman"

def printName():
    name = "cheesky"
    print("akses dari dalam " + name)

printName()
print("akses dari luar " + name)