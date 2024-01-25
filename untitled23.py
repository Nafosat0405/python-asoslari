class Futbolchi:
    def __init__(self,ismi,yoshi,kim_bolib_oynaydi,gollar_soni):
        self.ismi=ismi
        self.yoshi=yoshi
        self.kim_bolib_oynaydi=kim_bolib_oynaydi
        self.gollar_soni=gollar_soni
        
    def get_info(self):
        return f"Futbolchi: {self.ismi}  {self.kim_bolib_oynaydi}  {self.gollar_soni} "
    
    def set_gollar_soni(self):
        return self.gollar_soni
    
    def set_kim_bolib_oynaydi(self):
        return self.kim_bolib_oynaydi
    
oyinchi1=Futbolchi("Nodir",16,"himoyachi","gol urmagan")
oyinchi2=Futbolchi("Aziz",18,"darvozabon","gol urmagan")
oyinchi3=Futbolchi("Zafar",23,"hujumchi","34 ta gol urgan")
oyinchi4=Futbolchi("Doston",16,"hujmchi","23 ta gol urgan")

class Jamoa():
    def __init__(self,nomi,galabalar_soni,maglubiyatlar_soni):
        self.nomi=nomi
        self.galabalar_soni=galabalar_soni
        self.maglubiyatlar_soni=maglubiyatlar_soni
        self.futbolchilar_soni=0
        self.futbolchilar=[]
        
    def add_futbolchilar(self,Futbolchi):
        self.futbolchilar.append(Futbolchi)
        self.futbolchilar_soni+=1
        
    def get_futbolchilar_soni(self):
        return self.futbolchilar_soni
    
    def get_futbolchilar(self):
        return [futbolchi.get_info() for futbolchi in self.futbolchilar]
    
obj=Jamoa("Bunyodkor","109 ta","3 ta")
oyinchi1=Futbolchi("Nodir",16,"himoyachi","gol urmagan")
oyinchi2=Futbolchi("Aziz",18,"darvozabon","gol urmagan")
oyinchi3=Futbolchi("Zafar",23,"hujumchi","34 ta gol urgan")
oyinchi4=Futbolchi("Doston",16,"hujmchi","23 ta gol urgan")

obj.add_futbolchilar(oyinchi1)
obj.add_futbolchilar(oyinchi2)
obj.add_futbolchilar(oyinchi3)
obj.add_futbolchilar(oyinchi4)




