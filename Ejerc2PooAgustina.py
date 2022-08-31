# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una  persona)
#  y cantidad (puede tener decimales).
#  El titular será obligatorio y la cantidad es  opcional.
#  Construye los siguientes métodos para la clase: 
#  Un constructor, donde los datos pueden estar vacíos. 
# ∙ Los setters y getters para cada uno de los atributos.
# . El atributo no se puede  modificar directamente, sólo ingresando o retirando dinero. 
# ∙ mostrar(): Muestra los datos de la cuenta. 
# ∙ ingresar(cantidad): se ingresa una cantidad a la cuenta, 
# si la cantidad  introducida es negativa, no se hará nada. 
# ∙ retirar(cantidad): se retira una cantidad a la cuenta. 
# La cuenta puede estar en  números rojos.



class Cuenta():
    def __init__(self,nombre,cant):
        self.Titular= nombre
        self.__Cantidad=cant or ""

    def getTitular(self):
        return self.Titular

    def getCantidad(self):
        return self.__Cantidad

    def setTitular(self,nombre):
        self.Titular = nombre
        
    def setCantidad(self,cant):
        self.Cantidad= cant    

    def mostrar(self):
        print(f"Nombre del titular: {self.getTitular()}\n Cantidad: {self.getCantidad()} ")
 

    def IngresarDinero(self):
        nuevaCantidad= float(input("Ingrese el monto deseado: "))
        if nuevaCantidad > 0:
            self.__Cantidad+= nuevaCantidad
            return print("Su saldo es: ", self.__Cantidad)

    def RetirarDinero(self):
        extraccion= float(input("Ingrese el monto a retirar: "))
        if extraccion > 0:
            self.__Cantidad-= extraccion
            return print("Su saldo es: ", self.__Cantidad)
        else:
            print("Debe ingresar un monto mayor a 0")



cuenta1 = Cuenta("Claudia",180000)
cuenta1.mostrar()
cuenta1.IngresarDinero()
cuenta1.RetirarDinero()
cuenta1.mostrar()


        
        
        
