class Shaxs:
    __odamlar_soni=0
    def __init__(self,ism,familiya,ish_joyi,JSHSHIR):
        Shaxs.__odamlar_soni+=1
        self.soni=Shaxs.__odamlar_soni
        
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        self.__JSHSHIR="AA1234567"

    
    def set_JSHSHIR(self,new):
        self.__JSHSHIR=new
        
    def get_count(cls):
        return cls.__odamlar_soni
    
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.ish_joyi}"
    
    
obj1=Shaxs("Nafosat","Rustambekova","bank","AA1234567")
obj2=Shaxs("Fotima","Nurmetova","maktab","AA12345667")
obj3=Shaxs("Mashxura","Fayzullayeva","universitet","AA1234567")