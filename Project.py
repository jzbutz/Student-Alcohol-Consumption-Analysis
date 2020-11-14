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
        failure: a list of integers representing number of failures for each student.
        studentDalc: a list of integers representing the workday alcohol consumption for each student.
        studentWalc: a list of integers representing the weekend alcohol consumption for each student.
        absence: a list of integers representing the number of school absences for each student (from 0 to 93).
        finalGrade: a list of integers  representing the final grade for each student (from 0 to 20).
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
        
        print(self.finalGrade)

if __name__ == "__main__":
    student = Student()