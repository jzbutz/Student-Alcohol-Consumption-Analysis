"""
Name: Jonathan Butz
Directory ID: jzbutz
Date: 2020-11-08
Assignment: Final Project
"""

import re 
import csv
import sys

class Student:
    """A class for storing the data of all students found in the dataset.
    
    Attributes:
        failure: a list of strings representing number of failures for each student.
        studentDalc: a list of strings representing the workday alcohol consumption for each student.
        studentWalc: a list of strings representing the weekend alcohol consumption for each student.
        absence: a list of strings representing the number of school absences for each student (from 0 to 93).
        finalGrade: a list of strings  representing the final grade for each student (from 0 to 20).
    """
    def __init__(self):
        """
        Initializes a Student object. 
        """
        self.failure = []
        self.studentDalc = []
        self.studentWalc = []
        self.absence = []
        self.finalGrade = []
        
        file = open('smath.csv', 'r', encoding="utf8")
        spreadsheet = csv.reader(file)
        for row in spreadsheet: 
            self.failure.append(row[14])
            self.studentDalc.append(row[26])
            self.studentWalc.append(row[27])
            self.absence.append(row[29])
            self.finalGrade.append(row[32])
        file.close()
        
        self.failure.pop(0)
        self.studentDalc.pop(0)
        self.studentWalc.pop(0)
        self.absence.pop(0)
        self.finalGrade.pop(0)
        
    
    def calculate_averages(self):
        """
        A method for calculating the average absences for students with a combined WALC/DALC rating of 5 or higher
        """
        
        #index length 394
        index = 0
        number = 0
        highConsumptionAbsence = []
        
        while index < 395:
            if ((int(self.studentDalc[index]) + int(self.studentWalc[index])) >= 5):
                number = int(self.studentDalc[index])
                number = number + int(self.studentWalc[index])
                highConsumptionAbsence.append(self.absence[index])
                index = index + 1
            elif ((int(self.studentDalc[index]) + int(self.studentWalc[index])) < 5):
                index = index + 1
            else:
                print(highConsumptionAbsence)
                return highConsumptionAbsence
    
if __name__ == "__main__":
    student = Student()
    student.calculate_averages()