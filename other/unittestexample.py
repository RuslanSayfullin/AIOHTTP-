import unittest

def add(a, b):
    return a+b

class TsetAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def tes_add_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(sesult, 10)

    def test_add_zero(self):
        result = add(10, 0)
        self.assertEqual(result, 10)

if __name__=='__main__':
    unittest.main()


