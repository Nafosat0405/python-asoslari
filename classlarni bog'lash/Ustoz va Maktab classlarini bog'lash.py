class Ustoz:
    def __init__(self,ismi,yoshi,maktab,sinf):
        self.ismi=ismi
        self.yoshi=yoshi
        self.maktab=maktab
        self.sinf=sinf
        
    def get_info(self):
        return f"Ustoz: {self.ismi} {self.maktab} maktabi o'qtuvchisi. Dars beradigan sinfi {self.sinf}"
    
    
ustoz1=Ustoz("Sevara","34 yoshda","umumiy o'rta talim","4 G")
ustoz2=Ustoz("Gozal","45 yoshda","o'rta mahsus","4 V")


class Maktab():
    def __init__(self,nomi,raqami,manzili):
        self.nomi=nomi
        self.raqami=raqami
        self.manzili=manzili
        self.ustozlar_soni=0
        self.ustozlar=[]
        
    def add_teacher(self,ustoz):
        self.ustozlar.append(ustoz)
        self.ustozlar_soni+=1
        
    def get_teacher(self):
        return [ustoz.get_info() for ustoz in self.ustozlar]
    
    def get_teacher_num(self):
        return self.ustozlar_soni
    
obj=Maktab("Sobir Rahimov","16-son","Urganch shahar")

ustoz1=Ustoz("Sevara","34 yoshda","umumiy o'rta talim","4 G")
ustoz2=Ustoz("Gozal","45 yoshda","o'rta mahsus","4 V")

obj.add_teacher(ustoz1)
obj.add_teacher(ustoz2)


        
