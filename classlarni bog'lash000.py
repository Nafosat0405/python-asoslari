class Talaba:
    def __init__(self,ism,familiya,tyili):
        self.ism=ism
        self.familiya=familiya
        self.tyili=tyili
        self.bosqich=1
        
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich} - bosqich talabasi"
    
    
talaba1=Talaba("Alijon","Valiyev",2000)
talaba2=Talaba("Hasan","Alimov",2001)
talaba3=Talaba("Akrom","Boriyev",2001)
        
class Fan():
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    
    
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
        
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]
        
        
Matematika=Fan("Oliy Matematika")
talaba1=Talaba("Alijon","Valiyev",2000)
talaba2=Talaba("Hasan","Alimov",2001)
talaba3=Talaba("Akrom","Boriyev",2001)

Matematika.add_student(talaba1)
Matematika.add_student(talaba2)
Matematika.add_student(talaba3)

    