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
        
    def test_4(self):
        input = """number a[5] <- [1, 2, 3, 4, 5]
number b[2, 3] <-  [[1, 2], [4, 5], [3, 5]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        
    def test_5(self):
        input = """func main() begin
            result <- s1 ... s2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        
    def test_6(self):
        input = """func main() begin
            result <- s1 = s2
            result <- s1 == s2
            result <- s1 != s2
            result <- s1 < s2
            result <- s1 > s2
            result <- s1 <= s2
            result <- s1 >= s2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        
    def test_7(self):
        input = """func main() begin
            result <- s1 + s2
            result <- s1 - s2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
        
    def test_8(self):
        input = """func main() begin
            result <- s1 and s2
            result <- s1 or s2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        
    def test_9(self):
        input = """func main() begin
            result <- s1 * s2
            result <- s1 / s2
            result <- s1 % s2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        
    def test_10(self):
        input = """func main() begin
            result <- not a
            result <- -b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
        
    def test_11(self):
        input = """func main() begin
            a[3 + foo(2)] <- a[b[2, 3]] + 4
            foo(5, 7, sum("non"))[7] <- 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
    def test_12(self):
        input = """func foo(number a[5], string b)
        begin
            ##var i <- 0
            ##for i until i >= 5 by 1
            ##begin
                ##a[i] <- i * i + 5
            ##end
            ##return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))