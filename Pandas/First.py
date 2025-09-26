import pandas as pd
Customer={
    "cstmr_name":["Arjun","Anurag","Archana","Priyanshu","Akash"],
    "cstmr_age":[54,65,13,54,65],
    "cstmr_address":["Jaunpur","Agra","Mujaffarpur","Patna","Jaunpur"],
    "cstmr_gender":["M","M","F","M","M"]
}
Dtf=pd.DataFrame(Customer)
Dtf.to_csv("output.csv",index=False)

# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df)

# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.head)
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.tail())
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.sample())
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.shape)
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.info())
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.describe())
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.dtypes)
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.columns)
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df. index)
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df. values)
# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.loc[:])

# import pandas as pd

# df = pd.read_csv( r"D:\pytho\interview\Details.csv")

# print(df.sample(10))
 
# import pandas as pd

# # Create a proper dictionary structure for the DataFrame
# Customer = {
#     'Index': [95, 439, 773, 892, 1202, 317, 1472, 1456, 566, 1497],
#     'Customer_ID': ['B-25704', 'B-25998', 'B-25843', 'B-25603', 'B-25909', 'B-26016', 'B-25707', 'B-25989', 'B-25712', 'B-25973'],
#     'Amount': [126, 50, 45, 180, 168, 429, 8, 10, 193, 4141],
#     'Profit': [-63, -28, 0, 5, 56, 61, -6, 5, -275, 1698],
#     'Quantity': [3, 5, 2, 3, 3, 3, 1, 1, 3, 13],
#     'Category': ['Electronics', 'Furniture', 'Clothing', 'Clothing', 'Clothing', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Electronics'],
#     'Sub_Category': ['Accessories', 'Furnishings', 'Stole', 'Trousers', 'Saree', 'Electronic Games', 'Stole', 'Stole', 'Phones', 'Printers'],
#     'Payment_Method': ['UPI', 'COD', 'UPI', 'Debit Card', 'COD', 'Credit Card', 'COD', 'COD', 'Credit Card', 'COD']
# }

# # Create DataFrame from the dictionary
# Dtf = pd.DataFrame(Customer)

# # Save to CSV file
# Dtf.to_csv(r"D:\pytho\interview\panda\output.csv", index=False)

# # Display the DataFrame
# print("DataFrame created successfully:")
# print(Dtf)
 
import pandas as pd
df = pd.read_csv(r"D:\pytho\interview\panda\output.csv")
print(df.isnull().sum())
print(df.dropna().isnull().sum())