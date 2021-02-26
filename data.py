import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

flights_data = sns.load_dataset("flights")
res = flights_data.head()
print(res)

