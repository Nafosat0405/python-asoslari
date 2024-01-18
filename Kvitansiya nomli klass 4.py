class Kvitansiya:
    def __init__(self,raqami,sana,pul_miqdori,manzili):
        self.raqami=raqami
        self.sana=sana
        self.pul_miqdori=pul_miqdori
        self.manzili=manzili
        
    def get_info(self):
        return f"{self.raqami},{self.sana},{self.pul_miqdori},{self.manzili}"
    def set_manzili(self,x):
        self.manzili=x
        
obj1=Kvitansiya(8976,"30.05.2004",100000,"Beruniy ko'chasi 1-yolak 45-uy")
        