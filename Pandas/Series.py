import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index = ['a', 'b', 'c', 'd'])
print(data['b'])
print('a' in data)
print(data.keys())
print(list(data.items()))
print(data)
data['e'] = 1.25
print(data)
print(data['a':'c'])
print(data[0:2])
print(data[(data > 0.3) & (data < 0.8)])