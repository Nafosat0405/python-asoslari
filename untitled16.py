class Fan:
    def __init__(self,nomi,soat_xajmi,kursi,turi):
        self.nomi=nomi
        self.soat_xajmi=soat_xajmi
        self.kursi=kursi
        self.turi=turi
        
        
    def get_info(self):
        return f"{self.nomi},{self.kursi}"
    
    def set_kursi(self,x):
        self.kursi=x
        
obj1=Fan("Ma'lunotlar bazasi","180 soat",2,"aniq fanlar")