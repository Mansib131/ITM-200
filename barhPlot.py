import matplotlib.pyplot as plt

x = ['item1', 'item2', 'item3', 'item4', 'item5']
y = [10, 15, 18, 16, 11]

plt.figure(1)
plt.barh(x,y)

plt.title("Product Prices")
plt.xlabel("Products")
plt.ylabel("Price in CAD")
plt.grid()                  # Showing grids on the plot

plt.show()
