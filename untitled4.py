class Fan:
    def __init__(self,nomi,qriditi):
        self.nomi=nomi
        self.qriditi=qriditi
        
    def get_name(self):
        return self.ism
    def __repr__(self):
        return f"{self.nomi} {self.qriditi}"
        
    
obj1=Fan("Malumotlar bazasi","6 kridit")
obj2=Fan("Malumotlar tuzilmasi","6 kridit")
obj3=Fan("Diskret Matematika","6 kridit")

class Talaba:
    def __init__(self,ismi,familiyasi,kursi):
        self.ism=ismi
        self.familiyasi=familiyasi
        self.kursi=kursi
        self.fan=[]
    
    def get_name(self):
        return self.ism    
    
    
    
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.kursi}"
    def add_fan(self,fanlar):
        self.fan.append(fanlar)
        
    def get_fan(self):
        return self.fan
    
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
    
talaba1=Talaba("Nafosat","Rustambekova","941-22")
        
    
    
    
        

