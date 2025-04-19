import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [18,19,20,21],
    'Score' : [85, 90, 95, 100]
}

df = pd.DataFrame(data)
# print(df)   #outputs the whole DataFrame 
#print(df['Name']) # outputs the 'Name' column of the DataFrame
#print(df[df['Score'] > 90]) # outputs the rows where 'Score' is greater than 90
