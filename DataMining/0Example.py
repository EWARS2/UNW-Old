import pandas as pd
import numpy as np
coffee = pd.read_csv('coffee.csv')
print("\nHere is the data")
print(coffee.head())

print("\nHere is last five records")
print(coffee.tail(5))

print("\nHere is a sample of four items")
print(coffee.sample(4))

print("\nHere are rows 3 and 5")
print(coffee.loc[[3,5]])
print("\nHere are odd rows starting at row 3")
print(coffee.loc[3::2])

print('\nHere are some rows with column Day')
print(coffee.loc[1:5,'Day'])

print('\nHere are some rows with two columns')
print(coffee.loc[1:5,['Day','Units Sold']])

print('\nHere are some rows with two columns')
print(coffee.iloc[1:5,[0,2]])

#print('\nWednesday values')
#coffee.index = coffee['Day']
#print(coffee.loc['Wednesday'])

print('\nUpdating Data Frame')
coffee.loc[1,'Units Sold'] = 10
print(coffee)

print('\nSorting Data')
print(coffee.sort_values(['Units Sold','Day'], ascending = [0,0]))

print('\nGetting Info')
print(coffee.info())

print('\nFiltering Data by numerical condition')
print(coffee.loc[coffee['Units Sold'] > 29])

print('\nFiltering Data by string condition')
print(coffee[coffee['Day'].str.contains('s|S')])

print('\nFiltering Data by isin condition')
print(coffee[coffee['Day'].isin(['Monday','Friday'])])

print('\nFiltering Data by query')
#print(coffee.query('Day == "Monday" or Units_Sold == 35'))

print('\nAdding Columns')
coffee['Unit Price'] = np.where(coffee['Coffee Type']=='Espresso',3.99,5.99)
print(coffee)
coffee['Profit'] = coffee['Units Sold']*coffee['Unit Price']
print(coffee)

print('\nRemoving Column')
print(coffee.drop(columns=['Unit Price']))

print('\nValue Counts')
print(coffee['Units Sold'].value_counts())

print('\nSum Units Sold')
print(coffee['Units Sold'].sum())
print('\nAverge Units Sold')
print(coffee['Units Sold'].mean())
print('\nStd Units Sold')
print(coffee['Units Sold'].std())

print('\nSum Units Sold by Coffee Type')
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())

print('\nAverage Units Sold by Coffee Type')
print(coffee.groupby(['Coffee Type'])['Units Sold'].mean())
