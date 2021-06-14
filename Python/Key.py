"""
SEQUENCES
    List [] - Tuples {} - Dictionary {}
    key:value
"""

data = {1:{'name':'Hilman', 'age': '17', 'hobby' : 'sing'},
        2: {'name': 'Jhonny', 'age': '47', 'hobby': 'eating sugar'}}

for key, value in data.items():
    print("\nKeynya: ", key)
    for key2 in value:
        print(key2 + "-", value[key2])