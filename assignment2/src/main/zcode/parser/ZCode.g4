// Dao Quoc Khanh - 2013452

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: newlinelist decllistprime EOF;

///////////////////////// PARSER /////////////////////////
// List
decllist: decllistprime | ;
decllistprime: decl decllistprime | decl;
numlist: numlistprime | ;
numlistprime: FLOATLIT COMMA numlistprime | FLOATLIT;
paramdecllist: paramdecllistprime | ;
paramdecllistprime: paramdecl COMMA paramdecllistprime | paramdecl;
newlinelist: newlinelistprime | ;
newlinelistprime: NEWLINE newlinelistprime | NEWLINE;
stmtlist: stmtlistprime | ;
stmtlistprime: stmt stmtlistprime | stmt;
explist: explistprime | ;
explistprime: exp COMMA explistprime | exp;

// Declaration
decl: (vardecl | arrdecl | funcdecl) newlinelistprime;
vardecl: (typ | DYNAMIC) IDENTIFIER (ASSIGN exp)?
	| VAR IDENTIFIER ASSIGN exp;
arrdecl: typ IDENTIFIER LSB numlistprime RSB (ASSIGN exp)?;
paramdecl: typ IDENTIFIER (LSB numlistprime RSB)?;
funcdecl: FUNC IDENTIFIER LB paramdecllist RB newlinelist (returnstmt | blockstmt)?;

// Statement
stmt: notnewlinestmt newlinelistprime;
notnewlinestmt: vardecl | arrdecl | assignstmt | ifstmt | forstmt 
	| breakstmt | continuestmt | returnstmt | callstmt | blockstmt;
assignstmt: lhs ASSIGN exp;
ifstmt: IF exp newlinelist notnewlinestmt (newlinelistprime ELIF exp newlinelist notnewlinestmt)* (newlinelistprime ELSE newlinelist notnewlinestmt)?;
forstmt: FOR IDENTIFIER UNTIL exp BY exp newlinelist notnewlinestmt;
breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN exp?;
callstmt: IDENTIFIER LB explist RB;
blockstmt: BEGIN newlinelistprime stmtlist END;

// Expression
exp: exp1 CAT exp1 | exp1;
exp1: exp2 (EQ | COM | NEQ | LS | GR | LSE | GRE) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: (IDENTIFIER | callexp) LSB explistprime RSB | exp8;
exp8: IDENTIFIER | FLOATLIT | boollit | STRINGLIT | arraylit | LB exp RB | callexp;

// Others
boollit: TRUE | FALSE;
arraylit: LSB explist RSB;
typ: NUMBER | BOOL | STRING;
lhs: IDENTIFIER | (IDENTIFIER | callexp) LSB explistprime RSB;
callexp: IDENTIFIER LB explist RB;

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
COMMA: ',';
NEWLINE: '\n';

// Literal
//// Identifier literals
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;

//// Type literals
FLOATLIT: INTPART (DECPART | DECPART? EXPPART)?;
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;
STRINGLIT: '"' (~["\\\r\n] | ESCAPE | '\'"')* '"' {
	self.text = self.text[1:-1]
};
fragment ESCAPE: '\\' [bfrnt'\\];

//// Skip, errors
WS: [ \t\b\f\r]+ -> skip; // skip spaces, tabs, newlines
UNCLOSE_STRING: '"' (~["\\\r\n] | ESCAPE | '\'"')* EOF? {
	raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESCAPE | '\'"')* ('\\' ~[bfrnt'\\]) {
	self.text = self.text[1:]
	index = 0
	for i in self.text:
		if i == '\\': break
		index += 1
	raise IllegalEscape(self.text[:index + 2])
};
ERROR_TOKEN: . {raise ErrorToken(self.text)};