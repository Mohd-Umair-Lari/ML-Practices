import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.get_dummies(pd.read_csv("LOCATION/iris.csv").apply(lambda x: pd.cut(x, 3) if x.dtype != 'O' else x))
freq = apriori(df, min_support=0.2, use_colnames=True)
print(association_rules(freq, metric="confidence", min_threshold=0.3))