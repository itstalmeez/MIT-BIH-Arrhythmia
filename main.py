import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("MIT-BIH Arrhythmia Database.csv")
print(df.describe)
print(df.info)
print(df.isnull().sum())

columns_to_plot = [
    'record', 'type', '0_pre-RR', '0_post-RR', '0_pPeak', '0_tPeak', '0_rPeak', '0_sPeak', '0_qPeak',
    '0_qrs_interval', '0_pq_interval', '0_qt_interval', '0_st_interval', '0_qrs_morph0', '0_qrs_morph1',
    '0_qrs_morph2', '0_qrs_morph3', '0_qrs_morph4', '1_pre-RR', '1_post-RR', '1_pPeak', '1_tPeak', '1_rPeak',
    '1_sPeak', '1_qPeak', '1_qrs_interval', '1_pq_interval', '1_qt_interval', '1_st_interval', '1_qrs_morph0',
    '1_qrs_morph1', '1_qrs_morph2', '1_qrs_morph3', '1_qrs_morph4'
]

# Plot histograms for each selected column
plt.figure(figsize=(15, 20))

for i, column in enumerate(columns_to_plot, 1):
    plt.subplot(7, 5, i)
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()