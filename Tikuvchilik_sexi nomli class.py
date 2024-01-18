class Tikuvchilik_sexi:
    def __init__(self,ismi,boshliq,ishchi_soni):
        self.ismi=ismi
        self.boshliq=boshliq
        self.ishchi_soni=ishchi_soni
        
    def get_info(self):
        return f"{self.ismi},{self.boshliq}.Ishchilar soni:{self.ishchi_soni} ta"
    
    def set_ishchi_soni(self,x):
        self.ishchi_soni=x
        
obj1=Tikuvchilik_sexi("GUli_fashioner","Rustambekova Guli",50)
