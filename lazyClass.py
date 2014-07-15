



class simpleOperations(object):
    def __init__(self, x,y):
# __init__ is initialization operation that calls a class
        self.x = x
        self.y = y
        
    #===========================================================================
    # def productXY(self):
    #     prod = [self.x[i]*self.y[i] for i in range(len(self.x))]
    #     return prod
    # 
    # def addOneX(self):
    #     print self.x
    #     self.x = [self.x[i]+1 for i in range(len(self.x))]
    #     print self.x
    #     return None
    #===========================================================================
    
    def differenceXY(self):
        diff = [self.x[i]-self.y[i] for i in range(len(self.x))]
        return diff
    
    def addOneX(self):
      
        self.x = [self.x[i]+1 for i in range(len(self.x))]
        
        return None
    
x = [2,5,3]
y = [4,5,7]

randObj = simpleOperations(x,y)
prod = randObj.differenceXY()


print prod



