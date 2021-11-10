#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:47:25 2021

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
df['ao'] = ta.momentum.AwesomeOscillatorIndicator(df['High'], df['Low'], window1 = 5, window2=34).awesome_oscillator()
df['ao'].to_csv("ao-aapl" + ".csv", sep=',')
print("done")
plt.plot(df["Date"],df["ao"])
plt.show()