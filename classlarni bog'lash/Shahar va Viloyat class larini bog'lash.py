class Shahar:
    def __init__(self,tuman_nomi,xuquqiy_xolati):
        self.tuman_nomi=tuman_nomi
        self.xuquqiy_xolati=xuquqiy_xolati
        
    def get_info(self):
        return f" {self.tuman_nomi} {self.xuquqiy_xolati}"
    
    def get_tuman_nomi(self):
        return self.tuman_nomi
    
    def get_xuquqiy_xolati(self):
        return self.xuquqiy_xolati
    
shahar1=Shahar("Urganch tumani","yahshi")
shahar2=Shahar("Xiva tuman","yahshi")
shahar3=Shahar("Shovat tumani","yahshi")

class Viloyat():
    def __init__(self,nomi,yer_maydoni,aholisi_soni,respublikasi):
        self.nomi=nomi
        self.yer_maydoni=yer_maydoni
        self.aholisi_soni=aholisi_soni
        self.respublikasi=respublikasi
        self.shaharlari_soni=0
        self.shaharlari=[]
        
    def add_shaharlari(self,shahar):
        self.shaharlari.append(shahar)
        self.shaharlari_soni+=1
        
    def get_shaharlar(self):
        return [shahar.get_info() for shahar in self.shaharlari]
    
    def get_shaharlari_num(self):
        return self.shaharlari_soni
    
obj=Viloyat("Xorazim viloyati","6,1 ming km kv","1866,7 000","Toshkent shahri")

shahar1=Shahar("Urganch tumani","yahshi")
shahar2=Shahar("Xiva tuman","yahshi")
shahar3=Shahar("Shovat tumani","yahshi")

obj.add_shaharlari(shahar1)
obj.add_shaharlari(shahar2)
obj.add_shaharlari(shahar3)
    
    
    
    