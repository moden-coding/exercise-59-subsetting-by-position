#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t', index_col=0)
    pass

def main():
    df = subsetting_by_positions()
    print(df)

if __name__ == "__main__":
    main()
