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
            var i <- 0
            for i until i >= 5 by 1
            begin
                a[i] <- i * i + 5
            end
            for i until i <=9 by 4
                var i <- 0
            return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        
    def test_13(self):
        input = """func foo(number a[5], string b)
        begin
            if i < 5
                return -1 
            elif i >= 9
                continue
            elif i == 9
                break
            else
                return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
    def test_14(self):
        input = """func foo(number a[5], string b) return 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
        
    def test_15(self):
        input = """func main() begin
            aPI <- 3.14
            l[3] <- value * aPi
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test_16(self):
        input = """func foo(number a[5], string b)
        
        begin
            if exp <= 9
                return
            elif 5 >=3
                break
            elif 8
                continue
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        
    def test_16(self):
        input = """func main() begin
            var i <- 0
            for i until i >= 10 by 1
                writeNumbe(i)
                
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        
    def test_17(self):
        input = """func foo(number a[9], bool b)
        begin
            number r
            number s
            r <- 2.0
            number a[5]
            number b[5]
            s <- r * r * 3.14
            a[0] <- s
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    def test_18(self):
        input = """
        func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisor(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test_19(self):
        input = """
        func main()
            begin
                number x <- readNumber()
                if (isPrime(x)) writeString("Yes")
                else writeString("No")
            end
            
            
            
        func isPrime(number x)
            begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin 
                    if (x % i = 0) return false
                end
                return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_20(self):
        input = """
        func giaithua(number n)
        begin 
            if n <= 1 return 1
            return n * giaithua(n - 1)
        end
        func main()
        begin
            n <- readNumber()
            writeString("n! = ", giaithua(n))
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 20))