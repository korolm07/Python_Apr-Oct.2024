import pandas  
#in terminal  is harder to read info extracted in this way:
# with open('population_data.csv') as data_file:
   # data = data_file.readlines()
   # print(data)

#in terminal  is easier to read info extracted in this way:
import csv
with open('population_data.csv') as data_file:
    data = csv.reader(data_file)
    #to print all data:  
    #for row in data: 
        #print(row)
    #to print only 3rd column: 
    #for row in data: 
       # print(row[2])
    #to print 3rd column all in one list: 
    population = []
    for row in data: 
        if row[2] != 'pop':
            population.append(int(row[2]))
    #print(population)

data = pandas.read_csv('population_data.csv')
#print (data["pop"]) #print all data from column pop
print(type(data)) #row csv file is always Dataframe 'data type'.
print(type(data['pop']))  # column is always Series 'data type'.

pandas.set_option('display.max.rows', None) #all rows will be printed not just first 5 and last 5.. max default is 60 
#print (data)
#print(data.tail()) #last 5 rows
#print(data.head()) #first 5 rows
#print(data.head(2))
#print(data.info()) #object - all except specific data types (like num, data,..)
pandas.set_option('display.float_format', str)
#basic_statistics = data.describe(include='all') #by default is only integer, but we can include all
#print(basic_statistics)

#create series manually based on list: 
population = pandas.Series ([100,200,500],index=['London',"berlin","Tokyo"])
print (population.values) #like dictionary
print (population.index)
revenue = pandas.Series ({'London':100000, "Berlin": 3455667})
#print(revenue)
average_population = data['pop'].mean() #avarege value
print (average_population)
#print(data.country)

#ACCESS SERIES ELEMENT: 


    
 