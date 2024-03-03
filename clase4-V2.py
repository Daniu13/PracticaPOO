class Paciente:
    def __init__(self):
        self.__nombre = "juanita"
        self.__cedula = int
        self.__genero = ""
        self.__servicio = ""

    #Getters de La clase Paciente
    #Toman como parámetro el propio self, que toma el valor del objeto instantáneo y retorna cada caso respectivo de la función    
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    #Setters de la clasee Paciente
    #Parámetros: self, n/s/g/c
    #se asigna con la variable el valor que se quiere dar con sintaxis similar a cuando se asignan atributos
    #predeterminados en la función __init__:
    #En vez de retornar cualquier valor asignan la variable al atributo
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        self.__lista_pacientes = []
      
    def eliminarPaciente(self,c):
        if self.verDatosPaciente(c):
            pass
      
    def verificarPac(self,ced):
        encontrado =  False
        for p in self.__lista_pacientes:
            if ced == p.verCedula():
                encontrado = True
                break
        return encontrado

    def ingresarPaciente(self,pac):
        if self.verificarPac(pac.verCedula()):
            return False
        self.__lista_pacientes.append(pac)
        return True

    def verDatosPaciente(self,c):
        if self.verificarPac(c) == False:
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    def verNumeroPacientes(self):
        # print("Enel sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
        return len(self.__lista_pacientes)
        
def main():
    sis = Sistema()
    while True:
        opcion = int(input("Ingrese 0 para volver al menu, 1 para ingresar nuevo paciente, 2 ver paciente: , 3 - ver cantidad de pacientes "))
        if opcion == 1:
            print("A continuacion se solicitaran los seguientes datos:")
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2 se crea un objeto Paciente
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            r = sis.ingresarPaciente(pac)
            # 3 se almacena en la lista que esta dentro de la clase sistema

            if r == True:
                print("paciente ingresado")
            else:
                print("paciente ya existe en el sistema")

        elif opcion == 2:
            # 1 solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: "))
            # le pido al sistema que me devuelva en la variable p al paciente que tenga
            #  la cedula c en la lista
            p = sis.verDatosPaciente(c)
            # si encunetro el paciente imprimo los datos
            if p == None:
                print("El paciente no se encotró")
            else:
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
        
        elif opcion == 3:
            print(f"la cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                    
        elif opcion != 0:
            continue
        else:
            break

#El método main se llama para poder ejecutar la función main, se usa para asegurarse de que el código
#sea corrido en el archivo o entorno deseado, sin embargo al ser este un código de un sólo archivo carece de mayor utilidad
if __name__ == '__main__':
    main()