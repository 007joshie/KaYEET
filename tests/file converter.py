import json,glob

for file in glob.glob("*.json"):
    with open(file) as f:
        data = json.load(f)
    with open(str(file.split(".")[0])+".YEET",'w') as x:
        json.dump(data,x)

print(data,file.split(".")[0])
