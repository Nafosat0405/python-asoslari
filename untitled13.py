class Futbolchi:
     def __init__(self,ismi,yoshi,kim_bolib_oynaydi,gollar_soni):
         self.ismi=ismi
         self.yoshi=yoshi
         self.kim_bolib_oynaydi=kim_bolib_oynaydi
         self.gollar_soni=gollar_soni
         
     def get_info(self):
         return f"{self.ismi},{self.yoshi},{self.kim_bolib_oynaydi},{self.gollar_soni}"
     
     def set_gollar_soni(self,x):
         self.gollar_soni=x
         
obj1=Futbolchi("Zafar",18,"darvozabon",10)
        