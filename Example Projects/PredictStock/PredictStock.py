import os
import random as ran
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")

#Main
data = pd.read_csv('/home/victor/Documents/Code/Projects/Example/PredictStock/Stocks2013-2018.csv', delimiter = ',', on_bad_lines = 'skip')
data['date'] = pd.to_datetime(data['date'])

data.info()

companies = ['AAPL', 'AMD', 'FB', 'GOOGL', 'AMZN', 'NVDA', 'EBAY', 'CSCO', 'IBM']

plt.figure(figsize = (15,8))
for index, company in enumerate(companies, 1):
    plt.subplot(3, 3, index)
    c = data[data['Name'] == company]
    plt.plot(c['date'], c['close'], c = "r", label = "close", marker = "^")
    plt.plot(c['date'], c['open'], c = "g", label = "open", marker = "^")
    plt.title(company)
    plt.legend()
    plt.tight_layout()

plt.figure(figsize=(15, 8))
for index, company in enumerate(companies, 1):
    plt.subplot(3, 3, index)
    c = data[data['Name'] == company]
    plt.plot(c['date'], c['volume'], c='purple', marker='*')
    plt.title(f"{company} Volume")
    plt.tight_layout()

plt.show()


Nvidia = data[data['Name'] == 'NVDA']
pred_range = Nvidia.loc[(Nvidia['date'] > datetime(2013, 1, 1)) & (Nvidia['date'] < datetime(2018, 1, 1))]
plt.plot(Nvidia["date"], Nvidia['close'])
plt.xlabel("Date")
plt.ylabel("Close")
plt.title("Nvidia Stock Prices")
plt.show()