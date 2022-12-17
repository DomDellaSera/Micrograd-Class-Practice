import unittest
from neuronValue import Value




       
    

class TestValue(unittest.TestCase):

    def test_withValues_isCommutative(self):


        a = Value(1.0)
        b = Value(2.0)

        left_add = a + b
        right_add = b + a
        
        #Then
        self.assertTrue(left_add == right_add)
        
    
    def test_withMultiplication_worksCommutativly(self):
        #Given
        a = Value(2.0)
        b = Value(2.0)
        expected = Value(4.0)

        #When
        left_multiply = (a*b)
        right_multiply = (b*a)

        #Then
        self.assertTrue(right_multiply == expected)
        self.assertTrue(left_multiply == expected)

    def test_pow_computes(self):
        expected = Value(2**24)
        result = Value(2).__pow__(24)

        self.assertTrue(result, expected)



if __name__ == '__main__':
    unittest.main(verbosity=2)

