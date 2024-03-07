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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0179\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\7")
        buf.write("\2t\n\2\f\2\16\2w\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\7-\u0120\n-\f-\16-\u0123")
        buf.write("\13-\3.\3.\3.\5.\u0128\n.\3.\5.\u012b\n.\3/\6/\u012e\n")
        buf.write("/\r/\16/\u012f\3\60\3\60\7\60\u0134\n\60\f\60\16\60\u0137")
        buf.write("\13\60\3\61\3\61\5\61\u013b\n\61\3\61\6\61\u013e\n\61")
        buf.write("\r\61\16\61\u013f\3\62\3\62\3\62\3\62\3\62\7\62\u0147")
        buf.write("\n\62\f\62\16\62\u014a\13\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\6\64\u0153\n\64\r\64\16\64\u0154\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\7\65\u015e\n\65\f\65\16\65\u0161")
        buf.write("\13\65\3\65\5\65\u0164\n\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\7\66\u016d\n\66\f\66\16\66\u0170\13\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\67\3\67\3\67\2\28\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2")
        buf.write("_\2a\2c\60e\2g\61i\62k\63m\64\3\2\13\4\2\f\f\17\17\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\6\2\f\f")
        buf.write("\17\17$$^^\t\2))^^ddhhppttvv\5\2\n\13\16\17\"\"\2\u0188")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2c\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3")
        buf.write("\2\2\2\5z\3\2\2\2\7\177\3\2\2\2\t\u0085\3\2\2\2\13\u008c")
        buf.write("\3\2\2\2\r\u0091\3\2\2\2\17\u0098\3\2\2\2\21\u009f\3\2")
        buf.write("\2\2\23\u00a3\3\2\2\2\25\u00ab\3\2\2\2\27\u00b0\3\2\2")
        buf.write("\2\31\u00b4\3\2\2\2\33\u00ba\3\2\2\2\35\u00bd\3\2\2\2")
        buf.write("\37\u00c3\3\2\2\2!\u00cc\3\2\2\2#\u00cf\3\2\2\2%\u00d4")
        buf.write("\3\2\2\2\'\u00d9\3\2\2\2)\u00df\3\2\2\2+\u00e3\3\2\2\2")
        buf.write("-\u00e7\3\2\2\2/\u00eb\3\2\2\2\61\u00ee\3\2\2\2\63\u00f0")
        buf.write("\3\2\2\2\65\u00f2\3\2\2\2\67\u00f4\3\2\2\29\u00f6\3\2")
        buf.write("\2\2;\u00f8\3\2\2\2=\u00fa\3\2\2\2?\u00fd\3\2\2\2A\u0100")
        buf.write("\3\2\2\2C\u0102\3\2\2\2E\u0105\3\2\2\2G\u0107\3\2\2\2")
        buf.write("I\u010a\3\2\2\2K\u010e\3\2\2\2M\u0111\3\2\2\2O\u0113\3")
        buf.write("\2\2\2Q\u0115\3\2\2\2S\u0117\3\2\2\2U\u0119\3\2\2\2W\u011b")
        buf.write("\3\2\2\2Y\u011d\3\2\2\2[\u0124\3\2\2\2]\u012d\3\2\2\2")
        buf.write("_\u0131\3\2\2\2a\u0138\3\2\2\2c\u0141\3\2\2\2e\u014e\3")
        buf.write("\2\2\2g\u0152\3\2\2\2i\u0158\3\2\2\2k\u0167\3\2\2\2m\u0176")
        buf.write("\3\2\2\2op\7%\2\2pq\7%\2\2qu\3\2\2\2rt\n\2\2\2sr\3\2\2")
        buf.write("\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2x")
        buf.write("y\b\2\2\2y\4\3\2\2\2z{\7v\2\2{|\7t\2\2|}\7w\2\2}~\7g\2")
        buf.write("\2~\6\3\2\2\2\177\u0080\7h\2\2\u0080\u0081\7c\2\2\u0081")
        buf.write("\u0082\7n\2\2\u0082\u0083\7u\2\2\u0083\u0084\7g\2\2\u0084")
        buf.write("\b\3\2\2\2\u0085\u0086\7p\2\2\u0086\u0087\7w\2\2\u0087")
        buf.write("\u0088\7o\2\2\u0088\u0089\7d\2\2\u0089\u008a\7g\2\2\u008a")
        buf.write("\u008b\7t\2\2\u008b\n\3\2\2\2\u008c\u008d\7d\2\2\u008d")
        buf.write("\u008e\7q\2\2\u008e\u008f\7q\2\2\u008f\u0090\7n\2\2\u0090")
        buf.write("\f\3\2\2\2\u0091\u0092\7u\2\2\u0092\u0093\7v\2\2\u0093")
        buf.write("\u0094\7t\2\2\u0094\u0095\7k\2\2\u0095\u0096\7p\2\2\u0096")
        buf.write("\u0097\7i\2\2\u0097\16\3\2\2\2\u0098\u0099\7t\2\2\u0099")
        buf.write("\u009a\7g\2\2\u009a\u009b\7v\2\2\u009b\u009c\7w\2\2\u009c")
        buf.write("\u009d\7t\2\2\u009d\u009e\7p\2\2\u009e\20\3\2\2\2\u009f")
        buf.write("\u00a0\7x\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7t\2\2\u00a2")
        buf.write("\22\3\2\2\2\u00a3\u00a4\7f\2\2\u00a4\u00a5\7{\2\2\u00a5")
        buf.write("\u00a6\7p\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7o\2\2\u00a8")
        buf.write("\u00a9\7k\2\2\u00a9\u00aa\7e\2\2\u00aa\24\3\2\2\2\u00ab")
        buf.write("\u00ac\7h\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7p\2\2\u00ae")
        buf.write("\u00af\7e\2\2\u00af\26\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1")
        buf.write("\u00b2\7q\2\2\u00b2\u00b3\7t\2\2\u00b3\30\3\2\2\2\u00b4")
        buf.write("\u00b5\7w\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7")
        buf.write("\u00b8\7k\2\2\u00b8\u00b9\7n\2\2\u00b9\32\3\2\2\2\u00ba")
        buf.write("\u00bb\7d\2\2\u00bb\u00bc\7{\2\2\u00bc\34\3\2\2\2\u00bd")
        buf.write("\u00be\7d\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write("\u00c1\7c\2\2\u00c1\u00c2\7m\2\2\u00c2\36\3\2\2\2\u00c3")
        buf.write("\u00c4\7e\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\u00c7\7v\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7p\2\2\u00c9")
        buf.write("\u00ca\7w\2\2\u00ca\u00cb\7g\2\2\u00cb \3\2\2\2\u00cc")
        buf.write("\u00cd\7k\2\2\u00cd\u00ce\7h\2\2\u00ce\"\3\2\2\2\u00cf")
        buf.write("\u00d0\7g\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7u\2\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\u00d6\7n\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7h\2\2\u00d8")
        buf.write("&\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\u00dc\7i\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("(\3\2\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7p\2\2\u00e1")
        buf.write("\u00e2\7f\2\2\u00e2*\3\2\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7v\2\2\u00e6,\3\2\2\2\u00e7")
        buf.write("\u00e8\7c\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7f\2\2\u00ea")
        buf.write(".\3\2\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\60\3\2\2\2\u00ee\u00ef\7-\2\2\u00ef\62\3\2\2\2\u00f0")
        buf.write("\u00f1\7/\2\2\u00f1\64\3\2\2\2\u00f2\u00f3\7,\2\2\u00f3")
        buf.write("\66\3\2\2\2\u00f4\u00f5\7\61\2\2\u00f58\3\2\2\2\u00f6")
        buf.write("\u00f7\7\'\2\2\u00f7:\3\2\2\2\u00f8\u00f9\7?\2\2\u00f9")
        buf.write("<\3\2\2\2\u00fa\u00fb\7>\2\2\u00fb\u00fc\7/\2\2\u00fc")
        buf.write(">\3\2\2\2\u00fd\u00fe\7#\2\2\u00fe\u00ff\7?\2\2\u00ff")
        buf.write("@\3\2\2\2\u0100\u0101\7>\2\2\u0101B\3\2\2\2\u0102\u0103")
        buf.write("\7>\2\2\u0103\u0104\7?\2\2\u0104D\3\2\2\2\u0105\u0106")
        buf.write("\7@\2\2\u0106F\3\2\2\2\u0107\u0108\7@\2\2\u0108\u0109")
        buf.write("\7?\2\2\u0109H\3\2\2\2\u010a\u010b\7\60\2\2\u010b\u010c")
        buf.write("\7\60\2\2\u010c\u010d\7\60\2\2\u010dJ\3\2\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f\u0110\7?\2\2\u0110L\3\2\2\2\u0111\u0112")
        buf.write("\7*\2\2\u0112N\3\2\2\2\u0113\u0114\7+\2\2\u0114P\3\2\2")
        buf.write("\2\u0115\u0116\7]\2\2\u0116R\3\2\2\2\u0117\u0118\7_\2")
        buf.write("\2\u0118T\3\2\2\2\u0119\u011a\7.\2\2\u011aV\3\2\2\2\u011b")
        buf.write("\u011c\7\f\2\2\u011cX\3\2\2\2\u011d\u0121\t\3\2\2\u011e")
        buf.write("\u0120\t\4\2\2\u011f\u011e\3\2\2\2\u0120\u0123\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122Z\3\2\2")
        buf.write("\2\u0123\u0121\3\2\2\2\u0124\u012a\5]/\2\u0125\u012b\5")
        buf.write("_\60\2\u0126\u0128\5_\60\2\u0127\u0126\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\5a\61\2\u012a")
        buf.write("\u0125\3\2\2\2\u012a\u0127\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\\\3\2\2\2\u012c\u012e\t\5\2\2\u012d\u012c\3\2\2")
        buf.write("\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130^\3\2\2\2\u0131\u0135\7\60\2\2\u0132\u0134")
        buf.write("\t\5\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136`\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u013a\t\6\2\2\u0139\u013b\t\7\2\2")
        buf.write("\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3")
        buf.write("\2\2\2\u013c\u013e\t\5\2\2\u013d\u013c\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("b\3\2\2\2\u0141\u0148\7$\2\2\u0142\u0147\n\b\2\2\u0143")
        buf.write("\u0147\5e\63\2\u0144\u0145\7)\2\2\u0145\u0147\7$\2\2\u0146")
        buf.write("\u0142\3\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c")
        buf.write("\7$\2\2\u014c\u014d\b\62\3\2\u014dd\3\2\2\2\u014e\u014f")
        buf.write("\7^\2\2\u014f\u0150\t\t\2\2\u0150f\3\2\2\2\u0151\u0153")
        buf.write("\t\n\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\b\64\2\2\u0157h\3\2\2\2\u0158\u015f\7$\2")
        buf.write("\2\u0159\u015e\n\b\2\2\u015a\u015e\5e\63\2\u015b\u015c")
        buf.write("\7)\2\2\u015c\u015e\7$\2\2\u015d\u0159\3\2\2\2\u015d\u015a")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0163\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0162\u0164\7\2\2\3\u0163\u0162\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166")
        buf.write("\b\65\4\2\u0166j\3\2\2\2\u0167\u016e\7$\2\2\u0168\u016d")
        buf.write("\n\b\2\2\u0169\u016d\5e\63\2\u016a\u016b\7)\2\2\u016b")
        buf.write("\u016d\7$\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0171\u0172\7^\2\2\u0172\u0173\n\t\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0175\b\66\5\2\u0175l\3\2\2\2\u0176")
        buf.write("\u0177\13\2\2\2\u0177\u0178\b\67\6\2\u0178n\3\2\2\2\23")
        buf.write("\2u\u0121\u0127\u012a\u012f\u0135\u013a\u013f\u0146\u0148")
        buf.write("\u0154\u015d\u015f\u0163\u016c\u016e\7\b\2\2\3\62\2\3")
        buf.write("\65\3\3\66\4\3\67\5")
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
    COMMA = 42
    NEWLINE = 43
    IDENTIFIER = 44
    FLOATLIT = 45
    STRINGLIT = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_TOKEN = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
            "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NEQ", 
            "LS", "LSE", "GR", "GRE", "CAT", "COM", "LB", "RB", "LSB", "RSB", 
            "COMMA", "NEWLINE", "IDENTIFIER", "FLOATLIT", "STRINGLIT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "LINE_COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQ", "ASSIGN", "NEQ", "LS", "LSE", "GR", "GRE", "CAT", 
                  "COM", "LB", "RB", "LSB", "RSB", "COMMA", "NEWLINE", "IDENTIFIER", 
                  "FLOATLIT", "INTPART", "DECPART", "EXPPART", "STRINGLIT", 
                  "ESCAPE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
            actions[48] = self.STRINGLIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:]
            	index = 0
            	for i in self.text:
            		if i == '\\': break
            		index += 1
            	raise IllegalEscape(self.text[:index + 2])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


