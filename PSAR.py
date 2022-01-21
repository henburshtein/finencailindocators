#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:43:32 2021

@author: henburshtein
"""

import sys
import ta
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from contractstock import stock as s
import csv

df = yf.Ticker(s["symbol"]).history(period="max").reset_index()[["Date" , "Close" , "High", "Low"]]


df['psar'] = ta.trend.PSARIndicator(df['High'], df['Low'], df['Close'], step = 0.02, max_step = 0.2).psar()
df['psar'].to_csv("psar-aapl" + ".csv", sep=',')
print("done")
plt.plot(df["Date"],df["psar"])
plt.show()
