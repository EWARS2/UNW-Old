# Title: Sales Prediction
# Starting Out With Python, 5th Edition
# Chapter 2, Exercise 2
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Annual profit is X% of sales
# Annual profit percentage as decimal (1 = %100)
annualProfitPercentage = 0.23

# Get total sales and convert to float
totalSales = float(input("Input the projected amount of total sales: $"))

# Calculate annual profit
annualProfit = annualProfitPercentage * totalSales

# Give output with formatting
print(f"Annual profit is ${annualProfit:.2f}, "
      f"which is {annualProfitPercentage:.0%} "
      f"of the total sales of ${totalSales:.2f}")





# Programmed in IDLE. Why aren't we using it?
