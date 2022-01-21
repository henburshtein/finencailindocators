#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:13:11 2021

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

df['rsi'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
df['rsi'].to_csv("rsi-aapl" + ".csv", sep=',')
print("done")

plt.plot(df["Date"],df["rsi"])
plt.show()

df['ao'] = ta.momentum.AwesomeOscillatorIndicator(df['High'], df['Low'], window1 = 5, window2=34).awesome_oscillator()
df['ao'].to_csv("ao-aapl" + ".csv", sep=',')
print("done")
plt.plot(df["Date"],df["ao"])
plt.show()
