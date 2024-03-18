import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#import the file (extraction of the data from csv file)
df = pd.read_csv('finance_liquor_sales.csv')

# EXPLORATION AND MANIPULATION
#We explore the raw data. What columns are in there, what type are they, are there any null values
print('Dataset Columns:\n', df.columns, '\n')
print('Dataset Info:')
print(df.info())
print('Dataset Statistics:\n', df.describe(), '\n')
print('\nNull Values:\n', df.isnull().sum(), '\n')

#We can see that the data column is object and not a date so we have to change it. also there are 18 missing store locations which we are going to drop

#Clean the rows with missing store location because it's the only columns that has a direct impact on the data we need to extract (sales per store, we should know the location)
df_cleaned = df.dropna(subset = ['store_location']).copy()
df_cleaned.drop_duplicates(inplace = True)                  #Delete any Duplicate row
df_cleaned.fillna(value = 'Unknown', inplace = True)
df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])     #Convert the data column to datetime type
df_cleaned.reset_index(drop = True, inplace = True)         #reset the index

print('First 5 rows:', df_cleaned.head())                   #Explore the cleaned dataset
print('Dataset Statistics:\n', df_cleaned.describe(), '\n')
print(df_cleaned.shape)

#Save the cleaned dataframe to a CSV file
df_cleaned.to_csv('finance_liquor_sales_CLEANED.csv', index=False)

#########################################################
# TASK 1

df_zip = df_cleaned.sort_values('zip_code', ascending = True).copy()                                        #We sort the dataset by zipcode
data = df_zip[['zip_code', 'item_number', 'bottles_sold']]                                                  #create a new smaller dataframe
group = data.groupby('zip_code').apply(lambda x: x.loc[x['bottles_sold'].idxmax()]).reset_index(drop=True)  #groupby zip code and max bottles sold
top_values = group.nlargest(5, 'bottles_sold').index                                                        #the maximum values for annotation
print(group)

plt.figure(figsize=(10, 6))
sns.scatterplot(data = group, x=group.index, y='bottles_sold', size = group['bottles_sold'], legend = False) #create a scatter plot with zip codes and bottles sold

# Annotate the top 5 item numbers on the scatter plot
for i in top_values:
    plt.annotate(group['item_number'][i].astype(int), (group.index[i], group['bottles_sold'][i]),
                 textcoords="offset points", xytext=(0, 5), ha='center', color = 'black')

plt.xlabel('zip Code')
plt.ylabel('Bottles Sold')
plt.title('Most popular item in sales for each zip code')

plt.show()

max_row = group.loc[group['bottles_sold'].idxmax()]
print('The most popular item is:', max_row['item_number'], "located in zip_code:", max_row['zip_code'])

#########################################################
# TASK 2

df_cleaned['year'] = df_cleaned['date'].dt.year                             #add a 'year' column
newest = df_cleaned[df_cleaned['year'].isin([2016, 2017, 2018, 2019])]      #create a new dataframe filtered by the time range we need
total_sales = newest['sale_dollars'].sum().astype(int)                      #calculate the total sales for the period 2016-2019


profit = newest.groupby('store_name')['sale_dollars'].sum()                 #group by store name and sum up the sales for each store
sorted_profit = profit.sort_values(ascending=False)                         #sort by sales
data2 = pd.DataFrame(sorted_profit)                                         #turn the series to dataframe
data2['percentage'] = ((data2['sale_dollars'] / total_sales) * 100)         #calculate the percentage column

data2.to_csv('finance_liquor_sales_CLEANED_task2.csv',sep='\t', index=True, encoding='utf-8')

print(data2.head())

plt.figure(figsize = (10, 6))                                               #seaborn horizontal bar plot
ax = sns.barplot(data = data2.head(20), x = 'percentage', y = 'store_name', orient = 'h', palette = 'blend:#7AB,#EDA', hue = 'percentage')

for container in ax.containers:                                             #add percentage values at the end of each bar
    ax.bar_label(container, fmt='%1.2f%%')


plt.xlabel('Sales %')
plt.ylabel('Store Name')
plt.title('% Sales by Store')
plt.grid(axis = 'x', alpha = 0.3)
plt.tight_layout()
plt.show()
