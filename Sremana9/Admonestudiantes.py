from Estudiante import Estudiante
class AdmonEstudiantes:
    def __init__(self):
        self.misEstudiantes=[]
        print("Objetos tipo Admon Estudiantes creado ...!")   
        self.menu()
        
    def menu(self):
            opcion=-1
            while opcion!=0:
                print("Opciones:")
                print("0. para salir")
                print("1. Nuevo Estudiante")
                print("2. para ver todo ")
                print("3. buscar estudiante")
                print("4.Eliminar estudiante")
                print("5. modificar un alumno ")

                
                
                
                opcion = int(input("Diga su opcion:"))
                if opcion == 0:
                    print("Adios ....")
                elif opcion ==1:
                        self.nuevoEstudiante()
                elif opcion == 2:
                            self.vertodos()
                elif opcion == 3:
                    self.buscarAlumno()
                elif opcion == 4:
                    self.elimunarestudiante()
                elif opcion == 5:
                    self.modificaralumno()
        
        
        
    def nuevoEstudiante (self):
        #Pedir infromacion #
        codigoNew=int(input("Diga el codigo del estudiante"))
        if self.existecodigo(codigoNew)== True:
            print("El Codigo del estudiante ya existe")
        else:
            nombreNew=input("Diga el nombre del estudiante")
            notaNew=float(input("Diga la nota del estudiante"))
            if notaNew < 0 or notaNew>5:
                print("No se crea ya que la nota NO valida")
            else:
                    ##Crear el objeto estudiante#
                    alumno = Estudiante (codigoNew, nombreNew, notaNew)
                    #Guardar esta instancia en la lista
                    self.misEstudiantes.append(alumno)
        
    def vertodos(self):
        for alumno in self.misEstudiantes:
            print(alumno.toString())
    def buscarAlumno(self):
        bcodigo = int(input("Digite el codigo"))
        for alumno in self.misEstudiantes:
            if bcodigo == alumno.getCodigo():
                print(alumno.toString())
    def elimunarestudiante(self):
        dcodigo= int(input("Digite el codigo del estudiante"))
        for alumno in self.misEstudiantes:
            if dcodigo == alumno.getCodigo():
                self.misEstudiantes.remove(alumno)
    def modificaralumno(self):
        mcodigo = int(input("Digite el codigo del estudiante"))
        for alumno in self.misEstudiantes:
            if mcodigo == alumno.getCodigo():
                codigoNew=int(input("Diga el codigo del estudiante"))
                if self.existecodigo(codigoNew)==True:
                    print("Ya existe el codigo ")
                else:
                    nombreNew=input("Diga el nombre del estudiante")
                    notaNew=float(input("Diga la nota del estudiante"))
                    if notaNew<0 or notaNew>5:
                        print("El estudiante no pude ser modificado ")
                    else:
                        print("El estudiante fue modificado")
                        alumno.setNombre(nombreNew)
                        alumno.setNombre(nombreNew)
                        alumno.setCodigo(codigoNew)
                        alumno.setNota(notaNew)
    def existecodigo (self, codigo):
        for alumno in self.misEstudiantes:
            if codigo == alumno.getCodigo():
                return True
        return False
