import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

SMALL_SIZE = 16
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

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

def network_degree(df, condition):
    
    if type(df) != pd.core.frame.DataFrame or type(condition) not in [int, float]:
        raise TypeError("Args must be pandas dataframe and int or float")
    

    network_high = nx.from_pandas_edgelist(df, source = "protein1", target = "protein2")     

    node_degree = pd.DataFrame(network_high.degree, columns=["Protein", "Degree"])
    
    node_degree_high = node_degree[node_degree["Degree"] > condition]
    node_degree_low  = node_degree[node_degree["Degree"] <= condition]
    
    return node_degree_high, node_degree_low


def add_pfam2frames(df_pfam, df_degree, label = "High"):
    
    if type(df_pfam) != pd.core.frame.DataFrame or type(df_degree) != pd.core.frame.DataFrame:
        raise TypeError("Args must be pandas dataframe and int or float")

    list_pfam = []
    for key in df_degree["Protein"]:
        pfams = list(df_pfam["Pfam ID"].loc[df_pfam["Protein stable ID"] == key.split(".")[-1]])
        if np.NAN in pfams:
            list_pfam.append(np.NAN)
        else:
            list_pfam.append(pfams)
            
    df_degree["Pfam IDs"] = list_pfam
    
    df_degree = df_degree.dropna()
    
    n_pfam = [len(entery) for entery in df_degree["Pfam IDs"]]
    df_degree.loc[:, "Number of domains"] = n_pfam
    df_degree.loc[:, "Connectivity"] = [label for _ in range(len(n_pfam))]
    return df_degree


def plot_stat(df_pfam_highlow, file, args):
    
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    plt.figure(figsize=[10,7])
    plt.yscale("log")
    sns.boxplot(x="Connectivity", y="Number of domains", data=df_pfam_highlow)
    plt.title("Difference of the number of pfam domains\n in proteins with higly and low connectivity")
    plt.savefig(file)
    print("saving image at {}".format(file))
    return 0