import json
import random
f = open("db.json")
db = json.load(f)
question = random.choice(db['questions'])
print("Q. "+question['text'])
options = question['options']
random.shuffle(options)
c=65
for option in options:
    print(chr(c)+") "+option)
    c+=1
ans = input().upper()
if options[ord(ans)-65] == question['correct']:
    print("Correct!")
else:
    print("Wrong!")
f.close()