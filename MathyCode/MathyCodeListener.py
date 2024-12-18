# Generated from MathyCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathyCodeParser import MathyCodeParser
else:
    from MathyCodeParser import MathyCodeParser

# This class defines a complete listener for a parse tree produced by MathyCodeParser.
class MathyCodeListener(ParseTreeListener):

    # Enter a parse tree produced by MathyCodeParser#programa.
    def enterPrograma(self, ctx:MathyCodeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#programa.
    def exitPrograma(self, ctx:MathyCodeParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#instruccion.
    def enterInstruccion(self, ctx:MathyCodeParser.InstruccionContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#instruccion.
    def exitInstruccion(self, ctx:MathyCodeParser.InstruccionContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#declaracion.
    def enterDeclaracion(self, ctx:MathyCodeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#declaracion.
    def exitDeclaracion(self, ctx:MathyCodeParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#operacion.
    def enterOperacion(self, ctx:MathyCodeParser.OperacionContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#operacion.
    def exitOperacion(self, ctx:MathyCodeParser.OperacionContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#muestra.
    def enterMuestra(self, ctx:MathyCodeParser.MuestraContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#muestra.
    def exitMuestra(self, ctx:MathyCodeParser.MuestraContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#condicion.
    def enterCondicion(self, ctx:MathyCodeParser.CondicionContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#condicion.
    def exitCondicion(self, ctx:MathyCodeParser.CondicionContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#condicionLogica.
    def enterCondicionLogica(self, ctx:MathyCodeParser.CondicionLogicaContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#condicionLogica.
    def exitCondicionLogica(self, ctx:MathyCodeParser.CondicionLogicaContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#ciclo.
    def enterCiclo(self, ctx:MathyCodeParser.CicloContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#ciclo.
    def exitCiclo(self, ctx:MathyCodeParser.CicloContext):
        pass


    # Enter a parse tree produced by MathyCodeParser#comentario.
    def enterComentario(self, ctx:MathyCodeParser.ComentarioContext):
        pass

    # Exit a parse tree produced by MathyCodeParser#comentario.
    def exitComentario(self, ctx:MathyCodeParser.ComentarioContext):
        pass



del MathyCodeParser