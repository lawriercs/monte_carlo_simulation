# __Stock Price Prediction Using Monte Carlo Simulation__ 

This Python script simulates future stock prices over a 1-year horizon using a Monte Carlo Simulation based on Geometric Brownian Motion. It pulls historical data to estimate market parameters (drift and volatility) and provides both probabilistic metrics and visual representations of potential future outcomes.

## Description

This project is a quantitative financial analysis tool designed to simulate and evaluate potential future price trajectories for public equities using stochastic modeling. By retrieving historical data via the Yahoo Finance API, the script calculates localized market parameters: annualized drift (the asset's directional momentum) and annualized volatility (the magnitude of its price fluctuations). These metrics are then used to drive a Geometric Brownian Motion algorithm, executing 10,000 parallel random-walk simulations across a 252-day trading horizon.

Rather than relying on a fragile, single-point price prediction, the true utility of this project lies in its probabilistic framework for risk management and decision-support. By mapping thousands of distinct outcomes, it constructs a comprehensive terminal distribution that allows investors and analysts to quantify the exact mathematical probability of capital appreciation versus severe downside risk. Furthermore, by integrating a 95% Value at Risk (VaR) metric, the project explicitly calculates the maximum expected loss under normal market conditions, transforming raw historical volatility into actionable insight for portfolio optimization, hedging strategies, and risk tolerance assessment.

## Getting Started

### Dependencies

This project relies on the following standard Python data science libraries:
1. yfinance: Connects to the Yahoo Finance API to fetch live and historical market data.
2. numpy: Handles the heavy mathematical lifting, generating the 10,000 random-walk arrays simultaneously.
3. pandas: Manages the historical data dataframes and calculates daily log returns.
4. matplotlib: Generates the dual-panel plots for the simulated paths and terminal distribution.

These can all be installed using the following line of code:
``` python
pip install -r requirements.txt
```

### Executing the program

To run the simulation of your chosen stock, scroll to the bottom of the script and replace the argument in the function:
``` python
monte_carlo_simulation("MSFT")
```
with your chosen ticker.
