# FILE I/O

"""
-write-
file = open('data.txt', 'w')
file.write("Halo Halo Bandung")
text = file.read()
print(text)
"""

"""
-read+-
file = open('data.txt', 'r+')
file.write("Halo Halo Makassar")
text = file.read()
print(text)
"""

"""
-a+-
file = open('data.txt', 'a+')
file.write("Data Baru Bos")
text = file.read()
print(text)
"""

file = open('data.txt', 'a+')
file.write('\nnew life!!')
file.seek(0)
text = file.read()
print(text)