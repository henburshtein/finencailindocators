#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:48:38 2021

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


df['ema'] = ta.trend.EMAIndicator(df['Close'], window = 14, fillna = False ).ema_indicator()
df['ema'].to_csv("ema-aapl" + ".csv", sep=',')
print("done")
plt.plot(df["Date"],df["ema"])
plt.show()
