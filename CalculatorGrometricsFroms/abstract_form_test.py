
import unittest
from abstract_form import abstract_form

class test_abstract_form(unittest.TestCase):

    def test_elements(self):
        
        abstract_form_1 = abstract_form()
        
        self.assertEqual(type(abstract_form_1.perimeter()), str)
        self.assertEqual(abstract_form_1.print_parameters(), None)
        
        self.assertEqual(type(abstract_form_1.parameters), dict)
        self.assertEqual(type(abstract_form_1.sides), list)


if __name__ == '__main__':
    
    unittest.main()



