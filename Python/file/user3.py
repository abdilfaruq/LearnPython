"""
    WORK WITH JSON
"""
import json

"""
-write-
data = {}
data['member'] = [
        {'nama' : 'jackies', 'skill': 'tendangan beracun'},
        {'nama' : 'yip', 'skill': 'wingchun'},
        {'nama' : 'songoku', 'skill': 'kamekameha'}
]

with open('member.txt', 'w') as memberfile:
    json.dump(data, memberfile)
"""

with open('member.txt', 'r') as memberfile:
    data = json.load(memberfile)

    for member in data['member']:
        print('namanya adalah ' + member['nama'] + ' punya skill: ' + member['skill'])