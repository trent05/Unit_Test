import unittest

def fizzbuzz_test(f):
    if f(3) == "fizz" and f(5) == "buzz" and f(15) == "fizzbuzz":
        print("Success!")
    else:
        print("Nope. Try again.")

def fizzbuzz(n):
    ret = ""
    if not (n%3):
        ret += "fizz"
    if not (n%5):
        ret += "buzz"
    return ret or str(n)

import unittest

class ExampleTests(unittest.TestCase):
    def fizzbuzz_goodtest(f):
        output = []
        for n in range(100):
            output.append(str(f(n) + "\n"))

        expected = fizzbuzz
        i = 0
        for line in expected:
            if line == output[i]:
                print("Success!")
                i += 1
            else:
                print("Nope. Try Again.")
if __name__ == "__main__":
    unittest.main()



