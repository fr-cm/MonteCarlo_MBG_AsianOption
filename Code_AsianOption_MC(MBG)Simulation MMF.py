import numpy as np
import pandas as pd

#  per il generatore di numeri casuali
np.random.seed(42)
# Parametri iniziali
S0 = 100  # Prezzo iniziale del sottostante
K = 100  # Prezzo di esercizio (strike price)
T = 1   # Tempo fino alla scadenza (in anni)
r = 0.03662  # Tasso di interesse senza rischio Gennaio 2023 fonte https://www.bancaditalia.it/compiti/operazioni-mef/rendistato-rendiob/documenti/rendistato-2023.pdf
volatilità = [0.1, 0.2, 0.3, 0.4, 0.5]  # Diversi livelli di volatilità
n_simulazioni = [100, 10000, 1000000]  # Numero di simulazioni
n_passi = 365  # Numero di passi temporali (giorni)
dt = T / n_passi  # Intervallo di tempo
intervallo_confidenza = 0.95  # Livello di confidenza per l'intervallo di confidenza

#Simulazione montecarlo
def monte_carlo_simulation(S0, K, T, r, sigma, n_simulazioni, n_passi, dt, tipologia_opzione="average_price"):

    payoffs = []

    for _ in range(n_simulazioni):
        S = S0 #inizializzazione prezzo
        prices = [S0]
        # simulazione moto Browniano geometrico
        for _ in range(n_passi):
            dW = np.random.normal(0, np.sqrt(dt))
            S = S * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * dW)
            prices.append(S)

        average_price = np.mean(prices)
        if tipologia_opzione == "average_price":
            payoff = max(average_price - K, 0) #payoff call average price
        elif tipologia_opzione == "average_strike":
            payoff = max(S - average_price, 0) #payoff call average strike
        payoffs.append(payoff)

    prezzo_medio = np.exp(-r * T) * np.mean(payoffs)
    dev_standard = np.std(payoffs)
    intervallo_confidenza = (prezzo_medio - 1.96 * dev_standard / np.sqrt(n_simulazioni),
                             prezzo_medio + 1.96 * dev_standard / np.sqrt(n_simulazioni))

    return prezzo_medio, intervallo_confidenza


#ciclo for per avere subito la stringa di output della simulazione
#for sigma in volatilità:
#    for n_sim in n_simulazioni:
#       for tipologia_opzione in ["average_price", "average_strike"]:
#                prezzo_medio, intervallo_confidenza = monte_carlo_simulation(S0, K, T, r, sigma, n_sim, n_passi, dt, tipologia_opzione)
#                print(f"Volatilità: {sigma}, Opzione call {tipologia_opzione}, Numero di simulazioni: {n_sim}")
#           print(f"Prezzo medio: {prezzo_medio}, Intervallo di confidenza: {intervallo_confidenza}\n")

# Crea un DataFrame vuoto
data_columns = ['Volatilità', 'Tipo Opzione', 'Numero di Simulazioni', 'Prezzo Medio', 'Intervallo di Confidenza']
df = pd.DataFrame(columns=data_columns)

#simulazione per per i 2 tipi di opzioni e i numeri di simulazioni
for sigma in volatilità:
    for n_sim in n_simulazioni:
        for tipologia_opzione in ["average_price", "average_strike"]:
            prezzo_medio, intervallo_confidenza = monte_carlo_simulation(S0, K, T, r, sigma, n_sim, n_passi, dt,
                                                                         tipologia_opzione)

            # Crea un dizionario con i dati della simulazione corrente
            data_row = {'Volatilità': sigma,
                        'Tipo Opzione': tipologia_opzione,
                        'Numero di Simulazioni': n_sim,
                        'Prezzo Medio': prezzo_medio,
                        'Intervallo di Confidenza': intervallo_confidenza}
            df.loc[len(df)] = data_row

print(df.to_string())

