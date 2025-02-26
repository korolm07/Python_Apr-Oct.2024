import pandas as pd
crypto_list = ['BTC', 'XRP', 'LTC', 'ADA', 'ETH']

#convert list into series
crypto_series = pd.Series(data=crypto_list)
print (crypto_series)
print(type (crypto_series))

#immediate assignment
crypto_prices_prices = pd.Series(data=[2000,500,2000,20,50])
print(crypto_prices_prices)

stocks = ['lloyds', 'Wood', 'Palantir']
stocks_series = pd.Series(data=stocks)
print (stocks_series)
print (type (stocks_series))

#define panda series with custom index (above was default)
crypto_labels = ['crypto#1', 'crypto#2', 'crypto#3', 'crypto#4', 'crypto#5']
crypto_series = pd.Series (data=crypto_list, index = crypto_labels)
print (crypto_series)

stock_lables = ['stock#1', 'stock#2', 'stock#3']
stock_series_lables = pd.Series(data = stocks, index = stock_lables)
print (stock_series_lables)

#define series from dictionary
my_dict = {'Employee ID': 1, 'Employee name': 'Steve', 'Salary[$]': 2000, 'Years with Company': 10}
employee_series = pd.Series(my_dict)
print(employee_series)

#pandas attributes
print(crypto_series)
print(crypto_series.values)
print(crypto_series.index)
print(crypto_series.dtype)
print(crypto_series.is_unique) #like question: is it unique - true or false
print(crypto_series.shape)
print(crypto_series.size)

#pandas methods
crypto_prices = pd.Series(data = [2,4,5])
#sum of all elements in series: 
print(crypto_prices.sum())
#multiplication
print(crypto_prices.product())
#average
print(crypto_prices.mean())
#show first couple of elements 
print(crypto_prices.head(2))
#head creates new dataframe - in ex. below - new dataframe with first 2 rows extracted
new_crypto_prices = crypto_prices.head(2)
print(new_crypto_prices)
#last rows extract
print(crypto_prices.tail(2))
print(crypto_prices.memory_usage())

#import csv
#BTC_price_series = pd.read_csv('crypto.csv', squeeze=True) #squeeze True -> series. squeze false -> dataframe. Squeeze doesnt work in newer panda versions. 
df = pd.read_csv('crypto.csv')
series = df.iloc[:, 0]  # Select the first column as a Series
#print(series)
print (len(series))
print (max(series))
print (min(series))
my_series = pd.Series(data = [-10,100,-30,50,100])
my_series = abs(my_series) #convert all into positive
my_series = set(my_series) #get only unique
print(my_series)

#sorting
print(series.sort_values(ascending = False))
#series.sort_values(inplace = True)
#series.sort_index(inplace = True)
#print (series)
print(series.count())
print(series.describe()) #nice one - all statistic in one row
#check if num exists in series
print(1295.5 in series)
print(1295 in series.index)
prices_series = round(series)
print(399 in prices_series.values)
crypto_prices = pd.Series(data = [400, 500, 1500, 20, 70])
print(crypto_prices.mean())