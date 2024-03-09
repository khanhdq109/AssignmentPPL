# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u0175\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\5\3]\n\3\3\4\3\4\3\4\3\4\5\4c\n\4\3\5\3\5\5\5g\n")
        buf.write("\5\3\6\3\6\3\6\3\6\5\6m\n\6\3\7\3\7\5\7q\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\bx\n\b\3\t\3\t\5\t|\n\t\3\n\3\n\3\n\5\n\u0081")
        buf.write("\n\n\3\13\3\13\5\13\u0085\n\13\3\f\3\f\3\f\3\f\5\f\u008b")
        buf.write("\n\f\3\r\3\r\5\r\u008f\n\r\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u0096\n\16\3\17\3\17\3\17\5\17\u009b\n\17\3\17\3\17")
        buf.write("\3\20\3\20\5\20\u00a1\n\20\3\20\3\20\3\20\5\20\u00a6\n")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u00ac\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00b5\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00bd\n\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00c7\n\23\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00d6")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\7\27\u00e6\n\27\f\27\16\27\u00e9")
        buf.write("\13\27\3\27\3\27\3\27\3\27\3\27\5\27\u00f0\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\5\33\u0101\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u0112\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0119\n")
        buf.write("\37\3 \3 \3 \3 \3 \3 \7 \u0121\n \f \16 \u0124\13 \3!")
        buf.write("\3!\3!\3!\3!\3!\7!\u012c\n!\f!\16!\u012f\13!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u0137\n\"\f\"\16\"\u013a\13\"\3#\3")
        buf.write("#\3#\5#\u013f\n#\3$\3$\3$\5$\u0144\n$\3%\3%\5%\u0148\n")
        buf.write("%\3%\3%\3%\3%\3%\5%\u014f\n%\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\5&\u015b\n&\3\'\3\'\3(\3(\3(\3(\3)\3)\3*\3*\3*\5")
        buf.write("*\u0168\n*\3*\3*\3*\3*\5*\u016e\n*\3+\3+\3+\3+\3+\3+\2")
        buf.write("\5>@B,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRT\2\b\5\2\37\37!%\'\'\3\2\30")
        buf.write("\31\3\2\32\33\3\2\34\36\3\2\4\5\3\2\6\b\2\u017c\2V\3\2")
        buf.write("\2\2\4\\\3\2\2\2\6b\3\2\2\2\bf\3\2\2\2\nl\3\2\2\2\fp\3")
        buf.write("\2\2\2\16w\3\2\2\2\20{\3\2\2\2\22\u0080\3\2\2\2\24\u0084")
        buf.write("\3\2\2\2\26\u008a\3\2\2\2\30\u008e\3\2\2\2\32\u0095\3")
        buf.write("\2\2\2\34\u009a\3\2\2\2\36\u00ab\3\2\2\2 \u00ad\3\2\2")
        buf.write("\2\"\u00b6\3\2\2\2$\u00be\3\2\2\2&\u00c8\3\2\2\2(\u00d5")
        buf.write("\3\2\2\2*\u00d7\3\2\2\2,\u00db\3\2\2\2.\u00f1\3\2\2\2")
        buf.write("\60\u00fa\3\2\2\2\62\u00fc\3\2\2\2\64\u00fe\3\2\2\2\66")
        buf.write("\u0102\3\2\2\28\u0107\3\2\2\2:\u0111\3\2\2\2<\u0118\3")
        buf.write("\2\2\2>\u011a\3\2\2\2@\u0125\3\2\2\2B\u0130\3\2\2\2D\u013e")
        buf.write("\3\2\2\2F\u0143\3\2\2\2H\u014e\3\2\2\2J\u015a\3\2\2\2")
        buf.write("L\u015c\3\2\2\2N\u015e\3\2\2\2P\u0162\3\2\2\2R\u016d\3")
        buf.write("\2\2\2T\u016f\3\2\2\2VW\5\20\t\2WX\5\6\4\2XY\7\2\2\3Y")
        buf.write("\3\3\2\2\2Z]\5\6\4\2[]\3\2\2\2\\Z\3\2\2\2\\[\3\2\2\2]")
        buf.write("\5\3\2\2\2^_\5\34\17\2_`\5\6\4\2`c\3\2\2\2ac\5\34\17\2")
        buf.write("b^\3\2\2\2ba\3\2\2\2c\7\3\2\2\2dg\5\n\6\2eg\3\2\2\2fd")
        buf.write("\3\2\2\2fe\3\2\2\2g\t\3\2\2\2hi\7/\2\2ij\7,\2\2jm\5\n")
        buf.write("\6\2km\7/\2\2lh\3\2\2\2lk\3\2\2\2m\13\3\2\2\2nq\5\16\b")
        buf.write("\2oq\3\2\2\2pn\3\2\2\2po\3\2\2\2q\r\3\2\2\2rs\5\"\22\2")
        buf.write("st\7,\2\2tu\5\16\b\2ux\3\2\2\2vx\5\"\22\2wr\3\2\2\2wv")
        buf.write("\3\2\2\2x\17\3\2\2\2y|\5\22\n\2z|\3\2\2\2{y\3\2\2\2{z")
        buf.write("\3\2\2\2|\21\3\2\2\2}~\7-\2\2~\u0081\5\22\n\2\177\u0081")
        buf.write("\7-\2\2\u0080}\3\2\2\2\u0080\177\3\2\2\2\u0081\23\3\2")
        buf.write("\2\2\u0082\u0085\5\26\f\2\u0083\u0085\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0083\3\2\2\2\u0085\25\3\2\2\2\u0086\u0087")
        buf.write("\5&\24\2\u0087\u0088\5\26\f\2\u0088\u008b\3\2\2\2\u0089")
        buf.write("\u008b\5&\24\2\u008a\u0086\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\27\3\2\2\2\u008c\u008f\5\32\16\2\u008d\u008f\3")
        buf.write("\2\2\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f\31")
        buf.write("\3\2\2\2\u0090\u0091\5:\36\2\u0091\u0092\7,\2\2\u0092")
        buf.write("\u0093\5\32\16\2\u0093\u0096\3\2\2\2\u0094\u0096\5:\36")
        buf.write("\2\u0095\u0090\3\2\2\2\u0095\u0094\3\2\2\2\u0096\33\3")
        buf.write("\2\2\2\u0097\u009b\5\36\20\2\u0098\u009b\5 \21\2\u0099")
        buf.write("\u009b\5$\23\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\5")
        buf.write("\22\n\2\u009d\35\3\2\2\2\u009e\u00a1\5P)\2\u009f\u00a1")
        buf.write("\7\13\2\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\u00a5\7.\2\2\u00a3\u00a4\7 \2\2\u00a4")
        buf.write("\u00a6\5:\36\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00ac\3\2\2\2\u00a7\u00a8\7\n\2\2\u00a8\u00a9\7")
        buf.write(".\2\2\u00a9\u00aa\7 \2\2\u00aa\u00ac\5:\36\2\u00ab\u00a0")
        buf.write("\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ac\37\3\2\2\2\u00ad\u00ae")
        buf.write("\5P)\2\u00ae\u00af\7.\2\2\u00af\u00b0\7*\2\2\u00b0\u00b1")
        buf.write("\5\n\6\2\u00b1\u00b4\7+\2\2\u00b2\u00b3\7 \2\2\u00b3\u00b5")
        buf.write("\5:\36\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("!\3\2\2\2\u00b6\u00b7\5P)\2\u00b7\u00bc\7.\2\2\u00b8\u00b9")
        buf.write("\7*\2\2\u00b9\u00ba\5\n\6\2\u00ba\u00bb\7+\2\2\u00bb\u00bd")
        buf.write("\3\2\2\2\u00bc\u00b8\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("#\3\2\2\2\u00be\u00bf\7\f\2\2\u00bf\u00c0\7.\2\2\u00c0")
        buf.write("\u00c1\7(\2\2\u00c1\u00c2\5\f\7\2\u00c2\u00c3\7)\2\2\u00c3")
        buf.write("\u00c6\5\20\t\2\u00c4\u00c7\5\64\33\2\u00c5\u00c7\58\35")
        buf.write("\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7%\3\2\2\2\u00c8\u00c9\5(\25\2\u00c9\u00ca")
        buf.write("\5\22\n\2\u00ca\'\3\2\2\2\u00cb\u00d6\5\36\20\2\u00cc")
        buf.write("\u00d6\5 \21\2\u00cd\u00d6\5*\26\2\u00ce\u00d6\5,\27\2")
        buf.write("\u00cf\u00d6\5.\30\2\u00d0\u00d6\5\60\31\2\u00d1\u00d6")
        buf.write("\5\62\32\2\u00d2\u00d6\5\64\33\2\u00d3\u00d6\5\66\34\2")
        buf.write("\u00d4\u00d6\58\35\2\u00d5\u00cb\3\2\2\2\u00d5\u00cc\3")
        buf.write("\2\2\2\u00d5\u00cd\3\2\2\2\u00d5\u00ce\3\2\2\2\u00d5\u00cf")
        buf.write("\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d5")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d6)\3\2\2\2\u00d7\u00d8\5R*\2\u00d8\u00d9\7 \2\2\u00d9")
        buf.write("\u00da\5:\36\2\u00da+\3\2\2\2\u00db\u00dc\7\22\2\2\u00dc")
        buf.write("\u00dd\5:\36\2\u00dd\u00de\5\20\t\2\u00de\u00e7\5(\25")
        buf.write("\2\u00df\u00e0\5\22\n\2\u00e0\u00e1\7\24\2\2\u00e1\u00e2")
        buf.write("\5:\36\2\u00e2\u00e3\5\20\t\2\u00e3\u00e4\5(\25\2\u00e4")
        buf.write("\u00e6\3\2\2\2\u00e5\u00df\3\2\2\2\u00e6\u00e9\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ef\3")
        buf.write("\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\5\22\n\2\u00eb")
        buf.write("\u00ec\7\23\2\2\u00ec\u00ed\5\20\t\2\u00ed\u00ee\5(\25")
        buf.write("\2\u00ee\u00f0\3\2\2\2\u00ef\u00ea\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0-\3\2\2\2\u00f1\u00f2\7\r\2\2\u00f2\u00f3")
        buf.write("\7.\2\2\u00f3\u00f4\7\16\2\2\u00f4\u00f5\5:\36\2\u00f5")
        buf.write("\u00f6\7\17\2\2\u00f6\u00f7\5:\36\2\u00f7\u00f8\5\20\t")
        buf.write("\2\u00f8\u00f9\5(\25\2\u00f9/\3\2\2\2\u00fa\u00fb\7\20")
        buf.write("\2\2\u00fb\61\3\2\2\2\u00fc\u00fd\7\21\2\2\u00fd\63\3")
        buf.write("\2\2\2\u00fe\u0100\7\t\2\2\u00ff\u0101\5:\36\2\u0100\u00ff")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\65\3\2\2\2\u0102\u0103")
        buf.write("\7.\2\2\u0103\u0104\7(\2\2\u0104\u0105\5\30\r\2\u0105")
        buf.write("\u0106\7)\2\2\u0106\67\3\2\2\2\u0107\u0108\7\25\2\2\u0108")
        buf.write("\u0109\5\22\n\2\u0109\u010a\5\24\13\2\u010a\u010b\7\26")
        buf.write("\2\2\u010b9\3\2\2\2\u010c\u010d\5<\37\2\u010d\u010e\7")
        buf.write("&\2\2\u010e\u010f\5<\37\2\u010f\u0112\3\2\2\2\u0110\u0112")
        buf.write("\5<\37\2\u0111\u010c\3\2\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write(";\3\2\2\2\u0113\u0114\5> \2\u0114\u0115\t\2\2\2\u0115")
        buf.write("\u0116\5> \2\u0116\u0119\3\2\2\2\u0117\u0119\5> \2\u0118")
        buf.write("\u0113\3\2\2\2\u0118\u0117\3\2\2\2\u0119=\3\2\2\2\u011a")
        buf.write("\u011b\b \1\2\u011b\u011c\5@!\2\u011c\u0122\3\2\2\2\u011d")
        buf.write("\u011e\f\4\2\2\u011e\u011f\t\3\2\2\u011f\u0121\5@!\2\u0120")
        buf.write("\u011d\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123?\3\2\2\2\u0124\u0122\3\2\2")
        buf.write("\2\u0125\u0126\b!\1\2\u0126\u0127\5B\"\2\u0127\u012d\3")
        buf.write("\2\2\2\u0128\u0129\f\4\2\2\u0129\u012a\t\4\2\2\u012a\u012c")
        buf.write("\5B\"\2\u012b\u0128\3\2\2\2\u012c\u012f\3\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012eA\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u0130\u0131\b\"\1\2\u0131\u0132\5D#\2\u0132")
        buf.write("\u0138\3\2\2\2\u0133\u0134\f\4\2\2\u0134\u0135\t\5\2\2")
        buf.write("\u0135\u0137\5D#\2\u0136\u0133\3\2\2\2\u0137\u013a\3\2")
        buf.write("\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139C\3")
        buf.write("\2\2\2\u013a\u0138\3\2\2\2\u013b\u013c\7\27\2\2\u013c")
        buf.write("\u013f\5D#\2\u013d\u013f\5F$\2\u013e\u013b\3\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013fE\3\2\2\2\u0140\u0141\7\33\2\2\u0141")
        buf.write("\u0144\5F$\2\u0142\u0144\5H%\2\u0143\u0140\3\2\2\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144G\3\2\2\2\u0145\u0148\7.\2\2\u0146")
        buf.write("\u0148\5T+\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\7*\2\2\u014a\u014b\5\32\16")
        buf.write("\2\u014b\u014c\7+\2\2\u014c\u014f\3\2\2\2\u014d\u014f")
        buf.write("\5J&\2\u014e\u0147\3\2\2\2\u014e\u014d\3\2\2\2\u014fI")
        buf.write("\3\2\2\2\u0150\u015b\7.\2\2\u0151\u015b\7/\2\2\u0152\u015b")
        buf.write("\5L\'\2\u0153\u015b\7\60\2\2\u0154\u015b\5N(\2\u0155\u0156")
        buf.write("\7(\2\2\u0156\u0157\5:\36\2\u0157\u0158\7)\2\2\u0158\u015b")
        buf.write("\3\2\2\2\u0159\u015b\5T+\2\u015a\u0150\3\2\2\2\u015a\u0151")
        buf.write("\3\2\2\2\u015a\u0152\3\2\2\2\u015a\u0153\3\2\2\2\u015a")
        buf.write("\u0154\3\2\2\2\u015a\u0155\3\2\2\2\u015a\u0159\3\2\2\2")
        buf.write("\u015bK\3\2\2\2\u015c\u015d\t\6\2\2\u015dM\3\2\2\2\u015e")
        buf.write("\u015f\7*\2\2\u015f\u0160\5\30\r\2\u0160\u0161\7+\2\2")
        buf.write("\u0161O\3\2\2\2\u0162\u0163\t\7\2\2\u0163Q\3\2\2\2\u0164")
        buf.write("\u016e\7.\2\2\u0165\u0168\7.\2\2\u0166\u0168\5T+\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u016a\7*\2\2\u016a\u016b\5\32\16\2\u016b\u016c")
        buf.write("\7+\2\2\u016c\u016e\3\2\2\2\u016d\u0164\3\2\2\2\u016d")
        buf.write("\u0167\3\2\2\2\u016eS\3\2\2\2\u016f\u0170\7.\2\2\u0170")
        buf.write("\u0171\7(\2\2\u0171\u0172\5\30\r\2\u0172\u0173\7)\2\2")
        buf.write("\u0173U\3\2\2\2%\\bflpw{\u0080\u0084\u008a\u008e\u0095")
        buf.write("\u009a\u00a0\u00a5\u00ab\u00b4\u00bc\u00c6\u00d5\u00e7")
        buf.write("\u00ef\u0100\u0111\u0118\u0122\u012d\u0138\u013e\u0143")
        buf.write("\u0147\u014e\u015a\u0167\u016d")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "TRUE", "FALSE", "NUMBER", 
                      "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NEQ", 
                      "LS", "LSE", "GR", "GRE", "CAT", "COM", "LB", "RB", 
                      "LSB", "RSB", "COMMA", "NEWLINE", "IDENTIFIER", "FLOATLIT", 
                      "STRINGLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decllistprime = 2
    RULE_numlist = 3
    RULE_numlistprime = 4
    RULE_paramdecllist = 5
    RULE_paramdecllistprime = 6
    RULE_newlinelist = 7
    RULE_newlinelistprime = 8
    RULE_stmtlist = 9
    RULE_stmtlistprime = 10
    RULE_explist = 11
    RULE_explistprime = 12
    RULE_decl = 13
    RULE_vardecl = 14
    RULE_arrdecl = 15
    RULE_paramdecl = 16
    RULE_funcdecl = 17
    RULE_stmt = 18
    RULE_notnewlinestmt = 19
    RULE_assignstmt = 20
    RULE_ifstmt = 21
    RULE_forstmt = 22
    RULE_breakstmt = 23
    RULE_continuestmt = 24
    RULE_returnstmt = 25
    RULE_callstmt = 26
    RULE_blockstmt = 27
    RULE_exp = 28
    RULE_exp1 = 29
    RULE_exp2 = 30
    RULE_exp3 = 31
    RULE_exp4 = 32
    RULE_exp5 = 33
    RULE_exp6 = 34
    RULE_exp7 = 35
    RULE_exp8 = 36
    RULE_boollit = 37
    RULE_arraylit = 38
    RULE_typ = 39
    RULE_lhs = 40
    RULE_callexp = 41

    ruleNames =  [ "program", "decllist", "decllistprime", "numlist", "numlistprime", 
                   "paramdecllist", "paramdecllistprime", "newlinelist", 
                   "newlinelistprime", "stmtlist", "stmtlistprime", "explist", 
                   "explistprime", "decl", "vardecl", "arrdecl", "paramdecl", 
                   "funcdecl", "stmt", "notnewlinestmt", "assignstmt", "ifstmt", 
                   "forstmt", "breakstmt", "continuestmt", "returnstmt", 
                   "callstmt", "blockstmt", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "boollit", "arraylit", 
                   "typ", "lhs", "callexp" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    TRUE=2
    FALSE=3
    NUMBER=4
    BOOL=5
    STRING=6
    RETURN=7
    VAR=8
    DYNAMIC=9
    FUNC=10
    FOR=11
    UNTIL=12
    BY=13
    BREAK=14
    CONTINUE=15
    IF=16
    ELSE=17
    ELIF=18
    BEGIN=19
    END=20
    NOT=21
    AND=22
    OR=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    EQ=29
    ASSIGN=30
    NEQ=31
    LS=32
    LSE=33
    GR=34
    GRE=35
    CAT=36
    COM=37
    LB=38
    RB=39
    LSB=40
    RSB=41
    COMMA=42
    NEWLINE=43
    IDENTIFIER=44
    FLOATLIT=45
    STRINGLIT=46
    WS=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    ERROR_TOKEN=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def decllistprime(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistprimeContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.newlinelist()
            self.state = 85
            self.decllistprime()
            self.state = 86
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllistprime(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.decllistprime()
                pass
            elif token in [ZCodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllistprime(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllistprime" ):
                return visitor.visitDecllistprime(self)
            else:
                return visitor.visitChildren(self)




    def decllistprime(self):

        localctx = ZCodeParser.DecllistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decllistprime)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.decl()
                self.state = 93
                self.decllistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NumlistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlist" ):
                return visitor.visitNumlist(self)
            else:
                return visitor.visitChildren(self)




    def numlist(self):

        localctx = ZCodeParser.NumlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numlist)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.numlistprime()
                pass
            elif token in [ZCodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(ZCodeParser.FLOATLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NumlistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlistprime" ):
                return visitor.visitNumlistprime(self)
            else:
                return visitor.visitChildren(self)




    def numlistprime(self):

        localctx = ZCodeParser.NumlistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_numlistprime)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(ZCodeParser.FLOATLIT)
                self.state = 103
                self.match(ZCodeParser.COMMA)
                self.state = 104
                self.numlistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(ZCodeParser.FLOATLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecllistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdecllistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecllist" ):
                return visitor.visitParamdecllist(self)
            else:
                return visitor.visitChildren(self)




    def paramdecllist(self):

        localctx = ZCodeParser.ParamdecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramdecllist)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.paramdecllistprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdecllistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramdecllistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdecllistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecllistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecllistprime" ):
                return visitor.visitParamdecllistprime(self)
            else:
                return visitor.visitChildren(self)




    def paramdecllistprime(self):

        localctx = ZCodeParser.ParamdecllistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramdecllistprime)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.paramdecl()
                self.state = 113
                self.match(ZCodeParser.COMMA)
                self.state = 114
                self.paramdecllistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.paramdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_newlinelist)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.newlinelistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newlinelistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelistprime" ):
                return visitor.visitNewlinelistprime(self)
            else:
                return visitor.visitChildren(self)




    def newlinelistprime(self):

        localctx = ZCodeParser.NewlinelistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_newlinelistprime)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(ZCodeParser.NEWLINE)
                self.state = 124
                self.newlinelistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmtlist)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.stmtlistprime()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlistprime" ):
                return visitor.visitStmtlistprime(self)
            else:
                return visitor.visitChildren(self)




    def stmtlistprime(self):

        localctx = ZCodeParser.StmtlistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmtlistprime)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.stmt()
                self.state = 133
                self.stmtlistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = ZCodeParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_explist)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.IDENTIFIER, ZCodeParser.FLOATLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.explistprime()
                pass
            elif token in [ZCodeParser.RB, ZCodeParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def explistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplistprime" ):
                return visitor.visitExplistprime(self)
            else:
                return visitor.visitChildren(self)




    def explistprime(self):

        localctx = ZCodeParser.ExplistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_explistprime)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.exp()
                self.state = 143
                self.match(ZCodeParser.COMMA)
                self.state = 144
                self.explistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistprimeContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def arrdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArrdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 149
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 150
                self.arrdecl()
                pass

            elif la_ == 3:
                self.state = 151
                self.funcdecl()
                pass


            self.state = 154
            self.newlinelistprime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 156
                    self.typ()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 157
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 161
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 162
                    self.exp()


                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(ZCodeParser.VAR)
                self.state = 166
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 167
                self.match(ZCodeParser.ASSIGN)
                self.state = 168
                self.exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def numlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NumlistprimeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdecl" ):
                return visitor.visitArrdecl(self)
            else:
                return visitor.visitChildren(self)




    def arrdecl(self):

        localctx = ZCodeParser.ArrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.typ()
            self.state = 172
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 173
            self.match(ZCodeParser.LSB)
            self.state = 174
            self.numlistprime()
            self.state = 175
            self.match(ZCodeParser.RSB)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 176
                self.match(ZCodeParser.ASSIGN)
                self.state = 177
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def numlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NumlistprimeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.typ()
            self.state = 181
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 182
                self.match(ZCodeParser.LSB)
                self.state = 183
                self.numlistprime()
                self.state = 184
                self.match(ZCodeParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramdecllist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdecllistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.FUNC)
            self.state = 189
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 190
            self.match(ZCodeParser.LB)
            self.state = 191
            self.paramdecllist()
            self.state = 192
            self.match(ZCodeParser.RB)
            self.state = 193
            self.newlinelist()
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 194
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 195
                self.blockstmt()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notnewlinestmt(self):
            return self.getTypedRuleContext(ZCodeParser.NotnewlinestmtContext,0)


        def newlinelistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.notnewlinestmt()
            self.state = 199
            self.newlinelistprime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotnewlinestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def arrdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArrdeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_notnewlinestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotnewlinestmt" ):
                return visitor.visitNotnewlinestmt(self)
            else:
                return visitor.visitChildren(self)




    def notnewlinestmt(self):

        localctx = ZCodeParser.NotnewlinestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_notnewlinestmt)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.arrdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.continuestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 208
                self.returnstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 210
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.lhs()
            self.state = 214
            self.match(ZCodeParser.ASSIGN)
            self.state = 215
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def notnewlinestmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NotnewlinestmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NotnewlinestmtContext,i)


        def newlinelistprime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistprimeContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistprimeContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.IF)
            self.state = 218
            self.exp()
            self.state = 219
            self.newlinelist()
            self.state = 220
            self.notnewlinestmt()
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 221
                    self.newlinelistprime()
                    self.state = 222
                    self.match(ZCodeParser.ELIF)
                    self.state = 223
                    self.exp()
                    self.state = 224
                    self.newlinelist()
                    self.state = 225
                    self.notnewlinestmt() 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 232
                self.newlinelistprime()
                self.state = 233
                self.match(ZCodeParser.ELSE)
                self.state = 234
                self.newlinelist()
                self.state = 235
                self.notnewlinestmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def notnewlinestmt(self):
            return self.getTypedRuleContext(ZCodeParser.NotnewlinestmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.FOR)
            self.state = 240
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 241
            self.match(ZCodeParser.UNTIL)
            self.state = 242
            self.exp()
            self.state = 243
            self.match(ZCodeParser.BY)
            self.state = 244
            self.exp()
            self.state = 245
            self.newlinelist()
            self.state = 246
            self.notnewlinestmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ZCodeParser.RETURN)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.FLOATLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 253
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = ZCodeParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 257
            self.match(ZCodeParser.LB)
            self.state = 258
            self.explist()
            self.state = 259
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newlinelistprime(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistprimeContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ZCodeParser.BEGIN)
            self.state = 262
            self.newlinelistprime()
            self.state = 263
            self.stmtlist()
            self.state = 264
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def CAT(self):
            return self.getToken(ZCodeParser.CAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.exp1()
                self.state = 267
                self.match(ZCodeParser.CAT)
                self.state = 268
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def COM(self):
            return self.getToken(ZCodeParser.COM, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def GR(self):
            return self.getToken(ZCodeParser.GR, 0)

        def LSE(self):
            return self.getToken(ZCodeParser.LSE, 0)

        def GRE(self):
            return self.getToken(ZCodeParser.GRE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.exp2(0)
                self.state = 274
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.LSE) | (1 << ZCodeParser.GR) | (1 << ZCodeParser.GRE) | (1 << ZCodeParser.COM))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 283
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 284
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 285
                    self.exp3(0) 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 294
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 295
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 296
                    self.exp4(0) 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 306
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 307
                    self.exp5() 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp5)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(ZCodeParser.NOT)
                self.state = 314
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.IDENTIFIER, ZCodeParser.FLOATLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp6)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ZCodeParser.SUB)
                self.state = 319
                self.exp6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.IDENTIFIER, ZCodeParser.FLOATLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def explistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistprimeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def callexp(self):
            return self.getTypedRuleContext(ZCodeParser.CallexpContext,0)


        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp7)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 323
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 324
                    self.callexp()
                    pass


                self.state = 327
                self.match(ZCodeParser.LSB)
                self.state = 328
                self.explistprime()
                self.state = 329
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def FLOATLIT(self):
            return self.getToken(ZCodeParser.FLOATLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(ZCodeParser.BoollitContext,0)


        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def callexp(self):
            return self.getTypedRuleContext(ZCodeParser.CallexpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp8)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(ZCodeParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.boollit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.arraylit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 339
                self.match(ZCodeParser.LB)
                self.state = 340
                self.exp()
                self.state = 341
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.callexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boollit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = ZCodeParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ZCodeParser.LSB)
            self.state = 349
            self.explist()
            self.state = 350
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def explistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistprimeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def callexp(self):
            return self.getTypedRuleContext(ZCodeParser.CallexpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_lhs)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 355
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 356
                    self.callexp()
                    pass


                self.state = 359
                self.match(ZCodeParser.LSB)
                self.state = 360
                self.explistprime()
                self.state = 361
                self.match(ZCodeParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_callexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexp" ):
                return visitor.visitCallexp(self)
            else:
                return visitor.visitChildren(self)




    def callexp(self):

        localctx = ZCodeParser.CallexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_callexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 366
            self.match(ZCodeParser.LB)
            self.state = 367
            self.explist()
            self.state = 368
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.exp2_sempred
        self._predicates[31] = self.exp3_sempred
        self._predicates[32] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




