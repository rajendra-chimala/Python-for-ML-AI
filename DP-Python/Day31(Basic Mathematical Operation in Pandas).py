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
print("Mean\n",df.mean())
print("Median\n",df.median())
print("Standard Diviation \n",df.std())
print(df.min())
print(df.max())

