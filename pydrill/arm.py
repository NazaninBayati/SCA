import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv("/home/nazanin/modified_DB_Ceph.csv", header=None, dtype="string")
num_records = len(store_data)
print(num_records)
records = []
for i in range(0, num_records):
    records.append([str(store_data.values[i, j])for j in range(0, 20)])

association_rules = apriori(records, min_support=0.005, min_confidence=0.20)
association_rules = list(association_rules)
print(len(association_rules))
print(association_rules)

