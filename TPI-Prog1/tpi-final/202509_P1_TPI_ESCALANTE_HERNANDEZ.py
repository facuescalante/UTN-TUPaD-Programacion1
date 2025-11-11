# Universidad Tecnológica Nacional
# Tecnicatura en Programación a Distancia
# Cohorte: Agosto 2025
# Programación 1
# Comisión: 4 y 6
# Grupo: 13
# Escalante Juan Facundo
# Hernández, María Aldana

# Fecha: 11/11/2025

# * TPI - Trabajo práctico integrador grupal.
# Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas.

# Importación de bibliotecas (manejar archivos .csv y normalizar strings)
import csv
import unicodedata

# Lista de continentes válidos
CONTINENTES_VALIDOS = ["África", "América", "Asia", "Europa", "Oceanía", "Antártida"]


# Función para normalizar cadenas de texto a minúsculas y sin acentuaciones
# Ejemplo: América -> america
def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


# Función para encontrar el continente ingresado por el usuario en la lista de CONTINENTES_VALIDOS
# Se normalizan ambos valores para que coincida la búsqueda sin importar las mayúsculas, minúsculas, espacios o acentos
def encontrar_continente(entrada):
    entrada_norm = normalizar(entrada)
    for continente in CONTINENTES_VALIDOS:
        if normalizar(continente) == entrada_norm:
            return continente
    return None


# Funciones auxiliares para ordenamiento y estadísticas
def obtener_nombre(pais):
    return pais["nombre"]


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


# Función que carga la lista de paises creando un diccionario con los datos que encuentra en el .csv
# Cada fila del .csv sera un elemento del diccionario con sus respectivos key=values
def cargar_paises(nombre_archivo):
    paises = []  # Lista vacía donde se cargan los paises que están en el .csv
    archivo = open(nombre_archivo, newline="", encoding="utf-8")
    lector = csv.DictReader(archivo)  # Leemos el archivo .csv
    # Recorremos el archivo y validamos la existencia y los tipos de datos
    # Sí los datos son correctos creamos un elemento para el pais con las keys nombre, población, superficie y continente y asignamos los valores del .csv
    # Cada fila se convertirá en un elemento pais dentro de paises[]
    for fila in lector:
        if ("nombre" in fila and "poblacion" in fila and "superficie" in fila
            and "continente" in fila and fila["poblacion"].isdigit()
            and fila["superficie"].isdigit()
            ):
            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"],
            }
            paises.append(pais)  # Agregamos el elemento pais a paises[]
    archivo.close()
    return paises  # La función cargar_paises devuelve paises[]


# Función que recibe como parámetros el nombre del archivo y la lista, en este caso se usara para paises[]
def guardar_paises(nombre_archivo, paises):
    archivo = open(nombre_archivo, mode="w", newline="", encoding="utf-8" )  # Abrimos el archivo en modo sobrescribir
    campos = ["nombre","poblacion","superficie","continente"]  # Definimos los headings en una lista
    escritor = csv.DictWriter(archivo, fieldnames=campos)  # creamos un escritor para paises.csv con los headings
    escritor.writeheader()  # Escribimos el encabezado
    for pais in paises:  # Por cada elemento pais en paises[]
        escritor.writerow(pais)  # Escribimos una fila
    archivo.close()  # Cerramos archivo


# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")


# Función para agregar país
def agregar_pais(paises):
    nombre = input("Nombre del país: ").strip()  # Solicita ingresar nombre sin espacios
    poblacion = input("Población: ").strip()  # Solicita ingresar población sin espacios
    superficie = input("Superficie (km2): ").strip()  # Solicita ingresar superficie sin espacios
    continente_input = input("Continente: ").strip()  # Solicita ingresar continente sin espacios

    continente = encontrar_continente(continente_input)  # Convierte el continente ingresado en uno valido de CONTINENTES_VALIDOS[]

    if not nombre.replace(" ", "").isalpha():  # Sí no es una cadena de caracteres solo alfabéticos
        print("❌ El nombre del país debe contener solo letras.")  # Muestra mensaje de error
        return  # Vuelve al menú
    if (not poblacion.isdigit() or int(poblacion) <= 0):  # Sí no es un valor de solo dígitos numéricos positivo
        print("❌ La población debe ser un número entero positivo.")  # Muestra mensaje de error
        return  # Vuelve al menú
    if not superficie.isdigit() or int(superficie) <= 0:
        print("❌ La superficie debe ser un número entero positivo.")  # Muestra mensaje de error
        return  # Vuelve al menú
    if continente is None:  # Sí es un valor vacío
        print("❌ Continente inválido.")  # Muestra mensaje de error
        print(f"🌍 Continentes válidos: {', '.join(CONTINENTES_VALIDOS)}")  # Muestra los continentes válidos
        return  # Vuelve al menú

    # Crea el nuevo elemento pais con sus keys=values
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente,
    }
    paises.append(nuevo_pais)  # Lo agrega a paises[]
    guardar_paises("paises.csv", paises)  # Actualiza paises.csv con el nuevo pais
    print("✅ País agregado correctamente.")  # Informa al usuario que el país se guardo correctamente


# Función para actualizar país
def actualizar_pais(paises):  # Recibe una lista, en este caso de paises[]
    nombre_input = input("Ingrese el nombre del país a actualizar: ").strip()  # Solicita el nombre sin espacios
    nombre_normalizado = normalizar(nombre_input)  # Lo normaliza

    # Por cada elemento pais en paises[]
    for pais in paises:
        if (normalizar(pais["nombre"]) == nombre_normalizado):  # Sí encuentra el pais ingresado
            nueva_pob = input("Nueva población: ").strip()  # Solicita actualizar población
            nueva_sup = input("Nueva superficie: ").strip()  # Solicita actualizar superficie
            if (not nueva_pob.isdigit() or int(nueva_pob) <= 0):  # Valida el valor para población
                print("❌ La población debe ser un número entero positivo.")
                return
            if (not nueva_sup.isdigit() or int(nueva_sup) <= 0):  # Valida el valor para superficie
                print("❌ La superficie debe ser un número entero positivo.")
                return
            pais["poblacion"] = int(nueva_pob)  # Actualiza los datos de población
            pais["superficie"] = int(nueva_sup)  # Actualiza los datos de superficie
            guardar_paises("paises.csv", paises)  # Actualiza el .csv
            print("✅ Datos actualizados.")  # Mensaje de éxito
            return  # Vuelve al menú

    print("❌ País no encontrado.")  # Sí no hay coincidencia muestra mensaje de error


# Función para buscar país
def buscar_pais(paises):
    termino = input("Ingrese el nombre o parte del nombre del país: ").strip()
    if not termino:  # Valida inputs vacíos
        print("❌ Debe ingresar un término de búsqueda.")
        return

    termino_norm = normalizar(termino)  # Normaliza el input
    resultados = [p for p in paises if termino_norm in normalizar(p["nombre"])]  # Normaliza el resultado de búsqueda si coincide

    if resultados:  # Muestra los resultados
        print("\n🔎 Resultados encontrados:")
        for p in resultados:
            print(f"{p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")
    else:  # Sino hay coincidencias/resultados muestra mensaje de error
        print("❌ No se encontraron países con ese nombre.")


# Función para filtrar países por continente, rango de poblacion o superficie
def filtrar_paises(paises):
    print("\n--- FILTROS DISPONIBLES ---")  # Menú interno de filtros
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":  # Por continente
        continente_input = input("Ingrese el continente: ").strip()  # Solicita continente sin espacios
        continente = encontrar_continente(continente_input)  # Obtiene el continente válido
        if continente is None:  # Sí esta vacío
            print("❌ Continente inválido.")  # Muestra mensaje
            print(f"🌍 Continentes válidos: {', '.join(CONTINENTES_VALIDOS)}")
            return  # Vuelve al menú principal
        filtrados = [p for p in paises if p["continente"] == continente]  # Guarda los paises del continente ingresado

    elif opcion == "2":  # Por rango de población
        min_pob = input("Población mínima: ").strip()  # Solicita mínimo sin espacios
        max_pob = input("Población máxima: ").strip()  # Solicita máximo sin espacios
        if not min_pob.isdigit() or not max_pob.isdigit():  # Valida la entrada
            print("❌ Debe ingresar números válidos.")  # Muestra mensaje de error
            return  # Vuelve al menú principal
        min_pob = int(min_pob)  # Convierte entrada de mínimo en numero entero
        max_pob = int(max_pob)  # Convierte entrada de máximo en numero entero
        if min_pob > max_pob or min_pob < 0:  # Sí alguna entrada es menor que 0
            print("❌ Rango inválido.")  # Mensaje de error
            return  # Vuelve al menú principal
        filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]  # Si pasaron las validaciones guarda las coincidencias en filtrados[]

    elif opcion == "3":
        min_sup = input("Superficie mínima: ").strip()
        max_sup = input("Superficie máxima: ").strip()
        if not min_sup.isdigit() or not max_sup.isdigit():
            print("❌ Debe ingresar números válidos.")
            return
        min_sup = int(min_sup)
        max_sup = int(max_sup)
        if min_sup > max_sup or min_sup < 0:
            print("❌ Rango inválido.")
            return
        filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]

    else:
        print("❌ Opción inválida.")
        return

    if filtrados:
        print("\n🌍 Países filtrados:")
        for p in filtrados:
            print(f"{p['nombre']} - {p['continente']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km²")
    else:
        print("⚠️  No se encontraron países con ese filtro.")


# Función para ordenar países
def ordenar_paises(paises):
    print("\n--- ORDENAR POR ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    campo = input("Seleccione campo: ").strip()
    orden = (input("Ascendente (A) o Descendente (D): ").strip().upper())  # Solicita entrada para orden sin espacios y en mayúsculas

    if campo not in ["1", "2", "3"] or orden not in ["A","D",]:  # Sí las entradas son incorrectas
        print("❌ Opción inválida.")
        return  # Vuelve al menú principal

    reverse = (orden == "D")  # Sí el orden en D reverse toma el valor de true y el orden sera descendiente, si el "A" = false ascendiente
    if campo == "1":
        ordenados = sorted(paises, key=obtener_nombre, reverse=reverse)  # Ordena por nombre usando la función auxiliar obtener_nombre
    elif campo == "2":
        ordenados = sorted(paises, key=obtener_poblacion, reverse=reverse)  # Ordena por población usando la función auxiliar obtener_poblacion
    elif campo == "3":
        ordenados = sorted(paises, key=obtener_superficie, reverse=reverse)  # Ordena por superficie usando la función auxiliar obtener_superficie

    print("\n📋 Países ordenados:")  # Muestra el resultado con el orden solicitado
    for p in ordenados:
        print(f"{p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} km²")  # Imprime cada país con su información formateada


# Función para mostrar estadísticas
def mostrar_estadisticas(paises):
    if not paises:  # Sí no hay paises
        print("⚠️  No hay países cargados.")  # Informamos
        return  # Vuelve al menú

    mayor = max(paises, key=obtener_poblacion)  # Obtiene el pais con mayor población
    menor = min(paises, key=obtener_poblacion)  # Obtiene el pais con menor población
    promedio_pob = sum(obtener_poblacion(p) for p in paises) / len(paises)  # Promedio de poblacion
    promedio_sup = sum(obtener_superficie(p) for p in paises) / len(paises)  # Promedio de superficie

    continentes = {}  # Diccionario de continentes
    for p in paises:  # Recorremos paises[]
        cont = p["continente"]  # Extrae el nombre del continente del .csv
        continentes[cont] = (continentes.get(cont, 0) + 1)  # Crea el continente como elemento e inicializa en 1 pero si ya existe incrementa en 1

    print("\n📈 Estadísticas:")  # Muestra los resultados
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {int(promedio_pob)}")
    print(f"Promedio de superficie: {int(promedio_sup)} km²")
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  {cont}: {cant}")


# Función principal del programa
def ejecutar_programa():
    paises = cargar_paises("paises.csv")  # Llama a la función cargar_paises que almacena los paises en paises[] desde paises.csv
    while True:
        mostrar_menu()  # # Llama a la función que muestra el menú de opciones
        opcion = input("Seleccione una opción: ").strip()  # Solicita una opción
        if opcion == "1":
            agregar_pais(paises)  # Llama a la función para agregar pais
        elif opcion == "2":
            actualizar_pais(paises)  # Llama a la función para actualizar población y superficie de un pais existente
        elif opcion == "3":
            buscar_pais(paises)  # Llama a la función que busca un pais
        elif opcion == "4":
            filtrar_paises(paises)  # Llama a la función que filtra países por continente, rango de poblacion o superficie
        elif opcion == "5":
            ordenar_paises(paises)  # Llama a la función que ordena por nombre, poblacion o superficie
        elif opcion == "6":
            mostrar_estadisticas(paises)  # Llama a la función que muestra las estadisticas de los paises (mayor población, etc).
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break  # Termina el programa
        else:
            print("⚠️ Opción no válida.")


# Ejecutar
if __name__ == "__main__":
    ejecutar_programa()
