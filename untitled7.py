class Korabl:
    def __init__(self,ismi,suvsiljishi,turi,yoshi):
        self.ismi=ismi
        self.suvsiljishi=suvsiljishi
        self.turi=turi
        self.yoshi=yoshi
        
    def get_info(self):
        return f"{self.ismi}.{self.suvsiljishi}.[self.turi}.{self.yoshi}"
    
    def set_turi(self,x):
        self.turi=x
        
obj1=Korabl()