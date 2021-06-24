import pandas as pd
import numpy as np
import networkx as nx

def prepare_data(file, condition):
    """
    Reads csv files separated with spaces and splits the data frame in to two frames
    according to the condition evaluated on the "combined_score" field.
    args file and condition
    """
    if type(condition) not in [int, float]:
        raise TypeError("Condition must be a real number")
    if condition < 1:
        raise ValueError("Condition can not be negative")
        
    df = pd.read_csv(file, sep = " ")
    df_high = df[df["combined_score"] >= condition]
    df_low  = df[df["combined_score"] <  condition]
    return df_high, df_low