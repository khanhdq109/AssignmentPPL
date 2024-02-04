# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u015a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\7\2r\n\2\f\2")
        buf.write("\16\2u\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\7,\u011c\n,\f,\16,\u011f\13,\3-\3-\3-")
        buf.write("\5-\u0124\n-\3-\5-\u0127\n-\3.\6.\u012a\n.\r.\16.\u012b")
        buf.write("\3/\3/\7/\u0130\n/\f/\16/\u0133\13/\3\60\3\60\5\60\u0137")
        buf.write("\n\60\3\60\6\60\u013a\n\60\r\60\16\60\u013b\3\61\3\61")
        buf.write("\3\61\3\61\3\61\7\61\u0143\n\61\f\61\16\61\u0146\13\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\6\63\u014e\n\63\r\63\16")
        buf.write("\63\u014f\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\2\2\67\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a/c\2e\60g\61i\62k\63\3\2")
        buf.write("\13\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2")
        buf.write("\n\13\16\17\"\"\2\u0162\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2a\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\3m\3\2\2\2\5x\3\2\2\2\7}\3\2\2\2\t\u0083\3\2")
        buf.write("\2\2\13\u008a\3\2\2\2\r\u008f\3\2\2\2\17\u0096\3\2\2\2")
        buf.write("\21\u009d\3\2\2\2\23\u00a1\3\2\2\2\25\u00a9\3\2\2\2\27")
        buf.write("\u00ae\3\2\2\2\31\u00b2\3\2\2\2\33\u00b8\3\2\2\2\35\u00bb")
        buf.write("\3\2\2\2\37\u00c1\3\2\2\2!\u00ca\3\2\2\2#\u00cd\3\2\2")
        buf.write("\2%\u00d2\3\2\2\2\'\u00d7\3\2\2\2)\u00dd\3\2\2\2+\u00e1")
        buf.write("\3\2\2\2-\u00e5\3\2\2\2/\u00e9\3\2\2\2\61\u00ec\3\2\2")
        buf.write("\2\63\u00ee\3\2\2\2\65\u00f0\3\2\2\2\67\u00f2\3\2\2\2")
        buf.write("9\u00f4\3\2\2\2;\u00f6\3\2\2\2=\u00f8\3\2\2\2?\u00fb\3")
        buf.write("\2\2\2A\u00fe\3\2\2\2C\u0100\3\2\2\2E\u0103\3\2\2\2G\u0105")
        buf.write("\3\2\2\2I\u0108\3\2\2\2K\u010c\3\2\2\2M\u010f\3\2\2\2")
        buf.write("O\u0111\3\2\2\2Q\u0113\3\2\2\2S\u0115\3\2\2\2U\u0117\3")
        buf.write("\2\2\2W\u0119\3\2\2\2Y\u0120\3\2\2\2[\u0129\3\2\2\2]\u012d")
        buf.write("\3\2\2\2_\u0134\3\2\2\2a\u013d\3\2\2\2c\u0149\3\2\2\2")
        buf.write("e\u014d\3\2\2\2g\u0153\3\2\2\2i\u0156\3\2\2\2k\u0158\3")
        buf.write("\2\2\2mn\7%\2\2no\7%\2\2os\3\2\2\2pr\n\2\2\2qp\3\2\2\2")
        buf.write("ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\b")
        buf.write("\2\2\2w\4\3\2\2\2xy\7v\2\2yz\7t\2\2z{\7w\2\2{|\7g\2\2")
        buf.write("|\6\3\2\2\2}~\7h\2\2~\177\7c\2\2\177\u0080\7n\2\2\u0080")
        buf.write("\u0081\7u\2\2\u0081\u0082\7g\2\2\u0082\b\3\2\2\2\u0083")
        buf.write("\u0084\7p\2\2\u0084\u0085\7w\2\2\u0085\u0086\7o\2\2\u0086")
        buf.write("\u0087\7d\2\2\u0087\u0088\7g\2\2\u0088\u0089\7t\2\2\u0089")
        buf.write("\n\3\2\2\2\u008a\u008b\7d\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7q\2\2\u008d\u008e\7n\2\2\u008e\f\3\2\2\2\u008f")
        buf.write("\u0090\7u\2\2\u0090\u0091\7v\2\2\u0091\u0092\7t\2\2\u0092")
        buf.write("\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094\u0095\7i\2\2\u0095")
        buf.write("\16\3\2\2\2\u0096\u0097\7t\2\2\u0097\u0098\7g\2\2\u0098")
        buf.write("\u0099\7v\2\2\u0099\u009a\7w\2\2\u009a\u009b\7t\2\2\u009b")
        buf.write("\u009c\7p\2\2\u009c\20\3\2\2\2\u009d\u009e\7x\2\2\u009e")
        buf.write("\u009f\7c\2\2\u009f\u00a0\7t\2\2\u00a0\22\3\2\2\2\u00a1")
        buf.write("\u00a2\7f\2\2\u00a2\u00a3\7{\2\2\u00a3\u00a4\7p\2\2\u00a4")
        buf.write("\u00a5\7c\2\2\u00a5\u00a6\7o\2\2\u00a6\u00a7\7k\2\2\u00a7")
        buf.write("\u00a8\7e\2\2\u00a8\24\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa")
        buf.write("\u00ab\7w\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7e\2\2\u00ad")
        buf.write("\26\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7q\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\30\3\2\2\2\u00b2\u00b3\7w\2\2\u00b3")
        buf.write("\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7n\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9")
        buf.write("\u00ba\7{\2\2\u00ba\34\3\2\2\2\u00bb\u00bc\7d\2\2\u00bc")
        buf.write("\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7c\2\2\u00bf")
        buf.write("\u00c0\7m\2\2\u00c0\36\3\2\2\2\u00c1\u00c2\7e\2\2\u00c2")
        buf.write("\u00c3\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write("\u00c6\7k\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7w\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9 \3\2\2\2\u00ca\u00cb\7k\2\2\u00cb")
        buf.write("\u00cc\7h\2\2\u00cc\"\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce")
        buf.write("\u00cf\7n\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("$\3\2\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7n\2\2\u00d4")
        buf.write("\u00d5\7k\2\2\u00d5\u00d6\7h\2\2\u00d6&\3\2\2\2\u00d7")
        buf.write("\u00d8\7d\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7i\2\2\u00da")
        buf.write("\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc(\3\2\2\2\u00dd")
        buf.write("\u00de\7g\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7f\2\2\u00e0")
        buf.write("*\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7q\2\2\u00e3")
        buf.write("\u00e4\7v\2\2\u00e4,\3\2\2\2\u00e5\u00e6\7c\2\2\u00e6")
        buf.write("\u00e7\7p\2\2\u00e7\u00e8\7f\2\2\u00e8.\3\2\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7t\2\2\u00eb\60\3\2\2\2\u00ec")
        buf.write("\u00ed\7-\2\2\u00ed\62\3\2\2\2\u00ee\u00ef\7/\2\2\u00ef")
        buf.write("\64\3\2\2\2\u00f0\u00f1\7,\2\2\u00f1\66\3\2\2\2\u00f2")
        buf.write("\u00f3\7\61\2\2\u00f38\3\2\2\2\u00f4\u00f5\7\'\2\2\u00f5")
        buf.write(":\3\2\2\2\u00f6\u00f7\7?\2\2\u00f7<\3\2\2\2\u00f8\u00f9")
        buf.write("\7>\2\2\u00f9\u00fa\7/\2\2\u00fa>\3\2\2\2\u00fb\u00fc")
        buf.write("\7#\2\2\u00fc\u00fd\7?\2\2\u00fd@\3\2\2\2\u00fe\u00ff")
        buf.write("\7>\2\2\u00ffB\3\2\2\2\u0100\u0101\7>\2\2\u0101\u0102")
        buf.write("\7?\2\2\u0102D\3\2\2\2\u0103\u0104\7@\2\2\u0104F\3\2\2")
        buf.write("\2\u0105\u0106\7@\2\2\u0106\u0107\7?\2\2\u0107H\3\2\2")
        buf.write("\2\u0108\u0109\7\60\2\2\u0109\u010a\7\60\2\2\u010a\u010b")
        buf.write("\7\60\2\2\u010bJ\3\2\2\2\u010c\u010d\7?\2\2\u010d\u010e")
        buf.write("\7?\2\2\u010eL\3\2\2\2\u010f\u0110\7*\2\2\u0110N\3\2\2")
        buf.write("\2\u0111\u0112\7+\2\2\u0112P\3\2\2\2\u0113\u0114\7]\2")
        buf.write("\2\u0114R\3\2\2\2\u0115\u0116\7_\2\2\u0116T\3\2\2\2\u0117")
        buf.write("\u0118\7\f\2\2\u0118V\3\2\2\2\u0119\u011d\t\3\2\2\u011a")
        buf.write("\u011c\t\4\2\2\u011b\u011a\3\2\2\2\u011c\u011f\3\2\2\2")
        buf.write("\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011eX\3\2\2")
        buf.write("\2\u011f\u011d\3\2\2\2\u0120\u0126\5[.\2\u0121\u0127\5")
        buf.write("]/\2\u0122\u0124\5]/\2\u0123\u0122\3\2\2\2\u0123\u0124")
        buf.write("\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\5_\60\2\u0126")
        buf.write("\u0121\3\2\2\2\u0126\u0123\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127Z\3\2\2\2\u0128\u012a\t\5\2\2\u0129\u0128\3\2\2")
        buf.write("\2\u012a\u012b\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\\\3\2\2\2\u012d\u0131\7\60\2\2\u012e\u0130")
        buf.write("\t\5\2\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132^\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0134\u0136\t\6\2\2\u0135\u0137\t\7\2\2")
        buf.write("\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3")
        buf.write("\2\2\2\u0138\u013a\t\5\2\2\u0139\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("`\3\2\2\2\u013d\u0144\7$\2\2\u013e\u0143\n\b\2\2\u013f")
        buf.write("\u0143\5c\62\2\u0140\u0141\7)\2\2\u0141\u0143\7$\2\2\u0142")
        buf.write("\u013e\3\2\2\2\u0142\u013f\3\2\2\2\u0142\u0140\3\2\2\2")
        buf.write("\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3")
        buf.write("\2\2\2\u0145\u0147\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148")
        buf.write("\7$\2\2\u0148b\3\2\2\2\u0149\u014a\7^\2\2\u014a\u014b")
        buf.write("\t\t\2\2\u014bd\3\2\2\2\u014c\u014e\t\n\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\b\63\2")
        buf.write("\2\u0152f\3\2\2\2\u0153\u0154\13\2\2\2\u0154\u0155\b\64")
        buf.write("\3\2\u0155h\3\2\2\2\u0156\u0157\13\2\2\2\u0157j\3\2\2")
        buf.write("\2\u0158\u0159\13\2\2\2\u0159l\3\2\2\2\16\2s\u011d\u0123")
        buf.write("\u0126\u012b\u0131\u0136\u013b\u0142\u0144\u014f\4\b\2")
        buf.write("\2\3\64\2")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    RETURN = 7
    VAR = 8
    DYNAMIC = 9
    FUNC = 10
    FOR = 11
    UNTIL = 12
    BY = 13
    BREAK = 14
    CONTINUE = 15
    IF = 16
    ELSE = 17
    ELIF = 18
    BEGIN = 19
    END = 20
    NOT = 21
    AND = 22
    OR = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQ = 29
    ASSIGN = 30
    NEQ = 31
    LS = 32
    LSE = 33
    GR = 34
    GRE = 35
    CAT = 36
    COM = 37
    LB = 38
    RB = 39
    LSB = 40
    RSB = 41
    NEWLINE = 42
    IDENTIFIER = 43
    FLOATLIT = 44
    STRINGLIT = 45
    WS = 46
    ERROR_TOKEN = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
            "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NEQ", 
            "LS", "LSE", "GR", "GRE", "CAT", "COM", "LB", "RB", "LSB", "RSB", 
            "NEWLINE", "IDENTIFIER", "FLOATLIT", "STRINGLIT", "WS", "ERROR_TOKEN", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LINE_COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQ", "ASSIGN", "NEQ", "LS", "LSE", "GR", "GRE", "CAT", 
                  "COM", "LB", "RB", "LSB", "RSB", "NEWLINE", "IDENTIFIER", 
                  "FLOATLIT", "INTPART", "DECPART", "EXPPART", "STRINGLIT", 
                  "ESCAPE", "WS", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


