class Ishchi:
    def __init__(self,ismi,firma_raqami,staji):
        self.ismi=ismi
        self.firma_raqami=firma_raqami
        self.staji=staji
        
    def get_info(self):
        return f"{self.ismi},Firma raqami: {self.firma_raqami},{self.staji}"
    
    
    def update_staji(self):
        self.staji+=1
        
obj1=Ishchi("Nafosat","93-678-45-45",5 )
obj2=Ishchi("Muxlisa","97-678-46-46",6 )
obj3=Ishchi("Fotima","96-223-56-45",8 )
