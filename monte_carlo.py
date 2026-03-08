import yfinance as yf
import numpy as np

#INPUT needed to run the script
ticker   = input("Enter stock ticker: ").upper().strip() #Stock Ticker (AAPL for Apple)
horizon  = int(input("Simulation horizon in days: ")) #days are counted only when the stock market is open (252 days = 1 year)
n_paths  = 10_000 #10 000 paths to simulate 

#Fetching the data & compute parameters 
data        = yf.download(ticker, period="2y", auto_adjust=True, progress=False) #last two years of data and auto adjust if company uses stock splits and dividends
prices      = data["Close"].squeeze()
log_returns = np.log(prices / prices.shift(1)).dropna() #logarithmic returns because they are more mathematically correct

S0    = float(prices.iloc[-1]) #most recent closing price
sigma = float(log_returns.tail(252).std() * np.sqrt(252))   # annualised 252-day volatility
mu    = 0.053                                                 # risk-free rate (update as needed) 

#Geometric Brownian Motion Monte Carlo 

#A drift — the stock tends to grow at rate μ over time
#Random noise — each day the price gets a random shock up or down
#

dt            = 1 / 252 #one trading day
Z             = np.random.standard_normal((horizon, n_paths)) #A matrix of random numbers from a standard normal distribution

#formula for Geometric Brownian Motion
daily_factors = np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z) 

paths         = np.vstack([np.full(n_paths, S0), daily_factors]).cumprod(axis=0) #build of price paths

final_prices  = paths[-1] #final prices prediction

#Results 
print(f"\n{'─'*40}")
print(f"  {ticker} — Monte Carlo ({n_paths:,} paths, {horizon}d)")
print(f"{'─'*40}")
print(f"  Current price   : ${S0:.2f}")
print(f"  σ (annual vol)  : {sigma:.1%}")
print(f"  μ (drift)       : {mu:.1%}  [risk-free rate]")
print(f"{'─'*40}")
print(f"  Expected price  : ${final_prices.mean():.2f}")
print(f"  Downside  (5%)  : ${np.percentile(final_prices,  5):.2f}")
print(f"  Median   (50%)  : ${np.percentile(final_prices, 50):.2f}")
print(f"  Upside   (95%)  : ${np.percentile(final_prices, 95):.2f}")
print(f"  Prob of gain    : {(final_prices > S0).mean():.1%}")
print(f"  Std deviation   : ${final_prices.std():.2f}")
print(f"{'─'*40}\n")

