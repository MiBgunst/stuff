#Esta clase se encarga de extraer el texto y evaluarlo de diferentes maneras
class analisisTextual:
    def __init__(self): #constructor
        print("wot")
        
     #Esta funcion abre el archivo a analizar
    texto = []
    def Objetivo(self,file):
        objective = open(file, "r")
        texto = []
        for line in objective:
            texto.append(line)
        return texto
    
    def longitud(texto):
        for linea in texto:
            palabras = texto.split(" ")
            oraciones = texto.split(".")
            longitudGlobal = len(texto)
            print("Palabras en el texto: {0}/nOraciones en el texto: {1}/n Longitud total del texto: {2}".format(palabras, oraciones, longitudGlobal))
            
    def elementosGramaticales(texto):
        conectores = []
        puntuacion = []
        sustantivos y verbs = {not (conectores,puntuacion)} #***CORREGIR SINTAXIS***
        
        
    
        
        
    
        
    
        

        
texto = analisisTextual()
texto.Objetivo("maestrosyalumnos.txt")
texto.longitud()

"""test = open("maestrosyalumnos.txt")
lista = []
for i in test:
    lista.append(i)
print(lista)"""