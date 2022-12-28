import pandas as pd
df1=pd.read_excel('c1_new.xlsx')
df2=pd.read_excel('c2.xlsx')
df1.equals(df2)
comparison_values = df1.values == df2.values
print (comparison_values)
import numpy as np
rows,cols=np.where(comparison_values==False)
for item in zip(rows,cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])

df1.to_excel('./Excel_diff.xlsx',index=False,header=True)