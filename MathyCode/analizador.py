from antlr4 import *
from MathyCodeLexer import MathyCodeLexer
from MathyCodeParser import MathyCodeParser
from MaToPython import MathyCodeToPythonConverter

def main():
    file_path = "programa.txt"

    # Lee el contenido del archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        mathy_code = file.read()

    # Configura el lexer con el contenido del archivo
    lexer = MathyCodeLexer(InputStream(mathy_code))
    token_stream = CommonTokenStream(lexer)

    # Inicializa el parser con el flujo de tokens
    parser = MathyCodeParser(token_stream)

    # Genera el árbol de sintaxis a partir de la regla principal
    tree = parser.programa()

    # Utiliza el listener para procesar el código
    converter = MathyCodeToPythonConverter()
    walker = ParseTreeWalker()
    walker.walk(converter, tree)

    # Genera el archivo Python
    py_code = converter.get_python_code()
    with open("FuncionConvertida.py", "w", encoding="utf-8") as py_file:
        py_file.write(py_code)

    print("Función convertida y guardada en FuncionConvertida.py")

if __name__ == "__main__":
    main()
