import unittest
from neuronValue import Value




       
    

class TestValue(unittest.TestCase):

    def test_withValues_isCommutative(self):

        a = Value(1.0)
        b = Value(2.0)

        add = a + b
        add2 = b + a
        
        self.assertEqual(add.data, add2.data)
        
    
    def test_withMultiplication_worksCommutativly(self):
        a = Value(2.0)
        b = Value(2.0)
        expected = 4.0
        right_multiply = (a*b).data
        left_multiply = (b*a).data

        self.assertEqual(right_multiply, expected)
        self.assertEqual(left_multiply, expected)

    def test_user_level_change(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

