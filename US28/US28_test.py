import unittest
import pandas as pd
from US28_order_siblings_by_age import order_siblings_by_age

class TestOrderSiblingsByAge(unittest.TestCase):
    def test_order_siblings_by_age(self):
        
        individuals_data = {
            'ID': ['@I1@', '@I2@', '@I3@'],
            'NAME': ['Alice', 'Bob', 'Charlie'],
            'BIRTHDAY': ['1 JAN 1990', '1 JAN 1985', '1 JAN 1995']
        }
        individuals = pd.DataFrame(individuals_data)

      
        families_data = {
            'ID': ['@F1@', '@F2@'],
            'CHILDREN': [['@I1@', '@I2@'], ['@I3@']]
        }
        families = pd.DataFrame(families_data)

  
        ordered_siblings = order_siblings_by_age(individuals, families)

  
        expected_result = [
            {'family_id': '@F1@', 'siblings': ['Alice', 'Bob']},
            {'family_id': '@F2@', 'siblings': ['Charlie']}
        ]

        self.assertEqual(ordered_siblings, expected_result)

if __name__ == '__main__':
    unittest.main()
