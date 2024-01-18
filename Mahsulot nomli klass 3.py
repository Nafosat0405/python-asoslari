class Mahsulot:
    def __init__(self,nomi,soni,narxi,mamlakat):
        self.nomi=nomi
        self.soni=soni
        self.narxi=narxi
        self.mamlakat=mamlakat
        
        
        
    def get_soni(self):
        return self.soni
        
        
    def get_info(self):
        return f"{self.nomi},{self.soni},{self.narxi},{self.mamlakat}"
    
    def set_narxi(self,x):
        self.narxi=self.narxi+((self.narxi*x)/100)
        
obj1=Mahsulot("coca cola","6 ta",130000,"Uzbekiston")
  

