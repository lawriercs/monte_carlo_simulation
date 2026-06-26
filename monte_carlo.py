def monte_carlo_simulation(ticker):
    """
    This function performs a Monte Carlo simulation to predict the future stock price of TSLA
    over a 1-year period using historical data to estimate drift and volatility.
    """
    import numpy as np
    import pandas as pd
    import yfinance as yf
    import matplotlib.pyplot as plt

    # 1. Fetch historical data to calculate actual drift and volatility
    print("Fetching market data...")
    df = yf.download(ticker, start="2025-01-01", end="2026-01-01")

    # Calculate daily log returns
    df['Returns'] = np.log(df['Close'] / df['Close'].shift(1))

    # Annualize the parameters (252 trading days in a year)
    mu = (df['Returns'].mean() * 252) + (0.5 * sigma**2)
    sigma = df['Returns'].std() * np.sqrt(252)
    S0 = float(df['Close'].values.flatten()[-1]) # Use the last available stock price as starting point

    print(f"Starting Price (S0): ${S0:.2f}")
    print(f"Annual Drift (mu): {mu:.4f}")
    print(f"Annual Volatility (sigma): {sigma:.4f}")


    # 2. Monte Carlo Setup
    T = 1.0          # Time horizon (1 year)
    M = 252          # Number of time steps (trading days)
    N = 10000        # Number of simulated paths
    dt = T / M       # Time step size

    # Create an array to hold all simulated paths (rows = days, columns = simulated paths)
    paths = np.zeros((M + 1, N))
    paths[0] = S0    # Every path starts at the current stock price

    # 3. Simulate the paths using Geometric Brownian Motion
    for t in range(1, M + 1):
        # Draw N random normal numbers (one for each path)
        epsilon = np.random.standard_normal(N)
    
        # Calculate the next day's price for all N paths at once
        paths[t] = paths[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * epsilon * np.sqrt(dt))

    print(f"\nSimulation complete! Generated {N} paths.")
    print(f"Average predicted price in 1 year: ${np.mean(paths[-1]):.2f}")
    print(f"Average price return range in 1 year: ${(np.mean(paths[-1])-S0):.2f}")
    print(f"Probability of price increase: {np.mean(paths[-1] > S0) * 100:.2f}%")

    # 4. Visualize the results
    plt.figure(figsize=(12, 6))
    plt.plot(paths[:, :100], alpha=0.1, color='blue')  # Plot first 100 paths
    plt.xlabel('Trading Days')
    plt.ylabel('Stock Price ($)')
    plt.title(f'Monte Carlo Simulation: {ticker} Stock Price Paths')
    plt.grid(True)
    plt.show()

monte_carlo_simulation("AMD")