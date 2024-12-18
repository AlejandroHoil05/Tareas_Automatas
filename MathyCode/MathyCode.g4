grammar MathyCode;

// Lexer rules
EMPEZAR : 'EMPEZAR' ;
FIN : 'FIN' ;

TESORO : 'TESORO' ;
RESPUESTA : 'RESPUESTA' ;
VERDADERO : 'VERDADERO' ;
FALSO : 'FALSO' ;

COMBINA : 'COMBINA' ;
QUITA   : 'QUITA' ;
MULTIPLICA : 'MULTIPLICA' ;
DIVIDE  : 'DIVIDE' ;
DESCUBRE : 'DESCUBRE' ;
POTENCIA : 'POTENCIA' ;
RAIZ : 'RAIZ' ;

MUESTRA : 'MUESTRA' ;
NOTA : 'NOTA' ;

ELIGE : 'ELIGE' ;
ENTRE : 'ENTRE' ;

CON : 'CON' ;
DE : 'DE' ;
POR : 'POR' ;

SI : 'SI' ;
ENTONCES : 'ENTONCES' ;
MIENTRAS : 'MIENTRAS' ;
Y : 'Y' ;

MAYOR : 'MAYOR' ;
MENOR : 'MENOR' ;
IGUAL : 'IGUAL' ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
STRING : '"' .*? '"' ;

WS : [ \t\r\n]+ -> skip ;

// Parser rules
programa : EMPEZAR instruccion+ FIN ;

instruccion
    : declaracion
    | operacion
    | condicion
    | ciclo
    | muestra
    | comentario
    ;

declaracion
    : TESORO ID '=' NUMBER
    | RESPUESTA ID '=' (VERDADERO | FALSO)
    ;

operacion
    : COMBINA ID CON (ID | NUMBER)
    | QUITA ID DE (ID | NUMBER)
    | MULTIPLICA ID POR (ID | NUMBER)
    | DIVIDE ID ENTRE (ID | NUMBER)
    | DESCUBRE RAIZ DE ID
    | POTENCIA ID
    ;

muestra : MUESTRA (ID | STRING) ;

condicion : SI condicionLogica ENTONCES instruccion+ FIN ;

condicionLogica
    : (ID | NUMBER) MAYOR (ID | NUMBER)
    | (ID | NUMBER) MENOR (ID | NUMBER)
    | (ID | NUMBER) IGUAL (ID | NUMBER)
    | RESPUESTA
    ;

ciclo : MIENTRAS condicionLogica instruccion+ FIN ;

comentario : NOTA STRING ;