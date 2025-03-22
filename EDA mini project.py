import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.dates import DateFormatter
import matplotlib.cm as cm



#import csv
df = pd.read_csv('/Users/hartnell/Desktop/hki_parking_spaces_eng.csv')
df2 = pd.read_csv('/Users/hartnell/Desktop/kln_parking_spaces_eng.csv')
df3 = pd.read_csv('/Users/hartnell/Desktop/nt_parking_spaces_eng.csv')

combined_df = pd.concat([df, df2, df3])
display(combined_df)
combined_df.to_csv('Parking_spaces_sum.csv', index = False)