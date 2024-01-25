class Tikuvchi:
    def __init__(self,ism,familiya,lavozim,staj):
        self.ism=ism
        self.familiya=familiya
        self.lavozim=lavozim
        self.staj=staj
        
    def get_info(self):
        return f"{self.ism}  {self.familiya}  {self.lavozim} {self.staj}"
   
    def set_staj(self,x):
        self.staji=x
        
tikuvchi1=Tikuvchi("Nafosat","Rustambekova","Dazmolchi","1 oy")
tikuvchi2=Tikuvchi("Muxlisa","Rajabboyeva","Yordamchi","2 oy")
tikuvchi3=Tikuvchi("Fotima","Nurmetova"," asosiy tikuvchi","3 yil")
        
class Tikuvchilik_sexi:
    def __init__(self,nomi,boshliq,ishchi_soni):
        self.nomi=nomi
        self.boshliq=boshliq
        self.ishchi_soni=ishchi_soni
        self.tikuvchilar_soni=0
        self.tikuvchilar=[]
        
        
    def add_tikuvchilar(self,tikuvchi):
        self.tikuvchilar.append(tikuvchi)
        self.tikuvchilar_soni+=1
        
    
    def get_tikuvchilar(self):
        return [tikuvchi.get_info() for tikuvchi in self.tikuvchilar]
    
    
    def get_tikuvchilar_soni(self):
        return self.tikuvchilar_soni
    
    def set_ishchi_soni(self,soni):
        self.ishchi_soni=soni
    
obj1=Tikuvchilik_sexi("Chevar","Fayzullayeva Mashhura",23)
tikuvchi1=Tikuvchi("Nafosat","Rustambekova","Dazmolchi","1 oy")
tikuvchi2=Tikuvchi("Muxlisa","Rajabboyeva","Yordamchi","2 oy")
tikuvchi3=Tikuvchi("Fotima","Nurmetova"," asosiy tikuvchi","3 yil")


obj1.add_tikuvchilar(tikuvchi1)
obj1.add_tikuvchilar(tikuvchi2)
obj1.add_tikuvchilar(tikuvchi3)
    
