class Sistema:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}
        self.__num_mascotas = len(self.__lista_caninos) + len(self.__lista_felinos)

    #Setters y Getters de la clase sistema + sus otras funciones
    def ingresarMascota(self, mascota):
        if mascota.verTipo().lower() == "felino":
            self.__lista_felinos[mascota.verNumHistoria()] = mascota
        if mascota.verTipo().lower() == "canino":
            self.__lista_caninos[mascota.verNumHistoria()] = mascota
    def verFechaIngreso(self, historia):
        if self.verificar(historia)[1]:
            return self.__lista_caninos[historia].verFechaIngreso()
        elif self.verificar(historia)[1] == False:
            return self.__lista_felinos[historia].verFechaIngreso()
        return None
    def verNumeroMascotas(self):
        return len(self.__lista_felinos) + len(self.__lista_caninos)
    def verMedicamento(self, historia):
        if self.verificar(historia)[1]:
            return self.__lista_caninos[historia].verMedicamentos()
        elif self.verificar(historia)[1] == False:
            return self.__lista_felinos[historia].verMedicamentos()
        return None
    def eliminarMascota(self, historia):
        if self.verificar(historia)[1]:
            self.__lista_caninos.pop(historia)
            return True
        elif self.verificar(historia)[1] == False:
            self.__lista_felinos.pop(historia)
            return True
        return False
    def verificar(self, historia):
        if historia in self.__lista_caninos:
            return True, True
        if historia in self.__lista_felinos:
            return True, False
        return False
    def salir():
        pass

class Mascota:
    def __init__(self):
        self.__nombre = ""
        self.__num_historia = 0
        self.__tipo = ""
        self.__peso = 0
        self.__fecha_ingreso = ""
        self.__lista_medicamente = []

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
    def asignarMedicamentos(self, m):
        self.__lista_medicamente = m

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
    def verMedicamentos(self):
        return self.__lista_medicamente
    
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




if __name__ == "__main__":
    pass