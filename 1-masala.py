class Talaba:
    __number=0
    def __init__(self,ism,familiya,guruh,shartnoma):
        Talaba.__number+=1
        self.__id=Talaba.__number
        self.bosqich=1
        self.ism=ism
        self.familiya=familiya
        self.guruh=guruh
        self.shartnoma=shartnoma
        
    def get_id(self):
        return self.__id
    
    def get_count(cls):
        return cls.__number
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.guruh}"
    
    
obj1=Talaba("Nafosat","Rustambekova","941-22","kontrakt")
obj2=Talaba("Fotima","Nurmetova","941-22","kontrakt")
obj3=Talaba("Mashxura","Fayzullayeva","942-22","kontrakt")