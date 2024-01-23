class Mahsulot:
    def __init__(self,nomi,soni,narxi,mamlakat):
        self.nomi=nomi
        self.__soni=soni
        self.narxi=narxi
        self.mamlakat=mamlakat
        
    def get_num(self):
        return self.__soni
    
    
    def get_name(self):
        return self.nomi
    
    
    def set_narxi(self,x):
        self.narxi=x
        
    def get_info(self):
        return f"{ self.nomi}  {self.__soni}  {self.narxi} {self.mamlakat}"
        
    
mahsulot1=Mahsulot("Pecheniya","200 qadoq",30000,"Uzbekiston")
mahsulot2=Mahsulot("CHocacream","20 qadoq",30000,"Uzbekiston")
mahsulot3=Mahsulot("Cocacola","2 litr",15000,"Uzbekiston")

class Dukon():
    def __init__(self,nomi,manzili,turi):
        self.nomi=nomi
        self.manzili=manzili
        self.turi=turi
        self.mahsulot_soni=0
        self.mahsulot=[]
        
    def add_mahsulot(self,mahsulot):
        self.mahsulot.append(mahsulot)
        self.mahsulot_soni+1
        
    def get_mahsulotlar(self):
        return [mahsulot.get_info() for mahsulot in self.mahsulot]
    
    def mahsulot_num(self):
        return self.mahsulot_soni
    
Oziq_ovqat=Dukon("Yagona","Bobur mahallasi Lochin ko'chasi","Oziq ovqat dukoni")
mahsulot1=Mahsulot("Pecheniya","200 qadoq",30000,"Uzbekiston")
mahsulot2=Mahsulot("CHocacream","20 qadoq",30000,"Uzbekiston")
mahsulot3=Mahsulot("Cocacola","2 litr",15000,"Uzbekiston")


Oziq_ovqat.add_mahsulot(mahsulot1)
Oziq_ovqat.add_mahsulot(mahsulot2)
Oziq_ovqat.add_mahsulot(mahsulot3)
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    