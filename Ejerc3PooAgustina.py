# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
#clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
#titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
#ciento.Construye los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.,
#por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
#si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
#bonificación de la cuenta.
#Piensa los métodos heredados de la clase madre que hay que reescribir.
from Ejerc2PooAgustina import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self,titular, cant, bonif, edad):
        super().__init__(titular, cant)  
        self.Edad=edad
        self.Bonificacion=bonif

    def getBonificacion(self):
        return self.Bonificacion

    def getEdad(self):
        return self.Edad

    def setBonificacion(self,bonif):
        self.Bonificacion= bonif

    def setEdad(self,edad):
        self.Edad= edad

    def esTitularValido(self):
        if self.Edad >=18 and self.Edad <25:
            print("Usted es titular Válido")
            return True
        else:
            print("Usted no es titular válido")
            return False

    # def CalculoBonificacion(self):
    #         self.Bonificacion= self.Cantidad * (self.Bonificacion/100)

    def mostrar(self):
        print("="*40)
        print("CUENTA JOVEN")
        
        print(f"Su bonificacion es: {self.Bonificacion}%")

    def RetirarDinero(self):
        if self.esTitularValido():
            extraccion= float(input("Ingrese el monto a retirar: "))
            if extraccion > 0:
                self.Cantidad-= extraccion
                print("Su saldo es: ", self.Cantidad)
            else:
                print("Debe ingresar un monto mayor a 0")
        else:
            print("Usted no puede retirar dinero")
         
cuenta1=CuentaJoven("Claudia",180000,10,24)
cuenta1.mostrar()
cuenta1.esTitularValido()

cuenta1.RetirarDinero()
cuenta1.mostrar()           

