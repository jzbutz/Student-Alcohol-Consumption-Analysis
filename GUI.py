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

class Menu:

    def __init__ (self):

        self.input = 0
        
    def navigate(self):
        
        print("This program will help you analyze a dataset that has information on 397 students taking math.")
        print("Please note that DALC stands for workday alcohol consumption and WALC stands for weekend alcohol consumption.")
        print("Please select from the following menu options.")
        print("1. The mean DALC for all students. 1 represents very low, 5 represents very high.")
        print("2. The mean WALC for all students. 1 represents very low, 5 represents very high.")
        print("3. More information on students with higher than average DALC and WALC.")
        print("4. More information on students with lower than average DALC and WALC.")
        print("5. Exit the program.")
        self.input = input("Please enter your choice: ")
        
        if(self.input == "3"):
            print("Please select from the following options for information on students with higher than average DALC and WALC.")
            print("1. Average number of class previous class failures")
            print("2. Average number of absences.")
            print("3. Average final grade, from 0 to 20.")
            self.input = input("Please enter your choice: ")
            self.input = int(self.input) + 5
            
        elif(self.input == "4"):
            print("Please select from the following options for information on students with lower than average DALC and WALC.")
            print("1. Average number of class previous class failures")
            print("2. Average number of absences.")
            print("3. Average final grade, from 0 to 20.")
            self.input = input("Please enter your choice: ")
            self.input = int(self.input) + 8
            
        elif(self.input == "5"):
            self.input = 0
        
        else:
            self.input = 3
        
        return self.input