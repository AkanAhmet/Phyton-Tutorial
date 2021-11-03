import pandas as pd
data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
} 
print(data)

df = pd.DataFrame(data, index=['ahmet',"akan","burak","duman"])
print(df)

print(df.loc["ahmet"])
print()
print(df.iloc[0])


print("------------------ READING DATA FROM CSV------------------------------")
df2 = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
print(df2.head(10)) # head() ilk 5 , tail() son 5 veriyi verir

print(df2.info)

df2.drop('state',axis=1,inplace=True) # axis = 1 for column , axis = 0 for row
df2['month'] = pd.to_datetime(df2['date'], format="%d.%m.%y").dt.month_name()
df2.set_index('date', inplace=True) # inplace anında geçerli olmasını sağlar

print(df2['month'].value_counts())
print(df2.groupby('month')['cases'].sum())

print(df2.head())
print(df2.describe)