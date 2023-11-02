import pandas as pd

file_path_name = "registered_user_count_ytd.csv"

df = pd.read_csv(file_path_name)

print(type(pd))

head = df.head(3)  # lookup top rows of your DataFrame

describe = df.describe()  # get statistical insight

view = df["close"]  # view a single column of data

print(head)
print(describe)
print(view)
