import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Characters set
    def test_1(self):
        input = "   "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))
        
    def test_2(self):
        input = "\b \b \f"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))
        
    def test_3(self):
        input = "       "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))
        
    def test_4(self):
        input = "   \t"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))
        
    def test_5(self):
        input = "\f\f     \t    \b"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))
    
    # Program comment
    def test_6(self):
        input = "##"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))
    
    def test_7(self):
        input = "##################"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))
        
    def test_8(self):
        input = "## This is a single comment."
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))
        
    def test_9(self):
        input = "## Who are you? \t\f"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))
        
    def test_10(self):
        input = "## Hello \b\b\b\b"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))
    
    # Identifiers
    def test_11(self):
        input = "khanh0109"
        expect = "khanh0109,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))
        
    def test_12(self):
        input = "Glf_"
        expect = "Glf_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))
        
    def test_13(self):
        input = "fFF1122"
        expect = "fFF1122,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))
        
    def test_14(self):
        input = "p_"
        expect = "p_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))
        
    def test_15(self):
        input = "zas_______9_______"
        expect = "zas_______9_______,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))
        
    def test_16(self):
        input = ""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
        
    def test_17(self):
        input = "1B"
        expect = "1,B,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))
        
    def test_18(self):
        input = "or"
        expect = "or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))
        
    def test_19(self):
        input = "K92342 reds34234 t_32"
        expect = "K92342,reds34234,t_32,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))
        
    def test_20(self):
        input = "Zvaef@9fvi_82"
        expect = "Zvaef,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 120))
    
    # Keywords
    def test_21(self):
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))
        
    def test_22(self):
        input = "var"
        expect = "var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))
        
    def test_23(self):
        input = "or"
        expect = "or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_24(self):
        input = "elif break"
        expect = "elif,break,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))
        
    def test_25(self):
        input = "string"
        expect = "string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))
        
    def test_26(self):
        input = "strinG"
        expect = "strinG,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))
        
    def test_27(self):
        input = "if else elif"
        expect = "if,else,elif,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))
        
    def test_28(self):
        input = "brek"
        expect = "brek,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))
        
    def test_29(self):
        input = "by"
        expect = "by,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))
        
    def test_30(self):
        input = "continue      not if dynamic"
        expect = "continue,not,if,dynamic,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))
    
    # Operators
    def test_31(self):
        input = "+"
        expect = "+,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))
        
    def test_32(self):
        input = "+ - * / %    not and   or"
        expect = "+,-,*,/,%,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))
        
    def test_33(self):
        input = "<<=>"
        expect = "<,<=,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))
        
    def test_34(self):
        input = "==="
        expect = "==,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))
        
    def test_35(self):
        input = "... <-"
        expect = "...,<-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))
    
    # Separators
    def test_36(self):
        input = "()"
        expect = "(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))
        
    def test_37(self):
        input = "[]"
        expect = "[,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))
        
    def test_38(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))
        
    def test_39(self):
        input = "( \n [[[ \n ] )"
        expect = "(,\n,[,[,[,\n,],),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))
        
    def test_40(self):
        input = "## Hello \n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))
        
    # Number
    def test_41(self):
        input = "0"
        expect = "0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))
        
    def test_42(self):
        input = "199"
        expect = "199,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))
        
    def test_43(self):
        input = "12."
        expect = "12.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))
        
    def test_44(self):
        input = "12.3"
        expect = "12.3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))
        
    def test_45(self):
        input = "12.3e3"
        expect = "12.3e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))
        
    def test_46(self):
        input = "12e3"
        expect = "12e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 146))
        
    def test_47(self):
        input = "12.3e-30"
        expect = "12.3e-30,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))
        
    def test_48(self):
        input = "0000124.6e+1"
        expect = "0000124.6e+1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))
        
    def test_49(self):
        input = "19.e72"
        expect = "19.e72,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))
        
    def test_50(self):
        input = "2e+"
        expect = "2,e,+,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))
        
    # String
    def test_51(self):
        input = """This is a string"""
        expect = "This is a string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))
        
    def test_52(self):
        input = """"""
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))
        
    def test_53(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))
        
    def test_54(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))
        
    def test_55(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))
        
    def test_56(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))
        
    def test_57(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))
        
    def test_58(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))
        
    def test_59(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))
        
    def test_60(self):
        input = "\n\n"
        expect = "\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))
    
    # Combine