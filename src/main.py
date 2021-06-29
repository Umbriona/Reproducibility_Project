import argparse
import pandas as pd
import utils

parser = argparse.ArgumentParser(""" """)
parser.add_argument('-d', "--connection_data", type=str, required = True)
parser.add_argument('-p', "--pfam_data", type=str, required = True)

parser.add_argument('-c', "--connection_condition", type = int, default = 500)
parser.add_argument('-n', "--node_degree", type = int, default = 100 )

parser.add_argument('-o', "--output", type = str, default = "results/boxplot.png")

def main(args):
    
    df_high, df_low = utils.prepare_data(args.connection_data, args.connection_condition)
    node_degree_high, node_degree_low = utils.network_degree(df_high, args.node_degree)
    
    df_pfam = pd.read_table(args.pfam_data)
    
    df_degree_high = utils.add_pfam2frames(df_pfam, node_degree_high , label = "High")
    df_degree_low = utils.add_pfam2frames(df_pfam, node_degree_low , label = "Low")
    
    df_degree_highlow = pd.concat([df_degree_high, df_degree_low])
    
    utils.plot_stat(df_degree_highlow, args.output)
    
    
    return 0

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
