from MathyCodeListener import MathyCodeListener
from MathyCodeParser import MathyCodeParser


class MathyCodeToPythonConverter(MathyCodeListener):
    def __init__(self):
        self.python_code = ["if __name__ == \"__main__\":"]  # Lista para almacenar el código Python
        self.indentation = "    "  # Indentación inicial
        self.variables = {}  # Variables declaradas
        self.in_while_loop = False  # Variable para saber si estamos dentro de un ciclo "MIENTRAS"

    def get_python_code(self):
        """Devuelve el código Python generado como una cadena."""
        return "\n".join(self.python_code)

    def add_line(self, line):
        """Agrega una línea al código Python con la indentación actual."""
        self.python_code.append(f"{self.indentation}{line}")

    def enterPrograma(self, ctx):
        self.add_line("# Inicio del programa")

    def exitPrograma(self, ctx):
        self.add_line("# Fin del programa")

    def enterDeclaracion(self, ctx):
        var_name = ctx.ID().getText()
        value = ctx.NUMBER().getText()
        self.variables[var_name] = value
        self.add_line(f"{var_name} = {value}")

    def enterOperacion(self, ctx):
        op = ctx.getChild(0).getText()  # Operación (COMBINA, QUITA, MULTIPLICA, etc.)
        var1 = ctx.ID(0).getText()  # Primer operando
        var2_node = None

        # Comprobamos si hay un segundo operando (para algunas operaciones como POTENCIA)
        if len(ctx.children) > 3:
            var2_node = ctx.getChild(3)  # Segundo operando puede ser ID o NUMBER

        # Verificamos si el operando es un número o una variable
        if var2_node:
            if var2_node.getSymbol().type == MathyCodeParser.NUMBER:
                var2 = var2_node.getText()
            elif var2_node.getSymbol().type == MathyCodeParser.ID:
                var2 = var2_node.getText()
            else:
                raise ValueError("Operando desconocido: " + var2_node.getText())
        else:
            var2 = None  # Para operaciones como DESCUBRE o POTENCIA sin segundo operando

        if self.in_while_loop:  # Estamos dentro de un ciclo "MIENTRAS"
            if op == "COMBINA":
                self.add_line(f"{var1} = {var1} + {var2}")
            elif op == "QUITA":
                self.add_line(f"{var1} = {var1} - {var2}")
            elif op == "MULTIPLICA":
                self.add_line(f"{var1} = {var1} * {var2}")
            elif op == "DIVIDE":
                self.add_line(f"{var1} = {var1} / {var2}")
        else:  # No estamos dentro de un ciclo
            if op == "COMBINA":
                self.add_line(f"resultado = {var1} + {var2}")
            elif op == "QUITA":
                self.add_line(f"resultado = {var1} - {var2}")
            elif op == "MULTIPLICA":
                self.add_line(f"resultado = {var1} * {var2}")
            elif op == "DIVIDE":
                self.add_line(f"resultado = {var1} / {var2}")
            elif op == "POTENCIA":
                if var2:  # Si hay un segundo operando (exponente)
                    self.add_line(f"resultado = {var1} ** {var2}")  # Potencia en Python
                else:
                    self.add_line(f"resultado = {var1} ** 2")  # Por defecto, al cuadrado
            elif op == "DESCUBRE":
                self.add_line(f"resultado = {var1} ** 0.5")  # Raíz cuadrada en Python

    def enterMuestra(self, ctx):
        if ctx.ID():  # Si es una variable
            var_name = ctx.ID().getText()
            if var_name in self.variables or var_name == "resultado":
                self.add_line(f"print({var_name})")
            else:
                self.add_line(f"print('Variable {var_name} no encontrada')")
        elif ctx.STRING():  # Si es una cadena
            string_value = ctx.STRING().getText()
            self.add_line(f"print({string_value})")

    def enterCondicion(self, ctx):
        condition = " ".join([child.getText() for child in ctx.children[:-1]])
        self.add_line(f"if {condition}:")
        self.indentation += "    "

    def exitCondicion(self, ctx):
        self.indentation = self.indentation[:-4]

    def enterCiclo(self, ctx):
        left = ctx.condicionLogica().getChild(0).getText()
        operator = ctx.condicionLogica().getChild(1).getText()
        right = ctx.condicionLogica().getChild(2).getText()
        python_operator = self.convert_operator(operator)
        self.add_line(f"while {left} {python_operator} {right}:")
        self.indentation += "    "
        self.in_while_loop = True  # Activar el indicador de que estamos dentro de un ciclo

    def exitCiclo(self, ctx):
        self.indentation = self.indentation[:-4]
        self.in_while_loop = False  # Salimos del ciclo

    def convert_operator(self, operator):
        return {
            "MAYOR": ">",
            "MENOR": "<",
            "IGUAL": "=="
        }.get(operator, operator)
