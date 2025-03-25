#used to analyze data.
#bigreko data milauna use hunchha pandas.
# data frame / tabular format
#index aafai aaucha ani kunai line hatayo bhaney index update hudaina, jasto thyo testai aaucha.

# #new data file with no empty cells.
# import pandas as pd  #(pandas will act as pd)
# df = pd.read_csv("/Users/bhuwanthapa/Downloads/broadwaypython/pandas.csv")
# # print(df)
# new_df = df.dropna() #run garda chei hatako but actual file bata chei hatako chhaina.
# print(new_df.to_string()) #returns the data by removing the entire row junma NaN thyo.
# print(new_df) # returns updated data 
# print(df) # returns the old data
#  #purano mei update garna cheii:
# import pandas as pd  #(pandas will act as pd)
# df = pd.read_csv("/Users/bhuwanthapa/Downloads/broadwaypython/pandas.csv")
# df.dropna(inplace = True)
# print(new_df.to_string())

# #replace null values with the number 130:
# import pandas as pd
# df = pd.read_csv("/Users/bhuwanthapa/Downloads/broadwaypython/pandas_file.csv")
# df.fillna(130, inplace = True) #naya variable nabanai tyei old data ma update garna we use inplace = True

# #replace null values in certail "column" with the number 130:
# import pandas as pd
# df = pd.read_csv("/Users/bhuwanthapa/Downloads/broadwaypython/pandas_file.csv")
# df["Calories"].fillna(130, inplace = True)
# print(df)

# #mean of the int ( date doesn't count)
# import pandas as pd
# df = pd.read_csv("/Users/bhuwanthapa/Downloads/broadwaypython/pandas_file.csv")
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)
# print(df)

import pandas as pd
df = pd.read_csv("/Users/bhuwanthapa/Downloads/broadwaypython/pandas_file.csv")
df.dropna(inplace = True)
df["Date"] = pd.to_datetime(df["Date"], format = "mixed")
print(df)

