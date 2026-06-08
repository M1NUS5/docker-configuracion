import unittest
from app import saludo

class TestSaludo(unittest.TestCase):
    
    def test_saludo(self):
        self.assertEqual(
            saludo(), 
            "Hola Docker desde GitHub Actions"
            )
        
if __name__ == '__main__':
    unittest.main()
    