"""
Name: Jonathan Butz && David Lee
Directory ID: jzbutz && dlee2424
Date: 2020-11-08
Assignment: Final Project
"""
import pandas as pd
import re 
import csv
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from GUI import Menu

def main(userInput2):
    """Read in csv data. Use pandas to subset data.
    Receive user input from a menu. Return value of subset chosen by user.
    
    Attr:
        userInput(int): received user input
        
    Returns:
        value of the subset chosen by the user & boolean to end or continue the program.
    """
    userInput = int(userInput2)
    df = pd.read_csv('smath.csv')
    
    df_cond = df[["Dalc", "Walc", "absences", "failures", "G3", "Pstatus", "famsup", "internet"]]
    
    #I am only interested in students with DALC and WALC higher than the mean
    df_DWalc = df_cond[(df["Walc"] > df["Walc"].mean()) & (df["Dalc"] > df["Dalc"].mean())]
    
    #I am only interested in students with DALC and WALC lower than the mean
    df_DWalcLow = df_cond[(df["Walc"] <= df["Walc"].mean()) & (df["Dalc"] <= df["Dalc"].mean())]
    
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
    if(userInput == 12):
        plot1 = sns.lmplot(x = "Dalc", y = "G3", data = df)
        plot1.set(xlabel = "Weekday Alcohol Consumption", ylabel = "Final Grade", xlim=(0,6), ylim=(0,21))
        plt.show()
        input("Press any key to continue...")
        return False
    if(userInput == 13):
        plot2 = sns.lmplot(x = "Walc", y = "G3", data = df)
        plot2.set(xlabel = "Weekend Alcohol Consumption", ylabel = "Final Grade", xlim=(0,6), ylim=(0,21))
        plt.show()
        input("Press any key to continue...")
        return False
    if(userInput == 14):
        df.hist("Dalc")
        plt.suptitle("Weekday Alcohol Consumption")
        plt.show()
        input("Press any key to continue...")
        return False
    if(userInput == 15):
        df.hist("Walc")
        plt.suptitle("Weekend Alcohol Consumption")
        plt.show()
        input("Press any key to continue...")
        return False      
    
if __name__ == "__main__":
    finished = False #boolean initializer for while loop
    menu = Menu()
    while(finished == False):
        userInput2 = menu.navigate() #navigate method from menu class
        finished = main(userInput2) #run main program, pass in user input, return boolean