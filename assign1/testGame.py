import unittest

from calculatorGame import *
class testGame(unittest.TestCase):
    def test_multGame_1(self):
        "Test Multiplication Operation"
        self.assertEqual(multGame(2, 5), 10)
        self.assertEqual(multGame(-1, 1), -1)
        self.assertEqual(multGame(-1, -1), 1)
        self.assertEqual(multGame(0, 1), 0)
        self.assertEqual(multGame(1, 0), 0)
        self.assertEqual(multGame(10, 5), 50)
        self.assertEqual(multGame(10, 1), 10)

    def test_divGame_1(self):
        "Test Floor Division Operation"
        self.assertEqual(divGame(2, 5), 0)
        self.assertEqual(divGame(-1, 1), -1)
        self.assertEqual(divGame(-1, -1), 1)
        self.assertEqual(divGame(0, 1), 0)
        self.assertEqual(divGame(1, 1), 1)
        self.assertEqual(divGame(10, 5), 2)
        self.assertEqual(divGame(10, 1), 10)
    
    def test_addGame_1(self):
        "Test Addition Operation"
        self.assertEqual(addGame(2, 5), 7)
        self.assertEqual(addGame(-1, 1), 0)
        self.assertEqual(addGame(-1, -1), -2)
        self.assertEqual(addGame(0, 1), 1)
        self.assertEqual(addGame(1, 0), 1)
        self.assertEqual(addGame(10, 5), 15)
        self.assertEqual(addGame(10, 1), 11)
    
    def test_subGame_1(self):
        "Test Subtraction Operation"
        self.assertEqual(subGame(2, 5), -3)
        self.assertEqual(subGame(-1, 1), -2)
        self.assertEqual(subGame(-1, -1), 0)
        self.assertEqual(subGame(0, 1), -1)
        self.assertEqual(subGame(1, 0), 1)
        self.assertEqual(subGame(10, 5), 5)
        self.assertEqual(subGame(10, 1), 9)

    def test_basicOperatorsGame_1(self):
        "Test basic Operators game"
        self.assertEqual(basicOperatorsGame(5,10,1),15)
        self.assertEqual(basicOperatorsGame(5,10,2),-5)
        self.assertEqual(basicOperatorsGame(5,10,3),50)
        self.assertEqual(basicOperatorsGame(5,10,4),0)

    def test_modulusGame_1(self):
        "Test Modulus Operation"
        self.assertEqual(modulusGame(2, 5), 2)
        self.assertEqual(modulusGame(-1, 1), 0)
        self.assertEqual(modulusGame(-1, -1), 0)
        self.assertEqual(modulusGame(0, 1), 0)
        self.assertEqual(modulusGame(1, 1), 0)
        self.assertEqual(modulusGame(10, 5), 0)
        self.assertEqual(modulusGame(10, 1), 0)
        self.assertEqual(modulusGame(10, 7), 3)
        
    def test_get_int_between_x_and_y_inclusive(self):
        "Test getting an int between a given range"
        self.assertNotEqual(get_int_between_x_and_y_inclusive("Test: must enter 2:",1,2),3)
        self.assertNotEqual(get_int_between_x_and_y_inclusive("Test: must enter 2:",0,10),-1)
        self.assertNotEqual(get_int_between_x_and_y_inclusive("Test: must enter 2:",0,10),'g')

    def test_get_greater_than_zero_int(self):
        "Test getting an int greater than zero"
        self.assertNotEqual(get_greater_than_zero_int("Test: must enter 2:"),0)
        self.assertNotEqual(get_greater_than_zero_int("Test: must enter 2:"),'g')

    def test_get_valid_range(self):
        "Test getting a number greater than given input"
        self.assertNotEqual(get_valid_range("Test: must enter 2:",2),1)
        self.assertNotEqual(get_valid_range("Test: must enter 2:",0),-1)
        self.assertNotEqual(get_valid_range("Test: must enter 2:",0),'g')
    
    def test_get_valid_int(self):
        "Test getting a valid int"
        self.assertNotEqual(get_valid_int("Test: must enter 2:"),'f')
        self.assertNotEqual(get_valid_int("Test: must enter 2:"),'g')



if __name__ == '__main__':
    unittest.main()