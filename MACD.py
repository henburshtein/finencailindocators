#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:01:12 2021

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

df = yf.Ticker(s["symbol"]).history(period="max").reset_index()[["Date" , "Close" , "High", "Low"]]


df['macd'] = ta.trend.MACD(df['Close'], window_slow = 26, window_fast = 12, window_sign = 9).macd()
df['diff'] = ta.trend.MACD(df['Close'], window_slow = 26, window_fast = 12, window_sign = 9).macd_diff()
df['signal'] = ta.trend.MACD(df['Close'], window_slow = 26, window_fast = 12, window_sign = 9).macd_signal()

df['macd'].to_csv("macd-aapl" + ".csv", sep=',')
df['diff'].to_csv("macd-diff-aapl" + ".csv", sep=',')
df['signal'].to_csv("macd-signal-aapl" + ".csv", sep=',')

print("done")
plt.plot(df["Date"],df["macd"])
plt.plot(df["Date"],df["signal"])
plt.plot(df["Date"],df["diff"])
plt.show()
