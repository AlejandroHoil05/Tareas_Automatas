# Jose Alejandro Castillo Hoil

from traductorParser import traductorParser
from traductorListener import traductorListener


class convertidor(traductorListener):
    def __init__(self):
        super().__init__()
        self.codigo_java = []
        self.nombre_funcion = ""
        self.argumentos = ""

    def enterFunctionDef(self, ctx: traductorParser.FunctionDefContext):
        self.nombre_funcion = ctx.IDENTIFIER().getText()
        # Convertir parámetros de función a formato Java (int)
        parametros = ctx.parameters().getText()
        parametros_java = ', '.join([f"int {param.strip()}" for param in parametros.split(',')])
        self.codigo_java.append(f"public static int {self.nombre_funcion}({parametros_java}) " + "{")

    def exitFunctionDef(self, ctx: traductorParser.FunctionDefContext):
        self.codigo_java.append("}")

    def enterExpressionStatement(self, ctx: traductorParser.ExpressionStatementContext):
        nombre_variable = ctx.IDENTIFIER().getText()
        expresion = ctx.expression().getText()
        self.codigo_java.append(f"    int {nombre_variable} = {expresion};")

    def enterReturnStatement(self, ctx: traductorParser.ReturnStatementContext):
        expresion = ctx.expression().getText()
        self.codigo_java.append(f"    return {expresion};")

    def enterPrintStatement(self, ctx: traductorParser.PrintStatementContext):
        # Convertir print de Python a System.out.println de Java
        self.argumentos = ctx.arguments().getText()

    def get_java_code(self):
        # Agregar método main para ejecutar la función
        codigo_main = [
            "public static void main(String[] args) {",
            f"    System.out.println({self.nombre_funcion}({self.argumentos}));",
            "}"
        ]
        return "\n".join(self.codigo_java + codigo_main)
