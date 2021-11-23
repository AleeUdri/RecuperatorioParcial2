from TDA_Arbol_Binario import Arbol

#Punto 5
def MostrarDinosauriosDeXOrden(arbol, nombre):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            MostrarDinosauriosDeXOrden(arbol.izq, nombre)
        if(arbol.datos['nombre'] == nombre):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            MostrarDinosauriosDeXOrden(arbol.der, nombre)

#Punto 7
def MostrarCampoDinosauriosDeXNombre(arbol, nombre, campo):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            MostrarCampoDinosauriosDeXNombre(arbol.izq, nombre, campo)
        if(arbol.datos['nombre'] == nombre):
            print(arbol.info, arbol.datos[campo])
        if(arbol.der is not None):
            MostrarCampoDinosauriosDeXNombre(arbol.der, nombre, campo)

#Punto 8
def ContarDinosauriosDeXOrden(arbol, nombre):
    contador = 0
    if(arbol.info is not None):
        if(arbol.izq is not None):
            contador += ContarDinosauriosDeXOrden(arbol.izq, nombre)
        if(arbol.datos['nombre'] == nombre):
            contador += 1
        if(arbol.der is not None):
            contador += ContarDinosauriosDeXOrden(arbol.der, nombre)
    return contador

def ejercicio():
    #Punto 1
    dic_dinosaurios = [
        {'nombre' : 'Raptor', 'codigo' : '00001', 'zona' : '1A'},
        {'nombre' : 'Reptil engañoso', 'codigo' : '00002', 'zona' : '2A'},
        {'nombre' : 'Raptor', 'codigo' : '00792', 'zona' : '3A'},
        {'nombre' : 'T-REX', 'codigo' : '00003', 'zona' : '4A'},
        {'nombre' : 'Dientes de dos formas', 'codigo' : '00004', 'zona' : '2B'},
        {'nombre' : 'Sgimoloch', 'codigo' : '00010', 'zona' : '2C'},
        {'nombre' : 'T-REX', 'codigo' : '00005', 'zona' : '3B'},
        {'nombre' : 'T-REX', 'codigo' : '00006', 'zona' : '1P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00006', 'zona' : '2P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00007', 'zona' : '3P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00008', 'zona' : '4P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00009', 'zona' : '1F'},
        {'nombre' : 'Diplodocus', 'codigo' : '00012', 'zona' : '9P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00011', 'zona' : '8P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00013', 'zona' : '7P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00014', 'zona' : '6P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00015', 'zona' : '5P'}   
    ]
    
    arbol_dinosaurio_por_nombre = Arbol()
    arbol_dinosaurio_por_codigo = Arbol()
    
    #Punto 2
    arbol_dinosaurio_por_nombre = arbol_dinosaurio_por_nombre.cargar_arbol(dic_dinosaurios, 'nombre')
    arbol_dinosaurio_por_codigo = arbol_dinosaurio_por_codigo.cargar_arbol(dic_dinosaurios, 'codigo')
    
    #Punto 3
    print('Barrido inorden del arbol dinosaurios ordenado por nombres ')
    arbol_dinosaurio_por_nombre.inorden()
    
    #Punto 4
    print('\nMostrar toda la informacion del dinosaurio 792')
    print(arbol_dinosaurio_por_codigo.busqueda('00792').datos)
    
    #Punto 5
    print('\nMostrar toda la informacion de los T-rex')
    MostrarDinosauriosDeXOrden(arbol_dinosaurio_por_nombre, 'T-REX')
    
    #Punto 6
    print("\nModificar nombre de criatura mal cargada")
    info, datos  =  arbol_dinosaurio_por_nombre.eliminar_nodo('Sgimoloch')
    if info is not None:
        info = 'Stygimoloch'
        datos['nombre'] = 'Stygimoloch'
        arbol_dinosaurio_por_codigo.eliminar_nodo(datos['codigo'])
        arbol_dinosaurio_por_codigo = arbol_dinosaurio_por_codigo.insertar_nodo(datos['codigo'], datos)
        arbol_dinosaurio_por_nombre = arbol_dinosaurio_por_nombre.insertar_nodo(info, datos)
    
    #Punto 7
    print('\nMostrar todas las ubicaciones de los raptors')
    MostrarCampoDinosauriosDeXNombre(arbol_dinosaurio_por_nombre, 'Raptor', 'zona')

    #Punto 8
    print('\nContar cuantos diplodocus hay en el grafo')
    print('La cantidad de Diplodocus son de: ', ContarDinosauriosDeXOrden(arbol_dinosaurio_por_nombre, 'Diplodocus'))
    
    
    
ejercicio()