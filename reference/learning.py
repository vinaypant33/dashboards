import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



import plotly.express as px

database_name  = sns.get_dataset_names()

print(database_name)


df  = sns.load_dataset('tips')

df.head()