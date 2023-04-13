'''
**************************************************
Created by: MD Nashid Anjum
Date: November 1, 2022
contact: nashid.anjum@ryerson.ca

This example shows how to plot data using bar plot 
**************************************************
'''

import matplotlib.pyplot as plt

x = ['item1', 'item2', 'item3', 'item4', 'item5']
y = [10, 15, 18, 16, 11]

plt.figure(1)
plt.bar(x,y)

plt.title("Product Prices") # Writing plot title
plt.xlabel("Products")      # Writing x-axis label
plt.ylabel("Price in CAD")  # Writing y-axis label

plt.show()

