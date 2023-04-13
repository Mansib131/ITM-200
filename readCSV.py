'''
**************************************************
Created by: MD Nashid Anjum
Date: November 1, 2022
contact: nashid.anjum@ryerson.ca

This program shows how to read .csv file contents
**************************************************
'''
import csv             
with open('sample.csv', mode = 'r') as fileCSV: # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)                  # Reading the csv file
    for line in fCSV:
        print(line)                     # Printing file content line by line
  
