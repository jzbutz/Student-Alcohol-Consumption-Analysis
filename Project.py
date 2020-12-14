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
from GUI import Menu

def main(userInput2):
    userInput = int(userInput2)
    df = pd.read_csv('smath.csv')
    
    df_cond = df[["Dalc", "Walc", "absences", "failures", "G3", "Pstatus", "famsup", "internet"]]
    
    #I am only interested in students with DALC and WALC higher than the mean
    df_DWalc = df_cond[(df["Walc"] > df["Walc"].mean()) & (df["Dalc"] > df["Dalc"].mean())]
    
    #I am only interested in students with DALC and WALC lower than the mean
    df_DWalcLow = df_cond[(df["Walc"] <= df["Walc"].mean()) & (df["Dalc"] <= df["Dalc"].mean())]
    
    
    #df_Pstatus = df_cond[(df["Pstatus"] == "A")]
    #print(round(df_Pstatus["Dalc"].mean(), 2))
    #print(round(df_Pstatus["Walc"].mean(), 2))
    #print(round(df_Pstatus["G3"].mean(), 2))
    
    #df_Pstatus2 = df_cond[(df["Pstatus"] == "T")]
    #print(round(df_Pstatus2["Dalc"].mean(), 2))
    #print(round(df_Pstatus2["Walc"].mean(), 2))
    #print(round(df_Pstatus2["G3"].mean(), 2))
    
    #df_cond2 = df_cond[(df["internet"] == "no") & (df["famsup"] == "no")]
    #print(round(df_cond2["Dalc"].mean(), 2))
    #print(round(df_cond2["Walc"].mean(), 2))
    #print(round(df_cond2["G3"].mean(), 2))
    
    #df_cond3 = df_cond[((df["Walc"] <= df["Walc"].mean()) & (df["Dalc"] <= df["Dalc"].mean()) & (df["internet"] == "yes") & (df["famsup"] == "yes") & (df["Pstatus"] == "T"))]
    #print(round(df_cond3["Dalc"].mean(), 2))
    #print(round(df_cond3["Walc"].mean(), 2))
    #print(round(df_cond3["G3"].mean(), 2))
    
    if(userInput == 0):
        print("Ending the program.")
        return True
    if(userInput == 1):
        print("The mean DALC of all students is", round(df["Dalc"].mean(), 3))
        input("Press any key to continue...")
        return False
    if(userInput == 2):
        print("The mean WALC of all students is", round(df["Walc"].mean(), 3))
        input("Press any key to continue...")
        return False
    if(userInput == 3):
        print("You have entered an invalid key.")
        input("Press any key to continue...")
        return False
    if(userInput == 6):
        print("The average number of past failures is", round(df_DWalc["failures"].mean(), 2))
        input("Press any key to continue...")
        return False
    if(userInput == 7):
        print("The average number of absences is", round(df_DWalc["absences"].mean(),2))
        input("Press any key to continue...")
        return False
    if(userInput == 8):
        print("The average final grade is", round(df_DWalc["G3"].mean(), 2))
        input("Press any key to continue...")
        return False
    if(userInput == 9):
        print("The average number of past failures is", round(df_DWalcLow["failures"].mean(), 2))
        input("Press any key to continue...")
        return False
    if(userInput == 10):
        print("The average number of absences is", round(df_DWalcLow["absences"].mean(),2))
        input("Press any key to continue...")
        return False
    if(userInput == 11):
        print("The average final grade is", round(df_DWalcLow["G3"].mean(), 2))
        input("Press any key to continue...")
        return False
    
if __name__ == "__main__":
    finished = False
    menu = Menu()
    while(finished == False):
        userInput2 = menu.navigate()
        finished = main(userInput2)