class Ustoz:
    def __init__(self,ismi,yoshi,maktab,sinf):
        self.ismi=ismi
        self.yoshi=yoshi
        self.maktab=maktab
        self.sinf=sinf
        
    def get_info(self):
        return f"{self.ismi},{self.maktab},{self.sinf}"
    
    def set_sinf(self,x):
        self.sinf=x
        
obj1=Ustoz("Sevara",40,"16-son","4-G")
