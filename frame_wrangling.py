
import pandas as pd

df = pd.DataFrame(
    {"a" : [4 ,5, 6, 3],
     "b" : [7, 8, 9, 7],
     "c" : [10, 11, 12, 22],
     'g' : ['g1', 'g1', 'g2', 'g2']})
   # index = [1, 2, 3])

df.sor

df.groupby('g').fi


df[['a', 'b']]

df.drop('a', 2)

df = pd.DataFrame(
    {"a" : [4 ,5, 6, 3],
     "b" : [7, 8, 9, 7],
     "c" : [10, 11, 12, 22]})

pd.DataFrame(
    {"a" : [4 ,5, 6],
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]},
    index = [1, 2, 3])



a = ['g1', 'g1', 'g2', 'g2']

df[df['a'] > 4]
