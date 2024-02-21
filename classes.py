class Human :
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("yapıcı blok çalıştı")


    def age(self,age):
        return age
    
    def talk(self,message):
        print(message)

    def walk(self):
        #print("walking...") 
       #yerine 
        print(f"{self.name} walking...")




human1 = Human("Mehmet",25)
human1.talk("Hocam")
human1.walk()


