import matplotlib.pyplot as plt
import pandas as pd

# x = [1,2,3,4,5]
# y = [10,20,30,40,50]

# plt.plot(x,y)
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()  # This code creates a simple line plot using matplotlib. The x-axis values are [1, 2, 3, 4, 5] and the y-axis values are [10, 20, 30, 40, 50]. The plot is displayed with a title and labeled axes.

# names = ['Alice', 'Bob', 'Charlie', 'David']
# scores = [70, 80, 85, 90]

# plt.bar(names,scores,color = "blue")
# plt.title("Bar Plot of Scores")
# plt.xlabel("Names")
# plt.ylabel("Scores")
# plt.show()

# activities = ['Sleeping','Eating','Coding','Gaming']
# hours = [8,2,8,6]

# plt.pie(hours,labels=activities, autopct= '%1.1f%%')
# plt.title('Daily Activities')
# plt.show()

# ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

# plt.hist(ages, bins=5, color = 'blue')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

data = {
    "Year" : [2021,2022,2023],
    "Users" : [1500,2500,4000]
}

df = pd.DataFrame(data)

plt.plot(df["Year"], df["Users"],marker = 'o', color = "green")
plt.title("User Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()