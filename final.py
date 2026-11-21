from datetime import datetime
# LISTAS
codigos = []
dnis = []
nombres = []
tipos = []
asuntos = []
folios = []
fechas = []
estados = []

# DOCUMENTOS PERMITIDOS
tiposPermitidos = ["MATRICULA", "MATRÍCULA", "CONSTANCIA",
                   "CERTIFICADO", "SOLICITUD", "RECLAMO"]


# REGISTRAR EXPEDIENTE

def registrarExpediente():
    dni = input("Ingrese DNI: ").strip()
    nombre = input("Ingrese nombre del estudiante: ").strip()
    tipo = input("Tipo de documento: ").strip().upper()
    asunto = input("Ingrese asunto: ").strip()
    cantidad = input("Cantidad de folios: ").strip()

    if not dni.isdigit() or len(dni) != 8:
        print("DNI inválido.")
        return

    if nombre == "" or asunto == "":
        print("Debe completar todos los datos.")
        return

    if tipo not in tiposPermitidos:
        print("Tipo de documento no permitido.")
        return

    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Cantidad de folios inválida.")
        return

    codigo = "EXP-2026-" + str(len(codigos) + 1).zfill(4)

    codigos.append(codigo)
    dnis.append(dni)
    nombres.append(nombre)
    tipos.append(tipo)
    asuntos.append(asunto)
    folios.append(int(cantidad))
    fechas.append(datetime.now().strftime("%d/%m/%Y"))
    estados.append("Pendiente")

    print("\nExpediente registrado correctamente.")
    print("Código:", codigo)
    print("Fecha:", fechas[-1])


# BUSCAR EXPEDIENTE
def buscarExpediente():
    codigo = input("Ingrese código: ").strip().upper()

    for i in range(len(codigos)):
        if codigos[i] == codigo:
            print("\nCódigo:", codigos[i])
            print("DNI:", dnis[i])
            print("Estudiante:", nombres[i])
            print("Documento:", tipos[i])
            print("Asunto:", asuntos[i])
            print("Folios:", folios[i])
            print("Fecha:", fechas[i])
            print("Estado:", estados[i])
            return

    print("Expediente no encontrado.")


# ORDENAR POR INSERCION
def ordenarExpedientes():
    for i in range(1, len(codigos)):
        j = i

        while j > 0 and codigos[j] < codigos[j - 1]:

            auxiliar = codigos[j]
            codigos[j] = codigos[j - 1]
            codigos[j - 1] = auxiliar

            auxiliar = dnis[j]
            dnis[j] = dnis[j - 1]
            dnis[j - 1] = auxiliar

            auxiliar = nombres[j]
            nombres[j] = nombres[j - 1]
            nombres[j - 1] = auxiliar

            auxiliar = tipos[j]
            tipos[j] = tipos[j - 1]
            tipos[j - 1] = auxiliar

            auxiliar = asuntos[j]
            asuntos[j] = asuntos[j - 1]
            asuntos[j - 1] = auxiliar

            auxiliar = folios[j]
            folios[j] = folios[j - 1]
            folios[j - 1] = auxiliar

            auxiliar = fechas[j]
            fechas[j] = fechas[j - 1]
            fechas[j - 1] = auxiliar

            auxiliar = estados[j]
            estados[j] = estados[j - 1]
            estados[j - 1] = auxiliar

            j = j - 1

    print("Expedientes ordenados correctamente.")


# LISTAR EXPEDIENTES
def listarExpedientes():
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
    else:
        for i in range(len(codigos)):
            print(codigos[i], "-", nombres[i],
                  "-", tipos[i], "-", estados[i])


# MENU PRINCIPAL
while True:
    print("\n===== MESA DE PARTES DIGITAL =====")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Ordenar expedientes")
    print("4. Listar expedientes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrarExpediente()

    elif opcion == "2":
        buscarExpediente()

    elif opcion == "3":
        ordenarExpedientes()
        listarExpedientes()

    elif opcion == "4":
        listarExpedientes()

    elif opcion == "5":
        print("Cerrando sistema...")
        break

    else:
        print("Opción inválida.")
