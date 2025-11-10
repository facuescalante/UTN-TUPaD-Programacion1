Diseño del programa 
El sistema fue diseñado bajo el paradigma de Programación Estructurada y Modular, haciendo uso 
intensivo de las siguientes estructuras de datos y conceptos aprendidos en la asignatura Programación 
1. 
1. Listas (Estructuras de Datos) 
Las listas son la estructura de datos fundamental utilizada para almacenar la colección completa de 
países. Una lista en Python es una colección ordenada y mutable de elementos. Permite agrupar 
diferentes tipos de datos. 
La variable países es una lista principal donde cada elemento es un diccionario que representa un país. 
Este formato es ideal para aplicar iteraciones (bucles), filtros y ordenamientos sobre el conjunto de datos 
completo. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
9 
2. Diccionarios (Estructuras de Datos) 
Los diccionarios se utilizan como el contenedor individual para los datos de cada país. 
Un diccionario es una colección no ordenada y mutable de datos que almacena información en pares 
clave-valor. Permiten acceder a los datos por su nombre descriptivo (clave) en lugar de por un índice 
numérico. 
Cada país (nombre, población, superficie, continente) se almacena en un diccionario. Esto proporciona 
un acceso claro y semántico a los atributos. Por ejemplo, para obtener la población, se accede con 
pais["poblacion"]. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
10 
3. Funciones (Modularización) 
El código está completamente modularizado mediante el uso de funciones. 
Una función es un bloque de código reutilizable que realiza una tarea específica. 
Se aplica el principio de "una función = una responsabilidad". Las funciones principales son llamadas 
desde el menú (ejecutar_programa()) para realizar una única tarea, como agregar_pais(), buscar_pais(), 
o ordenar_paises(). Esto mejora la legibilidad y el mantenimiento del código. 
Se utilizan funciones pequeñas para tareas específicas, como normalizar() para eliminar acentos y las 
funciones obtener_nombre(), obtener_poblacion(), etc., para facilitar los ordenamientos. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
11 
4. Condicionales (Estructuras de Control) 
Las estructuras condicionales son esenciales para la lógica de validación y la toma de decisiones del 
menú. Permiten ejecutar bloques de código específicos basándose en si una condición es verdadera 
(True) o falsa (False). 
Se utilizan if/elif/else para validar que los datos ingresados por el usuario (población, superficie, 
continente) cumplan con los criterios de formato y rango (ej. if not poblacion.isdigit() or int(poblacion) 
<= 0: en agregar_pais). 
El flujo del programa se controla mediante condicionales (if opcion == "1":, elif opcion == "2":, etc.) en 
la función ejecutar_programa(). 
Se usan condiciones dentro de compresiones de lista para generar subconjuntos de datos (ej. [p for p in 
paises if min_pob <= p["poblacion"] <= max_pob]). 
TRABAJO PRÁCTICO INTEGRADOR                                                 
12 
TRABAJO PRÁCTICO INTEGRADOR                                                 
13 
5. Ordenamientos (Procesamiento de Datos) 
La función de ordenamiento utiliza el método sorted() de Python, aprovechando las funciones auxiliares 
para definir la clave de ordenamiento. 
El ordenamiento permite organizar los elementos de una colección (la lista de países) según un criterio 
específico (nombre, población o superficie). 
En la función ordenar_paises(), el usuario elige el campo. Se emplea el parámetro key con las funciones 
auxiliares (ej. key=obtener_poblacion) y el parámetro reverse=reverse para alternar entre orden 
Ascendente (A) y Descendente (D). 
TRABAJO PRÁCTICO INTEGRADOR                                                 
14 
6. Estadísticas Básicas (Análisis de Datos) 
El sistema calcula estadísticas clave para resumir la información del conjunto de datos. 
Son indicadores que resumen las propiedades de un conjunto de datos. 
Se usan las funciones max() y min() de Python con el argumento key para encontrar el país con mayor y 
menor población. 
El promedio de población y superficie se calcula usando la función sum() sobre los datos, dividido por el 
número total de países (len(paises)). 
Se utiliza un diccionario (continentes) para contar la cantidad de países por cada continente, 
demostrando el uso de diccionarios como contadores. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
15 
7. Archivos CSV (Persistencia de Datos) 
Se utiliza el módulo estándar csv para garantizar la persistencia de los datos. 
CSV (Comma Separated Values) es un formato de archivo de texto plano que utiliza comas para separar 
valores y líneas nuevas para separar registros. 
La función cargar_paises() utiliza csv.DictReader para leer el archivo paises.csv y convertir cada fila 
automáticamente en un diccionario. 
La función guardar_paises() utiliza csv.DictWriter para escribir la lista de diccionarios de vuelta al 
archivo, asegurando que los datos agregados o modificados se conserven. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
16 
Diagrama de flujo 
A continuación, se presenta el diagrama que define el flujo de operaciones principales del sistema. Este 
esquema visualiza cómo el programa se inicia, presenta el menú de opciones y gestiona la interacción 
con el usuario hasta su finalización. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
17 
Explicación del funcionamiento  
El programa opera mediante un bucle principal gestionado por la función ejecutar_programa(), que se 
encarga de iniciar el sistema y mantener la interacción constante con el usuario a través del menú.  
A continuación, se detalla el flujo de cada funcionalidad: 
1. Inicio y Persistencia de Datos 
El flujo comienza con dos acciones cruciales para la gestión de datos: 
• Carga Inicial (cargar_paises): Al iniciar ejecutar_programa(), se llama a 
cargar_paises("paises.csv"). Esta función lee el archivo CSV, utilizando csv.DictReader para mapear 
automáticamente las cabeceras a las claves del diccionario. Cada fila se convierte en un diccionario, 
y todos se añaden a la lista países, la estructura de datos principal del sistema. 
• Persistencia (guardar_paises): Después de cualquier operación que modifique la lista (como 
agregar o actualizar un país), se llama a guardar_paises(). Esta función utiliza csv.DictWriter para 
sobrescribir el archivo paises.csv con el estado actual de la lista, garantizando que los cambios sean 
permanentes. 
2. Gestión de Datos (Opciones 1 y 2) 
Opción 1: Agregar País (agregar_pais) 
1. Solicitud de Datos: Se pide el nombre, población, superficie y continente del nuevo país. 
2. Validación Robusta: Se implementan validaciones estrictas: 
a. Población y Superficie: Se verifica que los valores sean numéricos y positivos (if not 
poblacion.isdigit() or int(poblacion) <= 0:). 
b. Continente: Se usa la función auxiliar encontrar_continente() que, tras normalizar la 
entrada (quitar acentos y minúsculas con normalizar()), compara con una lista de 
CONTINENTES_VALIDOS, asegurando la coherencia de datos. 
3. Registro y Guardado: Si todos los datos son válidos, se crea un nuevo diccionario y se añade a la 
lista paises con .append(). Finalmente, se llama a guardar_paises() para actualizar el CSV. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
18 
Opción 2: Actualizar País (actualizar_pais) 
1. Búsqueda Preliminar: Se pide al usuario el nombre del país a modificar. La función itera sobre la 
lista de países para encontrar una coincidencia exacta. 
2. Modificación: Si se encuentra el país, se solicitan los nuevos valores de poblacion y superficie. 
Estos valores se validan de la misma manera que en la función de agregar. 
3. Actualización y Persistencia: Se actualizan los valores del diccionario del país encontrado. Si la 
actualización es exitosa, se llama a guardar_paises(). 
3. Consultas y Procesamiento (Opciones 3, 4 y 5) 
Opción 3: Buscar País (buscar_pais) 
1. Normalización de Búsqueda: Se pide el término de búsqueda. Tanto el nombre del país en el 
diccionario como el término ingresado por el usuario se normalizan usando la función normalizar(). 
Esto garantiza que la búsqueda sea insensible a mayúsculas, minúsculas y acentos, mejorando la 
experiencia del usuario. 
2. Filtro: Se recorre la lista paises y se añade a una nueva lista de resultados (paises_encontrados) 
todo aquel diccionario cuyo nombre normalizado contenga (coincidencia parcial) el término de 
búsqueda normalizado. 
Opción 4: Filtrar Países (filtrar_paises) 
Esta función ofrece un submenú para elegir el criterio de filtrado: 
• Por Continente: Se pide el continente. Se utiliza la función encontrar_continente() para validar 
la entrada. Luego, mediante una compresión de lista, se genera un subconjunto de países que 
coinciden con el continente validado. 
• Por Rango (Población/Superficie): Se piden un valor mínimo y máximo. Las entradas se validan 
para asegurar que sean números y que el mínimo sea menor o igual al máximo. La función utiliza 
compresiones de lista para incluir solo los países cuyo valor cae dentro del rango especificado. 
Opción 5: Ordenar Países (ordenar_paises) 
TRABAJO PRÁCTICO INTEGRADOR                                                 
19 
1. Criterio y Sentido: El usuario selecciona el criterio (Nombre, Población, Superficie) y el sentido 
(Ascendente/Descendente). 
2. Uso de sorted() con Clave: Se aplica la función nativa sorted() de Python sobre la lista paises. 
a. Se utiliza el parámetro key al que se le asigna una función auxiliar (ej. obtener_nombre, 
obtener_poblacion) para indicar por qué atributo del diccionario debe ordenarse. 
b. Se usa el parámetro reverse=True si el usuario eligió orden Descendente. 
Opción 6: Mostrar Estadísticas (mostrar_estadisticas) 
Esta función realiza un análisis completo de los datos en memoria: 
1. Máximos y Mínimos: Las funciones nativas max() y min() se utilizan con el argumento 
key=obtener_poblacion para encontrar directamente el país con la mayor y menor población. 
2. Promedios: El promedio de población y superficie se calcula sumando el valor de todos los países 
(sum()) y dividiendo por el total de países (len(paises)). 
3. Conteo por Categoría: Se inicializa un diccionario vacío (continentes = {}). Se itera sobre la lista 
paises y se utiliza el nombre del continente como clave, incrementando el valor del contador por 
cada país, demostrando el uso eficiente de diccionarios para el conteo de frecuencias. 
TRABAJO PRÁCTICO INTEGRADOR                                                 
20 
Conclusión 
El proyecto demostró la importancia de planificar la estructura de datos desde el inicio, ya que el uso de 
diccionarios facilitó enormemente la manipulación de los atributos de cada país. El trabajo en equipo 
permitió abordar las diferentes funcionalidades de forma distribuida, optimizando el tiempo de 
desarrollo e integrando los módulos de manera eficiente. También permitió fortalecer nuestras 
habilidades blandas, como la organización, planificación de tareas y mejorar nuestra comunicación para 
poder lograr el objetivo propuesto. 
Como potencial mejora o línea futura, el proyecto es escalable. La sólida base modular permitiría, sin 
modificar la lógica interna de procesamiento, migrar la interfaz de consola a una interfaz gráfica (GUI) o 
integrar servicios de visualización de datos (como gráficos o mapas), expandiendo así su utilidad. 
En síntesis, este TPI valida la adquisición de las habilidades necesarias para construir una aplicación 
funcional, robusta y bien diseñada en Python. 