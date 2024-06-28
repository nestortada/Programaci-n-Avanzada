class Gato:
    def __init__(self,name):
        self.nombre= name
        self.edad=1
        print("Nacio un gato",self.nombre)
    def llamarlo (self):
        print("ven gatito ,ven ", self.nombre)
    def crecer(self):
        self.edad=self.edad+1
        print(self.nombre,"crecio y tiene ", self.edad, " años")
    def etapa(self):
        if self.edad>2:
            print("es viejo")
        else:
            print("gato joven")