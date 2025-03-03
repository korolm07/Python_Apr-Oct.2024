data = { 
    'name': ['Alice', 'Bob', 'Charlie'], 
    'profession': ['Engineer', 'Doctor', 'Artist'], 
    'age': [28, 34, 22] 
} 
df = pd.DataFrame(data).set_index('age', drop = False).sort_index() 
#Or 
df = pd.DataFrame(data).reset_index().sort_index(ascending = False) #it will add index: 1,2,3,4  

#concat
import pandas as pd 
customers_a = pd.read_csv(r"C:\Users\Downloads\Data+Sources\Data Sources\CustomersA.csv") 
customers_b = pd.read_csv(r"C:\Users\Downloads\Data+Sources\Data Sources\CustomersB.csv") 
Customers = pd.concat ([customers_a,customers_b]) 

#Glob 
import pandas as pd 
import glob  
#this is how to load all csv files form one directory 
csv_files = glob.glob(r"C:\Users\Downloads\Data+Sources\Data Sources\*.csv") 
#make data frame that combines all files  
combined = pd.concat((pd.read_csv(f) for f in csv_files)) 
#drop collumn we do not need 
customers = combined.drop(['GeographyKey', 'Title', 'MiddleName'], axis = 1) 
#drop rows 
customers_rows = combined.drop(1,axis=0) 
#usecols  
use_columns = pd.concat((pd.read_csv(f, usecols = ['FirstName']) for f in csv_files)) 
#Export data:  
combined.to_csv(r"C:\Users\Downloads\Data+Sources\Data Sources\customerscombined.csv", index = False) 
#list all file names: 
import os  
directory = os.listdir('C:\\Users\\Downloads\\Data+Sources\\Data Sources') 
listDir = pd.DataFrame({"FileName":directory}) 
merged = pd.merge (tableA, tableB, how = 'Inner') 

import pandas as pd  
customers_a = pd.read_csv(r"C:\Users\Downloads\Data+Sources\Data Sources\CustomersA.csv") 
customers_b = pd.read_csv(r"C:\Users\Downloads\Data+Sources\Data Sources\CustomersB.csv")  
Customers = pd.concat([customers_a, customers_b])  
df = Customers[['CustomerKey', 'FirstName', 'LastName']] 
df.to_csv(r"C:\Users\Downloads\Data+Sources\Data Sources\newexportedfile.csv", index = False)  

#Merge allows to combine objects based on key  
import pandas as pd  
LeftFrame = pd.read_csv(r"C:\Users\QZ313YS\Downloads\Data+Sources\Data Sources\customerscombined.csv")  
RightFrame = pd.read_csv(r"C:\Users\QZ313YS\Downloads\Data+Sources\Data Sources\Sales.csv")  
Merged = pd.merge(LeftFrame, RightFrame, how = 'inner") 
#Join. Join happens on index, merge – on collumn names  

import pandas as pd  
LeftFrame = pd.read_csv(r"C:\Users\QZ313YS\Downloads\Data+Sources\Data Sources\customerscombined.csv")  
RightFrame = pd.read_csv(r"C:\Users\QZ313YS\Downloads\Data+Sources\Data Sources\Sales.csv")  
#Join = LeftFrame.join(RightFrame, lsuffix="CustomerKey", rsuffix = "CustomerKey") 
JoinedK = LeftFrame.join(RightFrame.set_index("CustomerKey"), on = "CustomerKey") 

#drop enire column if there are o nul values  
#dropnavalues = Joined.dropna() 
Delta = Joined.drop(["Unnamed: 0", "Title"], axis = 1) 
dropnavalues = Delta.dropna() 

#second way to get rid of empty spaces:  
MiddleName = Joined["MiddleName"].fillna("Middle Name not Defined", inplace = True) 
#third way, empty place is replaced by previous row 
Backfill = Joined["YearlyIncome"].fillna(method = "backfill", inplace = True) 

 
#Matplotlib  
#pie chart 
import matplotlib.pyplot as plt 
explode = (0,0.1) 
plt.pie(dataset.OrderQuantity, labels = dataset.Gender, autopct = "%1.1f%%", colors = ["#e76f51", "#219ebc"], shadow = True, startangle = 90, explode= explode, hatch=['**O', 'oO']) 
plt.show() 
 

#Bar chart 
import matplotlib.pyplot as plt 
plt.style.use('ggplot') 
x = dataset.Year 
y = dataset.OrderQuantity 
plt.barh(x,y, color = "green") 
plt.yticks(fontsize=20) 
plt.xlabel("Number of Orders, fontsize =15") 
plt.show() 

#Subplots 
import matplotlib.pyplot as plt  
fig, axs = plt.subplots(1,3, figsize=(9,3), sharey=True) #one row with 3 columns 
axs[0].bar(dataset.FirstName, dataset.SalesAmount) 
axs[1].scatter(dataset.FirstName, dataset.SalesAmount) 
axs[2].plot(dataset.FirstName, dataset.SalesAmount) 
fig.suptitle('Subplots') 
plt.show() 

 

 

 