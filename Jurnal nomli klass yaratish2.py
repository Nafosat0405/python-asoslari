class Jurnal:
    def __init(self,nomi,davriylik,korinishi,nashriyot):
        self.nomi=nomi
        self.davriylik=davriylik
        self.korinishi=korinishi
        self.nashriyot=nashriyot
        
    def get_info(self):
        return f"{self.nomi},{self.davriylik},{self.korinishi},{self.nashriyot}"
    def set_nomi(self,x):
        self.nomi=x
        
obj1=Jurnal("Guncha",1,"yumshoq muqova","Akademnashir")
obj2=Jurnal("Bolajon",4,"Qattiq muqova","Akademnashir")
obj3=Jurnal("Darakchi",2,"yumshoq muqova","Akademnashir")