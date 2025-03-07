import pandas as pd
df = pd.read_csv("apple_products.csv")
print(df.head())
print(df.head(12))
print(df.count())
print(df['Mrp'].max())
print(df['Mrp'].min())
print(df[df['Mrp'] == 149900])
print(df[df['Mrp'] == 39900])
print(df[df['Mrp'] <= 39900])
print(df[df['Mrp'] <= 50000])
print(df[df['Mrp'] >= 100000])
print(df['Product Name'])
print(type(df['Product Name']))
print(list(df['Product Name']))
print(df['Product Name'])
print(df['Product Name'][53])
print(df['Product Name'][53].upper())
print(df['Product Name'][53].lower())
print(df['Product Name'][51][6:15].lower())
print(df['Product Name'][51][6:15].upper().strip())
df['Model Name'] = df['Product Name'].str[6:15]
print(df['Model Name'].head())
print(df['Model Name'].head(12))
print(df.sort_values(by=['Star Rating'], ascending=True))
print(df.sort_values(by=['Star Rating'], ascending=False))
