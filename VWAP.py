#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:51:02 2021

@author: henburshtein
"""

import sys
sys.path.insert(1, '/Users/henburshtein/Downloads/twsapi_macunix.976.01/IBJts/source/pythonclient/ibapi/tickerspull/fundamentalpull')
import ta
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from contractstock import stock as s
import csv

df = yf.Ticker(s["symbol"]).history(period="max").reset_index()[["Date" , "Close" , "High", "Low", "Volume"]]


df['vwap'] = ta.volume.VolumeWeightedAveragePrice(df['High'], df['Low'], df['Close'], df['Volume']).volume_weighted_average_price()
df['vwap'].to_csv("vwap-aapl" + ".csv", sep=',')
print("done")
plt.plot(df["Date"],df["vwap"])
plt.show()