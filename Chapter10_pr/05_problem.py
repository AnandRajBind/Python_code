from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    
    def book(self,fro,to):
        print(f"Ticket is booked in train no {self.trainNo} from {self.fro} to {self.to}")
        
    def getStatus(self,trainNo):
        print(f"Train no {trainNo} is running on time")
        
    def getFare(self,fro, to):
        print(f"Fare for train no {trainNo} from {fro} to {to} is {randint(100,500)}")
        
        
t=Train(12345)
t.book("Delhi","Mumbai")
t.getStatus("Delhi","Mumbai")
t.getFare("Delhi","Mumbai")