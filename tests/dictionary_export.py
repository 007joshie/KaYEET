import json
from random import randint

#Quiz= {'meta':{'author':"unknown","title":"unknown",'length':4},'questions':{}}
Quiz={}
title="Example Title"
Quiz.update({'meta':{'author':"unknown","title":"unknown",'length':4}})
Quiz.update({'questions':{}})
for i in range(1,5):
    Quiz['questions'].update({"Q"+str(i):{'question':title+str(i)}})
    Quiz['questions']["Q"+str(i)].update({'choices':[]})
    Quiz['questions']["Q"+str(i)].update({'answer':randint(1,4)})
    for v in range(1,5):
        Quiz['questions']["Q"+str(i)]['choices'].append("Something"+str(v))

Quiz["meta"]['length']=5 
print(Quiz)
print(Quiz['questions']["Q1"]['choices'][0])

with open("quiz1.json", "w") as jsonFile:
    json.dump(Quiz, jsonFile)
