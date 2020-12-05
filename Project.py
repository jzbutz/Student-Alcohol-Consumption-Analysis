"""
Name: Jonathan Butz && David Lee
Directory ID: jzbutz && *****
Date: 2020-11-08
Assignment: Final Project
"""
import pandas as pd
import re 
import csv
import sys

def main():
    df = pd.read_csv('smath.csv')
    print(df["Dalc"].mean())
    print(df["Walc"].mean())
    df_cond = df[["Dalc", "Walc", "absences", "failures", "G3", "Pstatus", "famsup", "internet"]]
    
    #I am only interested in students with DALC and WALC higher than the mean
    df_DWalc = df_cond[(df["Walc"] > df["Walc"].mean()) & (df["Dalc"] > df["Dalc"].mean())]
    #print(df_DWalc)
    print(round(df_DWalc["failures"].mean(), 2))
    print(round(df_DWalc["absences"].mean(),2))
    print(round(df_DWalc["G3"].mean(), 2))
    
    #I am only interested in students with DALC and WALC lower than the mean
    df_DWalcLow = df_cond[(df["Walc"] <= df["Walc"].mean()) & (df["Dalc"] <= df["Dalc"].mean())]
    #print(df_DWalcLow)
    print(round(df_DWalcLow["failures"].mean(), 2))
    print(round(df_DWalcLow["absences"].mean(),2))
    print(round(df_DWalcLow["G3"].mean(), 2))
    
    df_Pstatus = df_cond[(df["Pstatus"] == "A")]
    print(df_Pstatus)
    print(round(df_Pstatus["Dalc"].mean(), 2))
    print(round(df_Pstatus["Walc"].mean(), 2))
    print(round(df_Pstatus["G3"].mean(), 2))
    
    df_Pstatus2 = df_cond[(df["Pstatus"] == "T")]
    print(df_Pstatus2)
    print(round(df_Pstatus2["Dalc"].mean(), 2))
    print(round(df_Pstatus2["Walc"].mean(), 2))
    print(round(df_Pstatus2["G3"].mean(), 2))
    
    df_cond2 = df_cond[(df["internet"] == "no") & (df["famsup"] == "no")]
    print(df_cond2)
    print(round(df_cond2["Dalc"].mean(), 2))
    print(round(df_cond2["Walc"].mean(), 2))
    print(round(df_cond2["G3"].mean(), 2))
    
    df_cond3 = df_cond[((df["Walc"] <= df["Walc"].mean()) & (df["Dalc"] <= df["Dalc"].mean()) & (df["internet"] == "yes") & (df["famsup"] == "yes") & (df["Pstatus"] == "T"))]
    print(df_cond3)
    print(round(df_cond3["Dalc"].mean(), 2))
    print(round(df_cond3["Walc"].mean(), 2))
    print(round(df_cond3["G3"].mean(), 2))
    
if __name__ == "__main__":
    main()