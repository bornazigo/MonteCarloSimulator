# MonteCarloSimulator
This is a simple Monte Carlo Simulator using Geometric Brownian Motion to predict the US stock market. 

A Python script that simulates thousands of possible future stock price paths using Geometric Brownian Motion (GBM) and outputs key risk and return statistics.

The script:
1. Downloads 2 years of real price data from Yahoo Finance 
2. Estimates the stock's volatility from that data
3. Simulates 10,000 possible future price paths
4. Reports where the price could realistically end up

The future price of a stock is unknown, but using the Monte Carlo simulation we simulate a lot of cases to make aproximations and use it to solve a problem.

Each simulation is one possible future — the stock goes up some days, down others, all randomly. I decided to use 10,000 of them to get a realistic picture of the full range of outcomes. 

