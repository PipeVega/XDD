class Mascota:
    def __init__(self, id_mascota, nombre, nombre_dueno, tipo):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.nombre_dueno = nombre_dueno
        self.tipo = tipo

    def __str__(self):
        return f"ID Mascota: {self.id_mascota}\nNombre: {self.nombre}\nNombre del Dueño: {self.nombre_dueno}\nTipo: {self.tipo}"


registro_mascotas = []

def validar_id_mascota(id_mascota):
    return id_mascota.isdigit() and len(id_mascota) == 5

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_tipo(tipo):
    return tipo.lower() == "perro" or tipo.lower() == "gato"

def mostrar_menu():
    print("------ Menú ------")
    print("1. Grabar/Registrar Mascota")
    print("2. Listar Todos los registros")
    print("3. Buscar Mascota por ID")
    print("4. Salir del sistema")

def grabar_mascota():
    id_mascota = input("Ingrese el ID de la mascota: ")
    while not validar_id_mascota(id_mascota):
        print("ID de mascota inválido. Debe ser numérico y tener una longitud de 5 caracteres.")
        id_mascota = input("Ingrese el ID de la mascota: ")

    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    while not validar_nombre(nombre_mascota):
        print("Nombre de mascota inválido. No puede estar vacío.")
        nombre_mascota = input("Ingrese el nombre de la mascota: ")

    nombre_dueno = input("Ingrese el nombre del dueño: ")
    while not validar_nombre(nombre_dueno):
        print("Nombre de dueño inválido. No puede estar vacío.")
        nombre_dueno = input("Ingrese el nombre del dueño: ")

    tipo_mascota = input("Ingrese el tipo de mascota (Perro/Gato): ")
    while not validar_tipo(tipo_mascota):
        print("Tipo de mascota inválido. Debe ser 'Perro' o 'Gato'.")
        tipo_mascota = input("Ingrese el tipo de mascota (Perro/Gato): ")

    mascota = Mascota(id_mascota, nombre_mascota, nombre_dueno, tipo_mascota)
    registro_mascotas.append(mascota)
    print("Mascota registrada con éxito.")

def listar_registros():
    if len(registro_mascotas) == 0:
        print("No hay registros de mascotas.")
    else:
        for mascota in registro_mascotas:
            print(mascota)
            print("--------------------")

def buscar_mascota_por_id():
    id_mascota_buscar = input("Ingrese el ID de la mascota a buscar: ")
    for mascota in registro_mascotas:
        if mascota.id_mascota == id_mascota_buscar:
            print(mascota)
            return
    print("No se encontró ninguna mascota con el ID proporcionado.")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        grabar_mascota()
    elif opcion == "2":
        listar_registros()
    elif opcion == "3":
        buscar_mascota_por_id()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

