class Ijarachi:
    def __init__(self,ismi,mamlakat,yoshi,sayohat_maqasadi):
        self.ismi=ismi
        self.mamlakat=mamlakat
        self.yoshi=yoshi
        self.sayohat_maqasadi=sayohat_maqasadi

        
    def get_info(self):
        return f"{self.ismi},{self.mamlakat},{self.yoshi}"
    
    def update_yoshi(self):
        self.yoshi+=1
        
obj1=Ijarachi("Nafosat","Turkiya","19","Dam olish")
obj2=Ijarachi("Guli","Turkiya","21","Dam olish")

   
