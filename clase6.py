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