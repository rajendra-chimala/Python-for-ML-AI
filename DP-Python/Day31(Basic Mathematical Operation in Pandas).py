import pandas as pd

data = {
"A": [10 , 20 , 30 , 40] ,
"B": [5 , 15 , 25 , 35] ,
"C": [2 , 4 , 6 , 8]
}



df = pd.DataFrame(data)

# print(df)


# 4 Basic Arithmetic Operations

# df["Sum of A and B"] = df["A"]+df["B"]

# print("Sum of A and B:")
# print(df["Sum of A and B"])


# df["Subtraction of A and B"] = df["A"]-df["B"]
# print("\nSubtraction of A and B:")
# print(df["Subtraction of A and B"])


# df["Multiplication of A and B"] = df["A"]*df["B"]
# print("\nMultiplication of A and B:")
# print(df["Multiplication of A and B"])


# df["Division of A and B"] = df["A"]/df["B"]
# print("\nDivision of A and B:")
# print(df["Division of A and B"])



# Descriptive Statistics
# print("Mean\n",df.mean())
# print("Median\n",df.median())
# print("Standard Diviation \n",df.std())
# print(df.min())
# print(df.max())


#  Element-wise Mathematical Functions
import numpy as np

# df["Square of A"] = np.square(df["A"])
# print("\nSquare of A:")
# print(df["Square of A"])


# df["Square Root of B"] = np.sqrt(df["B"])
# print("\nSquare Root of B:")    
# print(df["Square Root of B"])


# df["Log of A"] = np.log(df["A"])
# print("\nLog of A:")
# print(df["Log of A"])


# df["Exponential of A"] = np.exp(df["A"])
# print("\nExponential of A:")
# print(df["Exponential of A"])


#  Applying Functions with apply()


# def double(x):
#     return x * 2

# df["Square of C"] = df["C"].apply(double)
# print("\nSquare of C:")
# print(df["Square of C"])


#  Column-wise and Row-wise Operations

df [" row_sum "] = df .sum ( axis =1)
# Sum across rows (column - wise )
col_sum = df .sum ( axis =0)
print ( df )
print ("Column - wise sum :\n", col_sum )