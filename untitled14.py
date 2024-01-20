class Disk:
    def __init__(self,nomi,xajmi,narxi,mamlakat):
        self.nomi=nomi
        self.xajmi=xajmi
        self.narxi=narxi
        self.mamlakat=mamlakat
        
    def get_info(self):
        return f"{self.nomi},{self.xajmi},{self.narxi}"
    def set_narxi(self,x):
        self.narxi=(self.narxi*x)/100
        
obj1=Disk("Nafosat","Turkiya","19","Dam olish")
