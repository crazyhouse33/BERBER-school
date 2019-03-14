import unittest
import sys

sys.path.append("../../src/")
from controller import Controller

class TestController(unittest.TestCase):
    
    def testInterpreteData(self):
        print("TESTING INTERPRETING OF DATA ARGUMENT...")
        
        controller = Controller(5, 42, "20", 0, True, False, True)
        
        dataTest1 = "5849"
        resultTest1 = controller.interpreteData(dataTest1)
        print(str(resultTest1))
        self.assertEqual(resultTest1, 5849)
        
        dataTest2 = "10K"
        resultTest2 = controller.interpreteData(dataTest2)
        print(str(resultTest2))
        self.assertEqual(resultTest2, 10000)
        
        dataTest3 = "42M"
        resultTest3 = controller.interpreteData(dataTest3)
        print(str(resultTest3))
        self.assertEqual(resultTest3, 42000000)
        
        dataTest4 = "254G"
        resultTest4 = controller.interpreteData(dataTest4)
        print(str(resultTest4))
        self.assertEqual(resultTest4, 254000000000)
        
        dataTest5 = "25Q"
        resultTest5 = controller.interpreteData(dataTest5)
        print(str(resultTest5))
        self.assertEqual(resultTest5, -1)
        
if __name__ == '__main__':
    unittest.main()
