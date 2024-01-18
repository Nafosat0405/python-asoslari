class Shaxs:
    def __init__(self,ismi,yoshi,jinsi,millati):
        self.ismi=ismi
        self.yoshi=yoshi
        self.jinsi=jinsi
        self.millati=millati
        
    def get_info(self):
        return f"{self.ismi}.Yoshi:{self.yoshi}.{self.jinsi}. {self.millati}"
    
    def set_millati(self,x):
        self.millati=x
        
obj1=Shaxs("Guli",21,"ayol","uzbek")
