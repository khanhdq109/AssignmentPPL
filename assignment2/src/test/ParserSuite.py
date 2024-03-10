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
        
    def test_21(self):
        input = """func greet() return "Hello, World!"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = """func main() begin
            var i <- 0
            for i until i < 3 by 1
                for j until j < 3 by 1
                    writeNumber(i * j)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
        input = """func main() begin
            var x <- 1
            var y <- 2
            var z <- 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
        input = """string message <- "This is a string with newline: \\n and tab: \\t"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = """func add(number a, number b) begin
            return a + b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26(self):
        input = """func complexFunc(number a, string b, bool c) return a * 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_27(self):
        input = """func main() begin
            if (x > 0)
                if (x < 10)
                    x <- x + 5
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_28(self):
        input = """func main() begin
            number arr[3] <- [1 + 2, 2 * 3, 3 / 2]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29(self):
        input = """func noBlockFunc() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30(self):
        input = """func printArray(number arr[5]) begin
            for i until i < 5 by 1
                writeNumber(arr[i])
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_31(self):
        input = """func calculateArea(number radius) begin
            return 3.14 * radius * radius
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        
    def test_32(self):
        input = """func printName(string name) begin
            writeString(name)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33(self):
        input = """func main() begin
            string myName <- "John"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_34(self):
        input = """func greetPerson(string name) begin
            writeString("Hello, ", name, "!")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = """func main() begin
            bool isTrue <- true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36(self):
        input = """func processValue(bool flag) begin
            if flag
                return 1
            else
                return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37(self):
        input = """func main() begin
            number result <- processValue(true)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38(self):
        input = """func greetPerson(string name, number age) begin
            writeString("Hello, ", name, "! You are ", age, " years old.")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39(self):
        input = """func main() begin
            greetPerson("Alice", 25)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        input = """func addNumbers(number a, number b) begin
            return a + b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test_41(self):
        input = """func main() begin
            number x <- 1
            number y <- 2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42(self):
        input = """func calculateProduct(number a, number b) begin
            return a * b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43(self):
        input = """func main() begin
            string name <- "Alice"
            number age <- 30
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
        input = """func greetPerson(string name, number age) begin
            ##writeString("Hello, ", name, "! You are ", age, " years old.")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input = """func processValue(bool flag, number data) begin
            if flag
                return data
            else
                return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46(self):
        input = """func main() begin
            number result <- processValue(true, 42)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
        input = """func printMessage(string message, number value) begin
            writeString(message, ": ", value)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self):
        input = """func main() begin
            printMessage("The answer is", 42)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
        input = """func addNumbers(number a, number b, number c) begin
            return a + b + c
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input = """func main() begin
            number result <- addNumbers(1, 2, 3)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
        
    def test_51(self):
        input = """
        func factorial(number n)
            begin
                if n <= 1
                    return 1
                else
                    return n * factorial(n - 1)
            end
            
        func main()
            begin
                var num <- readNumber()
                writeString("Factorial of ", num, " is ", factorial(num))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52(self):
        input = """
        
        
        func fibonacci(number n)
        
        
            begin
            
            
                if n <= 1
                    return n
                else
                    return fibonacci(n - 1) + fibonacci(n - 2)
            end
        func main()
            begin
                var num <- readNumber()
                writeString("Fibonacci at position ", num, " is ", fibonacci(num))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
        
    def test_53(self):
        input = """var str <- "Hello world!"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54(self):
        input = """
        func sumNumbers(number n)
            begin
                if n <= 1
                begin
                    return 1
                end
                else
                begin
                    return n + sumNumbers(n - 1)
                end
            end
            
        func main()
            begin
                var result <- sumNumbers(5)
                writeString("Sum of numbers: ", result)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """
        func printPattern(number n)
            begin
                for i until i <= n by 1
                begin
                    for j until j <= i by 1
                    begin
                        writeNumber(j)
                    end
                    writeString("")
                end
            end
            
        func main()
            begin
                printPattern(4)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input = """
        func fibonacci(number n)
            begin
                if n <= 1
                begin
                    return n
                end
                else
                begin
                    return fibonacci(n - 1) + fibonacci(n - 2)
                end
            end
            
        func main()
            begin
                var result <- fibonacci(6)
                writeString("Fibonacci at position 6: ", result)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_57(self):
        input = """
        func isEven(number x)
            begin
                return x % 2 = 0
            end
            
        func main()
            begin
                var num <- 8
                if isEven(num)
                begin
                    writeString("Number is even.")
                end
                else
                begin
                    writeString("Number is odd.")
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
        
    def test_58(self):
        input = """
        func power(number base, number exponent)
        begin
            var result <- 1
            for i until i <= exponent by 1
            begin
                result <- result * base
            end
            return result
        end
        func main()
        begin
            var x <- 2
            var y <- 3
            var result <- power(x, y)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input = """
        func calculateAverage(number numbers[5])
        begin
            var sum <- 0
            for i until i < 5 by 1
            begin
                sum <- sum + numbers[i]
            end
            return sum / 5
        end
        func main()
        begin
            string nums[5] <- [10, 15, 20, 25, 30]
            var avg <- calculateAverage(nums)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """
        func printPattern(number n)
        begin
            for i until i <= n by 1
            begin
                for j until j <= i by 1
                    write("*")
                write()
            end
        end
        func main()
        begin
            var num <- 4
            printPattern(num)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input = """
        func isEven(number num)
        begin
            if num % 2 = 0
                return true
            else
                return false
        end
        func main()
        begin
            var x <- 7
            var result <- isEven(x)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input = """
        func findSum(number a, number b)
        begin
            return a + b
        end
        func main()
        begin
            var num1 <- 10
            var num2 <- 20
            var total <- findSum(num1, num2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test_63(self):
        input = """
        func multiplyByTwo(number x)
        begin
            return x * 2
        end
        
        
        func subtract(number a, number b)
        begin
            return a - b
        end
        
        
        
        
        func calculateSquare(number num)
        begin
            return num * num
        end
        func main()
        begin
            var value <- 5
            var twice <- multiplyByTwo(value)
            var result <- subtract(calculateSquare(twice), 10)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """
        func sumNumbers(number numbers[5])
        begin
            var sum <- 0
            for i until i < 5 by 1
            begin
                sum <- sum + numbers[i]
            end
            return sum
        end
        func findAverage(number nums[5])
        begin
            return sumNumbers(nums) / 5
        end
        func calculateFactorial(number n)
        begin
            if n <= 1
                return 1
            else
                return n * calculateFactorial(n - 1)
        end
        func main()
        begin
            number arr[5] <- [1, 2, 3, 4, 5]
            var avg <- findAverage(arr)
            var fact <- calculateFactorial(avg)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = """
        func powerOfTwo(number exp)
        begin
            return 2 * exp
        end
        
        func isOdd(number num)
        begin
            if num % 2 = 1
                return true
            else
                return false
        end
        func main()
        begin
            var x <- 3
            var result <- powerOfTwo(x)
            var odd <- isOdd(result)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = """
        func findMax(number arr[5])
        begin
            var max <- arr[0]
            for i until i < 5 by 1
            begin
                if arr[i] > max
                    max <- arr[i]
            end
            return max
        end
        func findMin(number nums[5])
        begin
            var min <- nums[0]
            for i until i < 5 by 1
            begin
                if nums[i] < min
                    min <- nums[i]
            end
            return min
        end
        func main()
        begin
            number numbers[5] <- [10, 5, 8, 15, 3]
            var maxVal <- findMax(numbers)
            var minVal <- findMin(numbers)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
        input = """
        func generateFibonacci(number n)
        begin
            number fibo[50]
            fibo[0] <- 0
            fibo[1] <- 1
            for i until i < n by 1
            begin
                fibo[i + 1] <- fibo[i] + fibo[i - 1]
            end
            return fibo
        end
        func main()
        begin
            var count <- 10
            var fibonacciSeries <- generateFibonacci(count)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input = """
        func multiplyByThree(number x)
        begin
            return x * 3
        end

        func addTwoNumbers(number a, number b)
        begin
            return a + b
        end

        func calculateCube(number num)
        begin
            return num * num * num
        end
        
        func main()
        begin
            var value <- 7
            var triple <- multiplyByThree(value)
            var sumResult <- addTwoNumbers(calculateCube(triple), 20)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69(self):
        input = """
        func reverseArray(number arr[5])
        begin
            number reversed[5]
            for i until i < 5 by 1
            begin
                reversed[i] <- arr[4 - i]
            end
            return reversed
        end

        func findMedian(number nums[5])
        begin
            var sorted <- sortArray(nums)
            return sorted[2]
        end

        func sortArray(number arr[5])
        begin
            number sorted[5]
            sorted <- arr
            for i until i < 5 by 1
            begin
                for j until j < 5 by 1
                begin
                    if sorted[i] < sorted[j]
                        swap(sorted[i], sorted[j])
                end
            end
            return sorted
        end
        
        func main()
        begin
            number data[5] <- [12, 5, 8, 15, 3]
            var reversedArray <- reverseArray(data)
            var median <- findMedian(reversedArray)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = """
        func countVowels(string text)
        begin
            var vowels <- 0
            var i <- 0
            for i until i < length(text) by 1
            begin
                if isVowel(text[i])
                    vowels <- vowels + 1
            end
            return vowels
        end

        func isVowel(string ch)
        begin
            if ch = 5 
                return true
            else
                return false
        end
        
        func main()
        begin
            var sentence <- "hello, world!"
            var numVowels <- countVowels(sentence)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = """
        func findSquareRoot(number num)
        begin
            return num * 0.5
        end

        func isPerfectSquare(number n)
        begin
            var root <- findSquareRoot(n)
            return root * root = n
        end

        func main()
        begin
            number value <- 25
            var result <- isPerfectSquare(value)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input = """
        func generateMultiples(number base, number count)
        begin
            number multiples[10]
            for i until i < 10 by 1
            begin
                multiples[i] <- base * (i + 1)
            end
            return multiples
        end

        func main()
        begin
            var startingValue <- 5
            var numMultiples <- 10
            var resultMultiples <- generateMultiples(startingValue, numMultiples)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input = """
        func findAverage(number nums[5])
        begin
            var sum <- 0
            for i until i < 5 by 1
            begin
                sum <- sum + nums[i]
            end
            return sum / 5
        end

        func isAboveAverage(number value, number nums[5])
        begin
            var average <- findAverage(nums)
            return value > average
        end

        func main()
        begin
            number data[5] <- [10, 15, 8, 12, 7]
            var targetValue <- 14
            var aboveAvg <- isAboveAverage(targetValue, data)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """
        func calculateArea(number radius)
        begin
            return 3.14 * radius * radius
        end

        func calculateVolume(number radius, number height)
        begin
            return calculateArea(radius) * height
        end

        func main()
        begin
            number r <- 5
            number h <- 10
            var area <- calculateArea(r)
            var volume <- calculateVolume(r, h)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = """
        func findGCD(number a, number b)
        begin
            begin
                var temp <- b
                b <- a % b
                a <- temp
            end
            return a
        end

        func findLCM(number a, number b)
        begin
            return (a * b) / findGCD(a, b)
        end

        func main()
        begin
            number num1 <- 15
            number num2 <- 25
            var gcd <- findGCD(num1, num2)
            var lcm <- findLCM(num1, num2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = """
        func calculatePower(number base, number exponent)
        begin
            var result <- 1
            for i until i <= exponent by 1
            begin
                result <- result * base
            end
            return result
        end

        func main()
        begin
            number x <- 2
            number exp <- 5
            var powerResult <- calculatePower(x, exp)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = """
        func reverseString(string text)
        begin
            var reversed <- ""
            var i <- length(text) - 1
            begin
                reversed <- reversed + text[i]
                i <- i - 1
            end
            return reversed
        end 
        func main() begin
            var original <- "hello"
            var reversedStr <- reverseString(original)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input = """
        func findSum(number nums[5])
        begin
            var sum <- 0
            for i until i < 5 by 1
            begin
                sum <- sum + nums[i]
            end
            return sum
        end

        func findProduct(number nums[5])
        begin
            var product <- 1
            for i until i < 5 by 1
            begin
                product <- product * nums[i]
            end
            return product
        end

        func main()
        begin
            number arr[5] <- [1, 2, 3, 4, 5]
            var sumResult <- findSum(arr)
            var productResult <- findProduct(arr)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79(self):
        input = """
        func findPrimeFactors(number num)
        begin
            number factors[50]
            var count <- 0
            for i until i <= num by 1
            begin
                begin
                    factors[count] <- i
                    count <- count + 1
                    num <- num / i
                end
            end
            return factors
        end

        func main()
        begin
            number value <- 24
            var primeFactors <- findPrimeFactors(value)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input = """
        func generateRandomNumbers(number n)
        begin
            number randomNums[50]
            for i until i < n by 1
            begin
                randomNums[i] <- random()
            end
            return randomNums
        end

        func main()
        begin
            var count <- 10
            var randomList <- generateRandomNumbers(count)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81(self):
        input = """
        func findDifference(number a, number b)
        begin
            if a > b
                return a - b
            else
                return b - a
        end

        func main()
        begin
            number x <- 7
            number y <- 12
            var diffResult <- findDifference(x, y)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input = """
        func isPalindrome(string text)
        begin
            var reversed <- ""
            var i <- length(text) - 1
            begin
                reversed <- reversed + text[i]
                i <- i - 1
            end
            return text = reversed
        end

        func main()
        begin
            var word <- "radar"
            var palindrome <- isPalindrome(word)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
        input = """
        func square(number x)
        begin
            return x * x
        end

        func main()
        begin
            var value <- 5
            var result <- square(value)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """
        func absoluteValue(number x)
        begin
            if x >= 0
                return x
            else
                return -x
        end

        func main()
        begin
            var num <- -10
            var absValue <- absoluteValue(num)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = """
        func isEven(number x)
        begin
            return x % 2 = 0
        end

        func main()
        begin
            var numbers <- 7
            var checkEven <- isEven(numbers)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input = """
        func greet(string name)
        begin
            writeString("Hello, ", name, "!")
        end

        func main()
        begin
            var userName <- "Alice"
            greet(userName)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = """
        func powerOfThree(number exp)
        begin
            return 3 * exp
        end

        func main()
        begin
            var exponent <- 4
            var result <- powerOfThree(exponent)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = """
        func isNegative(number x)
        begin
            return x < 0
        end

        func main()
        begin
            var num <- -15
            var checkNegative <- isNegative(num)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """
        func multiplyThreeNumbers(number a, number b, number c)
        begin
            return a * b * c
        end

        func main()
        begin
            var x <- 2
            var y <- 3
            var z <- 5
            var result <- multiplyThreeNumbers(x, y, z)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """
        
        
        func isVowel(string ch)
        begin 
            return ch = "a"
        end

        func main()
        begin
            var letter <- "o"
            var checkVowel <- isVowel(letter)
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = """
        func main()
        begin
            var x <- 5
            var y <- 10
            var sum <- x + y
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """
        func main()
        begin
            var name <- "John"
            var age <- 25
            var message <- "Hello, " + name + "! You are " + age + " years old."
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = """
        func main()
        begin
            var isTrue <- true
            var isFalse <- false
            var result <- isTrue and isFalse or not isFalse
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """
        func main()
        begin
            number numberArray[5] <- [1, 2, 3, 4, 5]
            var sum <- 0
            for i until i < 5 by 1
                sum <- sum + numberArray[i]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input = """
        
        
        func main()
        begin
            var x <- 8
            var y <- 3
            var quotient <- x / y
            var remainder <- x % y
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = """
        func main()
        begin
            var count <- 0
                count <- count + 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = """
        func main()
        begin
            var i <- 0
            for i until i < 10 by 2
                writeNumber(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """
        func main()
        begin
            var num <- readNumber()
            if num > 0
                writeString("Positive")
            else
                writeString("Non-positive")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """
        func main()
        begin
            var grade <- readNumber()
            if grade >= 90
                writeString("A")
            elif grade >= 80
                writeString("B")
            elif grade >= 70
                writeString("C")
            else
                writeString("Fail")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input = """
        func main()
        begin
            var i <- 1
            begin
                writeNumber(i)
                i <- i + 1
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
