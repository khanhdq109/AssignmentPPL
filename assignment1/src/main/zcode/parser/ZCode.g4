// Dao Quoc Khanh - 2013452

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: ;

///////////////////////// PARSER /////////////////////////
// Definition

// List

// Declaration

// Statement

// Expression

// Others
boollit: TRUE | FALSE;

///////////////////////// LEXER /////////////////////////
// Comments
LINE_COMMENT: '##' ~[\r\n]* -> skip;

// Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
ASSIGN: '<-';
NEQ: '!=';
LS: '<';
LSE: '<=';
GR: '>';
GRE: '>=';
CAT: '...';
COM: '==';

// Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
NEWLINE: '\n';

// Literal
//// Identifier literals
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

//// Type literals
FLOATLIT: INTPART (DECPART | DECPART? EXPPART)?;
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;
STRINGLIT: '"' (~["\\\r\n] | ESCAPE | '\'"')* '"';
fragment ESCAPE: '\\' [bfrnt'\\];

//// Skip, errors
WS: [ \t\b\f\r]+ -> skip; // skip spaces, tabs, newlines
ERROR_TOKEN: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;