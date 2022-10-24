class Persona:
    def __init__(self):
        pass
    def __init__(self, nombre, edad, DNI):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad=edad
    @property
    def DNI(self):
        return self.__DNI
    @DNI.setter
    def DNI(self, DNI):
        self.__DNI=DNI
    def mostrar(self):
        return "Nombre: " + str(self.nombre)+ " Edad: "+ str(self.edad) + " DNI: "+ str(self.DNI)
    def esMayorEdad(self):
        return print(self.edad>=18)

class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.__titular = titular
        self.__cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular=titular
     
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad=cantidad

    def mostrar(self):
        return "Titular: " + str(self.__titular)+ " Cantidad: "+ str(self.__cantidad)

    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad-=cantidad

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion
    
    def esTitularValido(self):
        return (self.titular.edad >18) and (self.titular.edad<25)
    
    def retirar(self, cantidad):
        if self.esTitularValido():
            self.__cantidad-=cantidad
        else:
            print("Usuario no válido no se puede retirar")
    
    def mostrar(self):
        return "Cuenta Joven \n" + super().mostrar() + " Bonificación: " + str(self.__bonificacion)

