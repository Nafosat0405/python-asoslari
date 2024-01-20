class Tasvir:
    def __init__(self,nomi,tasvirchi,yili,galereya):
        self.nomi=nomi
        self.tasvirchi=tasvirchi
        self.yili=yili
        self.galereya=galereya
        
    def get_info(self):
        return f"Tasvir nomi:{self.nomi}. Kim tomondan chizilgan:{self.tasvirchi}.Nechanchi yilda yaratilgan:{self.yili}"
    
    def set_yili(self,x):
        self.yili=x
        
obj1=Tasvir("Navruz bayramida","Rustambekova Guli", "2023", "Mukammal tasvir")
