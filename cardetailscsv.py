from os import replace

from pandas.core.frame import DataFrame
import numpy as np
import random
import pandas as pd

car_manuf_model = np.random.randint(100,300, size=(100,1))
list = ['Y', 'N']
model_data = pd.DataFrame({'Cubic Capacity': np.random.choice(range(100,150), 100, replace=True),
                            'EnginePerformance': np.random.choice(range(1,5), 100, replace=True),
                                'Hybrid Engine': random.choices(list, k=100)})

model_data.to_csv("car_details.csv", index=False)
data = pd.read_csv("car_details.csv")

x = data.iloc[:,0].values
y = data.iloc[:,1].values
for i in range(49,100):
    x[i] = np.random.choice(range(130,200))

for i in range(49,100):
    y[i] = np.random.choice(range(3,10))

print(x)
print(y)

data.to_csv("car_details.csv", index=False)