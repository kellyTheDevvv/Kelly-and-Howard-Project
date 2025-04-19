import pandas as pd

data = {
    "name" : ['Alice','Boibo','Charlie','David'],
    "age" : [25, 30, 35, 40],
    "score" : [85, 90, 95, 100]
}

df = pd.DataFrame(data)
#print("DataFrame:\n",df)
#print("name:", df['age'])
print(df[df['score'] >= 90])