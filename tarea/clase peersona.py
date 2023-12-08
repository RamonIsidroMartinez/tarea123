class Persona: 
    def _init_ (self):
        self.nombre=input("Escribe el nombre de la persona: ")
        self.apellidos=input("Ecribe el apellido de la persona: ")
        self.edad=int(input("Escribe la edad de la persona: "))
        self.sexo=input("Escribe la sexo de la persona: ")
        self.direccion= input("Escribe la direccion de la persona: ")

    def imprimir (self):

        print("El nombre de la persona es: ", self.nombre)
        print("El apellido de la persona es: ", self.apellidos)
        print("La edad de la persona es: ", self.edad)
        print("El sexo de la persona es: ", self.sexo)
        print("La direccion de la persona es: ", self.direccion)

persona1=Persona()
persona1.imprimir()