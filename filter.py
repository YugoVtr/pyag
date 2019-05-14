# https://openflights.org/data.html
import pandas as pd

df = pd.read_csv('airports.dat', header=None, sep=',')
brIATA = [ 'BEL','CNF','BSB','CFB','VCP','CGR','CGB','CWB','FLN','FOR','IGU','GRU','MCZ','MAO','NAT','POA','REC','GIG','SSA','QSC']
filtered = df[4].isin(brIATA)
df = df[filtered] 
df.iloc[:, [2,6,7]].to_csv("out.csv", index=False, header=False) 
