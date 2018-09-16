data= {"meta":{"title":"Computer Quiz","author":"Joshua Boag","length": 3},"questions":{"Q1":{"question":"How many","choices":["1","2","3","4"]},"Q2":{"question":"Where many","choices":["1","2","three","4"]},"Q3":{"question":"How much","choices":["one","2","3","4"]}}}

class Questions:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
quiz= Questions(**data)

for i in range(1,int(quiz.meta['length'])+1):
    print(i,quiz.questions["Q"+str(i)]['question'])



