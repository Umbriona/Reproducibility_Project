import os
import unittest
import pandas as pd
from src import utils

# Define (static variables)
INTERACTION_FILE = "data/9606.protein.links.v11.0.txt" 
PFAM_FILE = "data/proteins_w_domains.txt"
CONDITION_CONECTION = 500
CONDITION_DEGREE = 100



class TestUtilsPreparedata(unittest.TestCase):
    def test_split(self): 
        DF_HIGH, DF_LOW = utils.prepare_data(INTERACTION_FILE, CONDITION_CONECTION)
        self.assertLessEqual(CONDITION_CONECTION, min(DF_HIGH["combined_score"]))
        self.assertGreater(CONDITION_CONECTION, max(DF_LOW["combined_score"]))
        self.assertEqual(6, len(DF_LOW.keys()) + len(DF_HIGH.keys()))

        
    def test_values(self):
        self.assertRaises(ValueError, utils.prepare_data, INTERACTION_FILE, 0)
        self.assertRaises(ValueError, utils.prepare_data, INTERACTION_FILE, -1)
    
    def test_types(self):
        self.assertRaises(TypeError, utils.prepare_data, INTERACTION_FILE, 1 + 3j)
        self.assertRaises(TypeError, utils.prepare_data, INTERACTION_FILE, True)
        self.assertRaises(TypeError, utils.prepare_data, INTERACTION_FILE, "10")
        
class TestUtilsMakeNetworks(unittest.TestCase):

        
    def test_type(self):
        df_empty = pd.DataFrame({'A' : []})
        
        self.assertRaises(TypeError, utils.network_degree, 10, CONDITION_DEGREE)
        self.assertRaises(TypeError, utils.network_degree, True, CONDITION_DEGREE)
        self.assertRaises(TypeError, utils.network_degree, "10", CONDITION_DEGREE)
        self.assertRaises(TypeError, utils.network_degree, df_empty, 10+2j)
        self.assertRaises(TypeError, utils.network_degree, df_empty, "10")
        self.assertRaises(TypeError, utils.network_degree, df_empty, False)
        
    def test_values(self): 
        DF_HIGH, DF_LOW = utils.prepare_data(INTERACTION_FILE, CONDITION_CONECTION)
        DF_DEGREE_HIGH, DF_DEGREE_LOW = utils.network_degree(DF_HIGH, CONDITION_DEGREE)
        
        self.assertEqual(4, len(DF_DEGREE_HIGH.keys()) + len(DF_DEGREE_LOW.keys()))
        self.assertFalse(bool(set(DF_DEGREE_HIGH["Protein"]) & set(DF_DEGREE_LOW["Protein"])))
        
class TestUtilsPfam(unittest.TestCase):

        
    def test_type(self):
        
        df_empty = pd.DataFrame({'A' : []})
        self.assertRaises(TypeError, utils.add_pfam2frames, 10, df_empty)
        self.assertRaises(TypeError, utils.add_pfam2frames, True, df_empty)
        self.assertRaises(TypeError, utils.add_pfam2frames, "10", df_empty)
        self.assertRaises(TypeError, utils.add_pfam2frames, df_empty, 10+2j)
        self.assertRaises(TypeError, utils.add_pfam2frames, df_empty, "10")
        self.assertRaises(TypeError, utils.add_pfam2frames, df_empty, False)
        
    def test_shape(self):
        DF_HIGH, DF_LOW = utils.prepare_data(INTERACTION_FILE, CONDITION_CONECTION)
        DF_DEGREE_HIGH, DF_DEGREE_LOW = utils.network_degree(DF_HIGH, CONDITION_DEGREE)
        DF_PFAM = pd.read_table(PFAM_FILE)
        DF_DEGREE_PFAM = utils.add_pfam2frames(DF_PFAM, DF_DEGREE_HIGH)
        
        self.assertEqual(5, len(DF_DEGREE_PFAM.keys()))
        self.assertFalse(any(list(DF_DEGREE_PFAM.isna()["Pfam IDs"])))
        
        