from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    ############################# PROGRAM ##############################
    # program: newlinelist decllistprime EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        pass
    
    
    ############################### LIST ###############################
    # decllist: decllistprime | ;
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        pass
    
    # decllistprime: decl decllistprime | decl;
    def visitDecllistprime(self, ctx: ZCodeParser.DecllistprimeContext):
        pass
    
    # numlist: numlistprime | ;
    def visitNumlist(self, ctx: ZCodeParser.NumlistContext):
        pass
    
    # numlistprime: FLOATLIT COMMA numlistprime | FLOATLIT;
    def visitNumlistprime(self, ctx: ZCodeParser.NumlistprimeContext):
        pass
    
    # paramdecllist: paramdecllistprime | ;
    def visitParamdecllist(self, ctx: ZCodeParser.ParamdecllistContext):
        pass
    
    # paramdecllistprime: paramdecl COMMA paramdecllistprime | paramdecl;
    def visitParamdecllistprime(self, ctx: ZCodeParser.ParamdecllistprimeContext):
        pass
    
    # newlinelist: newlinelistprime | ;
    def visitNewlinelist(self, ctx: ZCodeParser.NewlinelistContext):
        pass
    
    # newlinelistprime: NEWLINE newlinelistprime | NEWLINE;
    def visitNewlinelistprime(self, ctx: ZCodeParser.NewlinelistprimeContext):
        pass
    
    # stmtlist: stmtlistprime | ;
    def visitStmtlist(self, ctx: ZCodeParser.StmtlistContext):
        pass
    
    # stmtlistprime: stmt stmtlistprime | stmt;
    def visitStmtlistprime(self, ctx: ZCodeParser.StmtlistprimeContext):
        pass
    
    # explist: explistprime | ;
    def visitExplist(self, ctx: ZCodeParser.ExplistContext):
        pass
    
    # explistprime: exp COMMA explistprime | exp;
    def visitExplistprime(self, ctx: ZCodeParser.ExplistprimeContext):
        pass
    
    
    ############################ DECLARATION ###########################
    # decl: (vardecl | arrdecl | funcdecl) newlinelistprime;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        pass
    
    # vardecl: (typ | DYNAMIC) IDENTIFIER (ASSIGN exp)? | VAR IDENTIFIER ASSIGN exp;
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        pass
    
    # arrdecl: typ IDENTIFIER LSB numlistprime RSB (ASSIGN exp)?;
    def visitArrdecl(self, ctx: ZCodeParser.ArrdeclContext):
        pass
    
    # paramdecl: typ IDENTIFIER (LSB numlistprime RSB)?;
    def visitParamdecl(self, ctx: ZCodeParser.ParamdeclContext):
        pass
    
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        pass
    
    ############################# STATEMENT ############################
    # stmt: notnewlinestmt newlinelistprime;
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        pass
    
    # notnewlinestmt: vardecl | arrdecl | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | callstmt | blockstmt;
    def visitNotnewlinestmt(self, ctx: ZCodeParser.NotnewlinestmtContext):
        pass
    
    # assignstmt: lhs ASSIGN exp;
    def visitAssignstmt(self, ctx: ZCodeParser.AssignstmtContext):
        pass
    
    # ifstmt: IF exp newlinelist notnewlinestmt (newlinelistprime ELIF exp newlinelist notnewlinestmt)* (newlinelistprime ELSE newlinelist notnewlinestmt)?;
    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        pass
    
    # forstmt: FOR IDENTIFIER UNTIL exp BY exp newlinelist notnewlinestmt;
    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        pass
    
    # breakstmt: BREAK;
    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        pass
    
    # continuestmt: CONTINUE;
    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        pass
    
    # returnstmt: RETURN exp?;
    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        pass
    
    # callstmt: IDENTIFIER LB explist RB;
    def visitCallstmt(self, ctx: ZCodeParser.CallstmtContext):
        pass
    
    # blockstmt: BEGIN newlinelistprime stmtlist END;
    def visitBlockstmt(self, ctx: ZCodeParser.BlockstmtContext):
        pass
    
    
    ############################# EXPRESSION ###########################
    # exp: exp1 CAT exp1 | exp1;
    def visitExp(self, ctx: ZCodeParser.ExpContext):
        pass
    
    # exp1: exp2 relational exp2 | exp2;
    def visitExp1(self, ctx: ZCodeParser.Exp1Context):
        pass
    
    # exp2: exp2 logical exp3 | exp3;
    def visitExp2(self, ctx: ZCodeParser.Exp2Context):
        pass
    
    # exp3: exp3 adding exp4 | exp4;
    def visitExp3(self, ctx: ZCodeParser.Exp3Context):
        pass
    
    # exp4: exp4 multiplying exp5 | exp5;
    def visitExp4(self, ctx: ZCodeParser.Exp4Context):
        pass
    
    # exp5: NOT exp5 | exp6;
    def visitExp5(self, ctx: ZCodeParser.Exp5Context):
        pass
    
    # exp6: SUB exp6 | exp7;
    def visitExp6(self, ctx: ZCodeParser.Exp6Context):
        pass
    
    # exp7: (IDENTIFIER | callstmt) LSB explistprime RSB | exp8;
    def visitExp7(self, ctx: ZCodeParser.Exp7Context):
        pass
    
    # exp8: IDENTIFIER | FLOATLIT | boollit | STRINGLIT | LSB explist RSB | LB exp RB | callstmt;
    def visitExp8(self, ctx: ZCodeParser.Exp8Context):
        pass
    
    
    ############################### OTHERS #############################
    # boollit: TRUE | FALSE;
    def visitBoollit(self, ctx: ZCodeParser.BoollitContext):
        pass
    
    # typ: NUMBER | BOOL | STRING;
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        pass
    
    # lhs: IDENTIFIER | (IDENTIFIER | callstmt) LSB explistprime RSB;
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        pass