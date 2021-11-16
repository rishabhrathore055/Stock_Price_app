import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price application
Shown are the stock closing price and volume of Google!
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.title("Closeing Graphs")
st.line_chart(tickerDf.Close)
st.title("Volumes Graphs")
st.line_chart(tickerDf.Volume)