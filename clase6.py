class Sistema:
    def __init__(self):
        self.__lista_mascotas = []
        self.__num_mascotas = len(self.__lista_mascotas)

    def eliminarMascota(self):
        pass

class Mascota:
    def __init__(self):
        self.__nombre = ""
        self.__num_historia = 0
        self.__tipo = ""
        self.__peso = 0
        self.__fecha_ingreso = ""
        self.__medicamento = ""

    #Setters de Mascota
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarNumHistoria(self, nh):
        self.__num_historia = nh
    def asignarTipo(self, t):
        self.__tipo = t
    def asignarPeso(self, p):
        self.__peso = p
    def asignarFechaIngreso(self, fi):
        self.__fecha_ingreso = fi
    def asignarMedicamento(self, m):
        self.__medicamento = m

    #Getters de Mascota
    def verNombre(self):
        return self.__nombre
    def verNumHistoria(self):
        return self.__num_historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFechaIngreso(self):
        return self.__fecha_ingreso
    def verMedicamento(self):
        return self.__medicamento
    
class Medicamente:
    def __init__(self):
        self.__nombre = ""
        self.__dosis = 0

    #Setters y Getters de Nombre son polimorfismo con la clase Mascota
    #por las funciones asignarNombre() y verNombre()
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarDosis(self, d):
        self.__dosis = d
    
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis