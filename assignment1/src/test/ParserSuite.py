import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """number a[5] <- [1, 2, 3, 4, 5]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test_2(self):
        input = """number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        
    def test_3(self):
        input = """func main() begin
end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))