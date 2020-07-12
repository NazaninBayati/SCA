import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

temp = []

store_data = pd.read_csv("/home/nazanin/modified_DB_Ceph_summary.csv", header=None, dtype="string")
dataset = store_data.values.tolist()


#data cleaning
for m in range(len(dataset)):
    temp = dataset[m]
    for n in range(len(dataset[m])):
        if str(dataset[m][n] ) == '<NA>':
            counter = n
            dataset[m] = temp[0:n]
            break
print(dataset)

association_rules = apriori(dataset, min_support=0.005, min_confidence=0.20)
association_rules = list(association_rules)
print(len(association_rules))
print(association_rules)
