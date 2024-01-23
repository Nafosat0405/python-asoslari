class Ishchi:
    def __init__(self,ismi,guruh_raqami,staji):
        self.ismi=ismi
        self.guruh_raqami=guruh_raqami
        self.staji=staji
        
    def get_info(self):
        return f"Ismi: {self.ismi} Guruh raqami: {self.guruh_raqami}  Staji:{self.staji}"
    
    def set_staji(self,x):
        self.staji=x
        
        
ishchi1=Ishchi("Nafosat","941-22","3 yil")
ishchi2=Ishchi("Muxlisa","942-22","4 yil")
ishchi3=Ishchi("Fotima","961-23","5 yil")


class Korxona():
    def __init__(self,nomi,firma_raqami,manzili):
        self.nomi=nomi
        self.firma_raqami=firma_raqami
        self.manzili=manzili
        self.ishchilar_soni=0
        self.ishchilar=[]
        
        
    def add_ishchilar(self,ishchi):
        self.ishchilar.append(ishchi)
        self.ishchilar_soni+=1
        
        
    def get_ishchilar(self):
        return [osh.get_info() for osh in self.ishchilar]
    
    def get_ishchi_num(self):
        return self.ishchilar_soni
    
IT_kompaniya=Korxona("Mustafo IT software","90 678 45 34","Urganch shahri Al-Xorazmiy ko'chasi 78-uy")
ishchi1=Ishchi("Nafosat","941-22","3 yil")
ishchi2=Ishchi("Muxlisa","942-22","4 yil")
ishchi3=Ishchi("Fotima","961-23","5 yil")

IT_kompaniya.add_ishchilar(ishchi1)
IT_kompaniya.add_ishchilar(ishchi2)
IT_kompaniya.add_ishchilar(ishchi3)


