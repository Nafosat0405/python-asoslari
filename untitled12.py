class Telefon:
    def __init__(self,abonet_ismi,raqami,manzili,turi):
        self.abonet_ismi=abonet_ismi
        self.raqami=raqami
        self.manzili=manzili
        self.turi=turi
        
        
    def get_info(self):
        return f"{self.abonet_ismi},{self.raqami},{self.manzili}"
    
    def set_raqami(self,x):
        self.raqami=x
        
obj1=Telefon("Nafosat","93-248-30-64","Urganch shahri","faol")