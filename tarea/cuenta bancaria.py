class Cuenta_Bancaria: 
    def _init_(self): 
        self.cantidad= 200000
        self.numero_cuenta=input("Escribe el numero de cuenta: ")
        self.titular_saldo=input("Digite su nombre: ")
        
       
    def DR(self, opcion, digitar):

        self.total=0 
        self.opcion= input("Elige D si desea depositar o R si desea retirar: ")
       
        while self.opcion!='D' and self.opcion!='R' :
            self.opcion= input("Elige las opciones dadas: ")
        if self.opcion=='D' or self.opcion=='d':
           self.digitar= int(input("Digite la cantidad a depositar: "))
           self.total=self.cantidad + self.digitar
           print("Su saldo actual es: ",self.total)

        elif self.opcion=='R' : 
          self.digitar= int(input("Digite la cantidad a retirar: "))

        while self.digitar> self.cantidad:
              
          self.digitar= int(input("La cantidad que desea retirar es mayor a tu saldo, digite una cantidad igual o menor : "))

          self.total=self.cantidad - self.digitar

          print("Su saldo actual es: ",self.total)
          
    def interes (self):
       self.inte= (0.10/360)*self.cantidad
       print("La tasa de interes es igual a: ", self.inte)
        
       
       


CB= Cuenta_Bancaria()
CB.DR(opcion="",digitar=0)
CB.interes()