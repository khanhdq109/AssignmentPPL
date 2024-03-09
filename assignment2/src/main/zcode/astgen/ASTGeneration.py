from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    ############################# PROGRAM ##############################
    # program: newlinelist decllistprime EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        decl = self.visit(ctx.decllistprime())
        return Program(decl)
    
    
    ############################### LIST ###############################
    # decllist: decllistprime | ;
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.decllistprime())
    
    # decllistprime: decl decllistprime | decl;
    def visitDecllistprime(self, ctx: ZCodeParser.DecllistprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decllistprime())
    
    # numlist: numlistprime | ;
    def visitNumlist(self, ctx: ZCodeParser.NumlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.numlistprime())
    
    # numlistprime: FLOATLIT COMMA numlistprime | FLOATLIT;
    def visitNumlistprime(self, ctx: ZCodeParser.NumlistprimeContext):
        if ctx.getChildCount() == 1:
            return [NumberLiteral(float(ctx.FLOATLIT().getText()))]
        return [NumberLiteral(float(ctx.FLOATLIT().getText()))] + self.visit(ctx.numlistprime())
    
    # paramdecllist: paramdecllistprime | ;
    def visitParamdecllist(self, ctx: ZCodeParser.ParamdecllistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramdecllistprime())
    
    # paramdecllistprime: paramdecl COMMA paramdecllistprime | paramdecl;
    def visitParamdecllistprime(self, ctx: ZCodeParser.ParamdecllistprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramdecl())]
        return [self.visit(ctx.paramdecl())] + self.visit(ctx.paramdecllistprime())
    
    # stmtlist: stmtlistprime | ;
    def visitStmtlist(self, ctx: ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtlistprime())
    
    # stmtlistprime: stmt stmtlistprime | stmt;
    def visitStmtlistprime(self, ctx: ZCodeParser.StmtlistprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlistprime())
    
    # explist: explistprime | ;
    def visitExplist(self, ctx: ZCodeParser.ExplistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.explistprime())
    
    # explistprime: exp COMMA explistprime | exp;
    def visitExplistprime(self, ctx: ZCodeParser.ExplistprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.explistprime())
    
    
    ############################ DECLARATION ###########################
    # decl: (vardecl | arrdecl | funcdecl) newlinelistprime;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        return self.visit(ctx.getChild(0))
    
    # vardecl: (typ | DYNAMIC) IDENTIFIER (ASSIGN exp)? | VAR IDENTIFIER ASSIGN exp;
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = None
        if ctx.typ():
            varType = self.visit(ctx.typ())
        modifier = None
        varInit = None
        if ctx.ASSIGN():
            varInit = self.visit(ctx.exp())
        return VarDecl(name, varType, modifier, varInit)
    
    # arrdecl: typ IDENTIFIER LSB numlistprime RSB (ASSIGN exp)?;
    def visitArrdecl(self, ctx: ZCodeParser.ArrdeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        size = self.visit(ctx.numlistprime())
        eleType = self.visit(ctx.typ())
        varType = ArrayType(size, eleType)
        modifier = None
        varInit = None
        if ctx.ASSIGN():
            varInit = self.visit(ctx.exp())
        return VarDecl(name, varType, modifier, varInit)
    
    # paramdecl: typ IDENTIFIER (LSB numlistprime RSB)?;
    def visitParamdecl(self, ctx: ZCodeParser.ParamdeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        if ctx.LSB():
            size = self.visit(ctx.numlistprime())
            eleType = self.visit(ctx.typ())
            varType = ArrayType(size, eleType)
        else:
            varType = self.visit(ctx.typ())
        modifier = None
        varInit = None
        return VarDecl(name, varType, modifier, varInit)
    
    # funcdecl: FUNC IDENTIFIER LB paramdecllist RB newlinelist (returnstmt | blockstmt)?;
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = self.visit(ctx.paramdecllist())
        body = None
        if ctx.returnstmt():
            body = self.visit(ctx.returnstmt())
        elif ctx.blockstmt():
            body = self.visit(ctx.blockstmt())
        return FuncDecl(name, param, body)
    
    ############################# STATEMENT ############################
    # stmt: notnewlinestmt newlinelistprime;
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        return self.visit(ctx.notnewlinestmt())
    
    # notnewlinestmt: vardecl | arrdecl | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | callstmt | blockstmt;
    def visitNotnewlinestmt(self, ctx: ZCodeParser.NotnewlinestmtContext):
        return self.visit(ctx.getChild(0))
    
    # assignstmt: lhs ASSIGN exp;
    def visitAssignstmt(self, ctx: ZCodeParser.AssignstmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)
    
    # ifstmt: IF exp newlinelist notnewlinestmt (newlinelistprime ELIF exp newlinelist notnewlinestmt)* (newlinelistprime ELSE newlinelist notnewlinestmt)?;
    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        explist = ctx.exp()
        stmtlist = ctx.notnewlinestmt()
        # if
        expr = explist[0]
        thenStmt = stmtlist[0]
        # elif
        elifStmt = []
        if ctx.ELIF():
            if ctx.ELSE():
                elifStmt = list(zip(explist[1:], stmtlist[1:-1]))
            else: elifStmt = list(zip(explist[1:], stmtlist[1:]))
        # else
        elseStmt = None
        if ctx.ELSE():
            elseStmt = stmtlist[-1]
        return If(expr, thenStmt, elifStmt, elseStmt)
    
    # forstmt: FOR IDENTIFIER UNTIL exp BY exp newlinelist notnewlinestmt;
    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = self.visit(ctx.exp(0))
        updExpr = self.visit(ctx.exp(1))
        body = self.visit(ctx.notnewlinestmt())
        return For(name, condExpr, updExpr, body)
    
    # breakstmt: BREAK;
    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        return Break()
    
    # continuestmt: CONTINUE;
    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        return Continue()
    
    # returnstmt: RETURN exp?;
    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        if ctx.getChildCount == 1:
            return None
        expr = self.visit(ctx.exp())
        return Return(expr)
    
    # callstmt: IDENTIFIER LB explist RB;
    def visitCallstmt(self, ctx: ZCodeParser.CallstmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.explist())
        return CallStmt(name, args)
    
    # blockstmt: BEGIN newlinelistprime stmtlist END;
    def visitBlockstmt(self, ctx: ZCodeParser.BlockstmtContext):
        stmt = self.visit(ctx.stmtlist())
        return Block(stmt)
    
    
    ############################# EXPRESSION ###########################
    # exp: exp1 CAT exp1 | exp1;
    def visitExp(self, ctx: ZCodeParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        left = self.visit(ctx.exp1(0))
        right = self.visit(ctx.exp1(1))
        return BinaryOp(ctx.CAT().getText(), left, right)
    
    # exp1: exp2 (EQ | COM | NEQ | LS | GR | LSE | GRE) exp2 | exp2;
    def visitExp1(self, ctx: ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        left = self.visit(ctx.exp2(0))
        right = self.visit(ctx.exp2(1))
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    
    # exp2: exp2 (AND | OR) exp3 | exp3;
    def visitExp2(self, ctx: ZCodeParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    
    # exp3: exp3 (ADD | SUB) exp4 | exp4;
    def visitExp3(self, ctx: ZCodeParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    
    # exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
    def visitExp4(self, ctx: ZCodeParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        left = self.visit(ctx.exp4())
        right = self.visit(ctx.exp5())
        return BinaryOp(ctx.getChild(1).getText(), left, right)
    
    # exp5: NOT exp5 | exp6;
    def visitExp5(self, ctx: ZCodeParser.Exp5Context):
        if ctx.getChildCount == 1:
            return self.visit(ctx.exp6())
        operand = self.visit(ctx.exp5())
        return UnaryOp(ctx.NOT().getText(), operand)
    
    # exp6: SUB exp6 | exp7;
    def visitExp6(self, ctx: ZCodeParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        operand = self.visit(ctx.exp6())
        return UnaryOp(ctx.SUB().getText(), operand)
    
    # exp7: (IDENTIFIER | callexp) LSB explistprime RSB | exp8;
    def visitExp7(self, ctx: ZCodeParser.Exp7Context):
        if ctx.getChildCount == 1:
            return self.visit(ctx.exp8())
        if ctx.callexp():
            arr = self.visit(ctx.callexp())
        else: arr = Id(ctx.IDENTIFIER().getText())
        idx = self.visit(ctx.explistprime())
        return ArrayCell(arr, idx)
    
    # exp8: IDENTIFIER | FLOATLIT | boollit | STRINGLIT | arraylit | LB exp RB | callexp;
    def visitExp8(self, ctx: ZCodeParser.Exp8Context):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.FLOATLIT():
            return NumberLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.boollit():
            return self.visit(ctx.boollit())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.exp():
            return self.visit(ctx.exp())
        return self.visit(ctx.callexp())
    
    
    ############################### OTHERS #############################
    # boollit: TRUE | FALSE;
    def visitBoollit(self, ctx: ZCodeParser.BoollitContext):
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText() == "true")
        return BooleanLiteral(ctx.FALSE().getText() == "true")
    
    # arraylit: LSB explist RSB;
    def visitArraylit(self, ctx: ZCodeParser.ArraylitContext):
        explist = self.visit(ctx.explist())
        return ArrayLiteral(explist)
    
    # typ: NUMBER | BOOL | STRING;
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()
    
    # lhs: IDENTIFIER | (IDENTIFIER | callexp) LSB explistprime RSB;
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        if ctx.callexp():
            arr = self.visit(ctx.callexp())
        else: arr = Id(ctx.IDENTIFIER().getText())
        idx = self.visit(ctx.explistprime())
        return ArrayCell(arr, idx)
        
    # callexp: IDENTIFIER LB explist RB;
    def visitCallexp(self, ctx: ZCodeParser.CallexpContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.explist())
        return CallExpr(name, args)
        