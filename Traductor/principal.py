# Jose Alejandro Castillo Hoil

from antlr4 import *
from traductorLexer import traductorLexer
from traductorParser import traductorParser
from convertidor import convertidor

def main():
    # Definir la ruta del archivo de entrada
    ruta_archivo = "operacion.txt"

    # Lectura del contenido del archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        codigo_python = archivo.read()

    # Crear lexer y parser para analizar el contenido
    lexer = traductorLexer(InputStream(codigo_python))
    token_stream = CommonTokenStream(lexer)
    parser = traductorParser(token_stream)

    # Generación del árbol de sintaxis usando la regla 'program'
    arbol_sintaxis = parser.program()

    # Inicializar el convertidor y realizar la conversión
    conversor = convertidor()
    ParseTreeWalker().walk(conversor, arbol_sintaxis)

    # Generación y escritura del archivo Java
    codigo_java = conversor.get_java_code()
    with open("archivoConvertido.java", "w") as archivo_java:
        archivo_java.write("public class archivoConvertido {\n")
        archivo_java.write(codigo_java)
        archivo_java.write("\n}")

    print("Conversión completada en archivoConvertido.java")

if __name__ == '__main__':
    main()
