#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 04:37:44 2021

@author: henburshtein
"""

import sys
import ta
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from contractstock import stock as s
import csv

df = yf.Ticker(s["symbol"]).history(period="max").reset_index()[["Date" , "Close" , "High", "Low", "Volume"]]

df['obv'] = ta.volume.OnBalanceVolumeIndicator(df['Close'], df['Volume'], fillna = False).on_balance_volume()
df['obv'].to_csv("obv-aapl" + ".csv", sep=',')
print("done")

plt.plot(df["Date"],df["obv"])
plt.show()
