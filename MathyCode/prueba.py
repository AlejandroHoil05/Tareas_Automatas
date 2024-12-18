from antlr4 import *
from MathyCodeLexer import MathyCodeLexer  # Cambia el nombre según tu lexer generado
from MathyCodeParser import MathyCodeParser  # Cambia el nombre según tu parser generado
from MathyCodeListener import MathyCodeListener  # Cambia el nombre según tu listener generado, si es necesario


def main():
    # Nombre del archivo de texto con la función en Python
    file_path = "programa.txt"

    # Lee el contenido del archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    # Configura el lexer con el contenido del archivo
    lexer = MathyCodeLexer(InputStream(python_code))
    token_stream = CommonTokenStream(lexer)  # Crea el flujo de tokens

    # Inicializa el parser con el flujo de tokens
    parser = MathyCodeParser(token_stream)

    # Genera el árbol de sintaxis a partir de la regla principal
    tree = parser.programa()  # Cambia 'program' por la regla inicial de tu gramática, si es diferente

    # Imprime el árbol de sintaxis generado
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()
