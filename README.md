# MonteCarlo_MBG_AsianOption

This Python script provides a Monte Carlo simulation framework to evaluate **Asian options** using **Geometric Brownian Motion (GBM)** trajectories. It supports both **average strike** and **average price** Asian options and includes an analysis of how **volatility** affects the option price.

---

## 💡 What Are Asian Options?

Asian options are financial derivatives where the payoff depends on the **average price** of the underlying asset over a certain period, rather than the price at a specific date. They come in two main types:

- **Average Price Asian Option**: Payoff depends on the average of the asset prices.
- **Average Strike Asian Option**: Payoff depends on the average strike calculated from asset prices.

These options reduce the risk of market manipulation and are less volatile than standard European options.

---

## 🧮 What the Script Does

### ✅ 1. Simulates GBM Price Paths

- Uses the Monte Carlo method to simulate multiple price trajectories of the underlying asset.
- Follows the Geometric Brownian Motion (GBM) model:
  
  \[
  dS_t = \mu S_t dt + \sigma S_t dW_t
  \]

### ✅ 2. Calculates Asian Option Prices

- Computes the payoff for both **Average Price** and **Average Strike** options across all simulated paths.
- Uses the **risk-neutral pricing approach** by discounting expected payoffs at the risk-free rate.

### ✅ 3. Analyzes Volatility Impact

- Runs the simulation across a range of volatility values.
- Plots how the option price varies with increasing volatility.

---

## 📈 Example Outputs


[**Click here to view the Result Study**](https://github.com/fr-cm/MonteCarlo_MBG_AsianOption/blob/main/Result_MMF_FC.pdf)


---

![chat_1](https://raw.githubusercontent.com/fr-cm/MonteCarlo_MBG_AsianOption/refs/heads/main/Img/chart.png) ![chart_2](https://raw.githubusercontent.com/fr-cm/MonteCarlo_MBG_AsianOption/refs/heads/main/Img/chart1.png)

---
![Data](https://raw.githubusercontent.com/fr-cm/MonteCarlo_MBG_AsianOption/refs/heads/main/Img/data.png)


- Final estimated prices for each type of Asian option.
- Graph showing the relationship between volatility and option price.

---


