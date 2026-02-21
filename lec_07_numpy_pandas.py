import numpy as np
import pandas as pd

data = np.array([1,2,3,4,5])

print("Original Array: ",data)
print("Multiply Array: ",data*2)
print("Sum of Arrays: ",np.sum(data))



data={
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,35],
    "Salary":[50000,70000,60000]
}

df=pd.DataFrame(data)
print("\nData Frame")
print(df)

print("\nNames Column: ",df["Name"].tolist())
print("\nFirst Row\n",df.iloc[0])