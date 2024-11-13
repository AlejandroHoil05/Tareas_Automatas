# Generated from ./traductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .traductorParser import traductorParser
else:
    from traductorParser import traductorParser

# This class defines a complete listener for a parse tree produced by traductorParser.
class traductorListener(ParseTreeListener):

    # Enter a parse tree produced by traductorParser#program.
    def enterProgram(self, ctx:traductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by traductorParser#program.
    def exitProgram(self, ctx:traductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by traductorParser#functionDef.
    def enterFunctionDef(self, ctx:traductorParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by traductorParser#functionDef.
    def exitFunctionDef(self, ctx:traductorParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by traductorParser#parameters.
    def enterParameters(self, ctx:traductorParser.ParametersContext):
        pass

    # Exit a parse tree produced by traductorParser#parameters.
    def exitParameters(self, ctx:traductorParser.ParametersContext):
        pass


    # Enter a parse tree produced by traductorParser#statement.
    def enterStatement(self, ctx:traductorParser.StatementContext):
        pass

    # Exit a parse tree produced by traductorParser#statement.
    def exitStatement(self, ctx:traductorParser.StatementContext):
        pass


    # Enter a parse tree produced by traductorParser#expressionStatement.
    def enterExpressionStatement(self, ctx:traductorParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by traductorParser#expressionStatement.
    def exitExpressionStatement(self, ctx:traductorParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by traductorParser#returnStatement.
    def enterReturnStatement(self, ctx:traductorParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by traductorParser#returnStatement.
    def exitReturnStatement(self, ctx:traductorParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by traductorParser#printStatement.
    def enterPrintStatement(self, ctx:traductorParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by traductorParser#printStatement.
    def exitPrintStatement(self, ctx:traductorParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by traductorParser#expression.
    def enterExpression(self, ctx:traductorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by traductorParser#expression.
    def exitExpression(self, ctx:traductorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by traductorParser#term.
    def enterTerm(self, ctx:traductorParser.TermContext):
        pass

    # Exit a parse tree produced by traductorParser#term.
    def exitTerm(self, ctx:traductorParser.TermContext):
        pass


    # Enter a parse tree produced by traductorParser#factor.
    def enterFactor(self, ctx:traductorParser.FactorContext):
        pass

    # Exit a parse tree produced by traductorParser#factor.
    def exitFactor(self, ctx:traductorParser.FactorContext):
        pass


    # Enter a parse tree produced by traductorParser#arguments.
    def enterArguments(self, ctx:traductorParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by traductorParser#arguments.
    def exitArguments(self, ctx:traductorParser.ArgumentsContext):
        pass



del traductorParser