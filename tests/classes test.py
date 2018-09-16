quiz= {"meta":{"title":"Computer Quiz","Author":"Joshua Boag"},1:{"How many cores does a computer have":{"1","2","3","4"}}}

class Questions:
    def __init__(self):
        self.question= "Test"
        

for key in quiz:
   print("key: %s , value: %s" % (key, quiz[key]))
