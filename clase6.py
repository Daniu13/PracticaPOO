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
    
    #Polimorfismo con verNombre() de Mascota
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis


def main():
    hospitalSys = Sistema()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if hospitalSys.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            if hospitalSys.verificar(historia)[0] == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamente()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mascotinha = Mascota()
                mascotinha.asignarNombre(nombre)
                mascotinha.asignarNumHistoria(historia)
                mascotinha.asignarPeso(peso)
                mascotinha.asignarTipo(tipo)
                mascotinha.asignarFechaIngreso(fecha)
                mascotinha.asignarMedicamentos(lista_med)
                hospitalSys.ingresarMascota(mascotinha)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = hospitalSys.verFechaIngreso(q)
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=hospitalSys.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = hospitalSys.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = hospitalSys.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__ == "__main__":
    main()