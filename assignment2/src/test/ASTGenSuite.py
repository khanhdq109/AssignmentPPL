import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """var str <- "Hello world!"
        """
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test_3(self):
        input = """func main() begin
            number a
            if (5 < 2) a <- 1
            elif (not true) a <- 2
            elif ("h" == "6") a <- 3
            end
        """
        expect = None
        self.assertTrue(TestAST.test(input, expect, 303))