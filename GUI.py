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

class Menu:
    """This class will display a menu and return a value to the project file from user input.
    """

    def __init__ (self):
        """Class initializer
        """

        self.input = 0
        
    def navigate(self):
        """Display a menu and return a value to the project file from user input.
        
        Return:
            self.input(int): user input from menu choice
        """
        
        print("This program will help you analyze a dataset that has information on 397 students taking math.")
        print("Please note that DALC stands for workday alcohol consumption and WALC stands for weekend alcohol consumption.")
        print("Please select from the following menu options.")
        print("1. The mean DALC for all students. 1 represents very low, 5 represents very high.")
        print("2. The mean WALC for all students. 1 represents very low, 5 represents very high.")
        print("3. More information on students with higher than average DALC and WALC.")
        print("4. More information on students with lower than average DALC and WALC.")
        print("5. To enter data visualization menu.")
        print("6. Exit the program.")
        self.input = input("Please enter your choice: ")
        
        if(self.input == "1"):
            return int(self.input)
        
        if(self.input == "2"):
            return int(self.input)
        
        if(self.input == "3"):
            print("Please select from the following options for information on students with higher than average DALC and WALC.")
            print("1. Average number of class previous class failures")
            print("2. Average number of absences.")
            print("3. Average final grade, from 0 to 20.")
            self.input = input("Please enter your choice: ")
            self.input = int(self.input) + 5
            return self.input
            
        if(self.input == "4"):
            print("Please select from the following options for information on students with lower than average DALC and WALC.")
            print("1. Average number of class previous class failures")
            print("2. Average number of absences.")
            print("3. Average final grade, from 0 to 20.")
            self.input = input("Please enter your choice: ")
            self.input = int(self.input) + 8
            return self.input
        
        if(self.input == "5"):
            print("Please select from the following options to see data visualized")
            print("1. Chart of final grades based on DALC consumption")
            print("2. Chart of final grades based on WALC consumption")
            print("3. Distribution of DALC")
            print("4. Distribution of WALC")
            self.input = input("Please enter your choice: ")
            self.input = int(self.input) + 11
            return self.input
            
        if(self.input == "6"):
            self.input = 0
            return self.input
        
        else:
            self.input = 3
            return self.input