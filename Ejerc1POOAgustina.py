# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas
# de datos.
#  mostrar(): Muestra los datos de la persona.
#  esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.



class Persona():
    def __init__(self,nom,ed,dni):
        if (nom,ed,dni):
            if type(nom) != str: 
                return print("Dato incorrecto")
            if type(ed) != int: 
                return print("Dato incorrecto")
            if type(dni) != str: 
                return print("Dato incorrecto")
        
        self.Nombre=nom or ""
        self.Edad=ed or 0
        self.DNI=dni or ""

    def getNombre(self):
        return self.Nombre

    def getEdad(self):
        return self.Edad

    def getDNI(self):
        return self.DNI

    def setNombre(self,nuevoNombre):
        if type (nuevoNombre) == int:
            return print("Ingresó un dato incorrecto")        
        else:
            self.Nombre=nuevoNombre
            return print("Nombre cargado con éxito")      
        

    def setEdad(self,nuevaEdad):
        if type (self.Edad) == str and type(self.Edad)==float:
            return print("Ingresó un dato incorrecto")
        else:
            self.Edad=nuevaEdad
            return print("Edad cargada con éxito")  

    def setDNI(self,nuevoDni):
        self.DNI= nuevoDni    

    def mostrar(self):
        print(f"Nombre: {self.Nombre} \n Edad: {self.Edad} años \n DNI: {self.DNI} ")

    def EsMayordeEdad(self):
        if type(self.Edad)== int:

            if self.Edad>=18:
                print("Es mayor de edad")
                return True
            else:
                print("Es menor de edad")
                return False
        else:
            print("Dato incorrecto")

    def validarDatoNum(self):
        if type (self.Edad) == str:
            return print("Ingresó un dato incorrecto")
        else:
            return print("dato correcto")          

    def validarDatoStr(self):
        if type (self.Nombre) == int:
            return print("Ingresó un dato incorrecto")        
        else:
            return print("dato correcto")          




Persona1=Persona("Claudia",43,"27539499")
Persona1.validarDatoNum()
Persona1.validarDatoStr()
Persona1.EsMayordeEdad()
Persona1.mostrar()                                

