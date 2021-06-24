import os
import unittest
from src import utils

INTERACTION_FILE = "data/9606.protein.links.v11.0.txt" 

class TestUtilsPreparedata(unittest.TestCase):
    def test_split(self):
        df_high, df_low = utils.prepare_data(INTERACTION_FILE, 500)
        
        self.assertLessEqual(500, min(df_high["combined_score"]))
        self.assertGreater(500, max(df_low["combined_score"]))
        self.assertEqual(6, len(df_low.keys()) + len(df_high.keys()))
        
    def test_values(self):
        self.assertRaises(ValueError, utils.prepare_data, INTERACTION_FILE, 0)
        self.assertRaises(ValueError, utils.prepare_data, INTERACTION_FILE, -1)
    
    def test_types(self):
        self.assertRaises(TypeError, utils.prepare_data, INTERACTION_FILE, 1 + 3j)
        self.assertRaises(TypeError, utils.prepare_data, INTERACTION_FILE, True)
        self.assertRaises(TypeError, utils.prepare_data, INTERACTION_FILE, "10")
        
        
        