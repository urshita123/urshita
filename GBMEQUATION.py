import matplotlib.pyplot as plt
import numpy as np

#mu=drift factor for gbm equation
#sigma: volatility rate
#t: time span
#dt: lenght of steps
#S0: Stock Price in t=0
#W: Brownian Motion with Drift N[0,1]

def main():
  t = 2 #assigning values
  mu = 0.1
  sigma = 0.01
  S0 = 20
  dt = 0.01
  N = round(T / dt)
  t = np.linspace(0, T, N)
  W = np.random.standard_normal(size = N)
  W = np.cumsum(W)*np.sqrt(dt) # standard brownian motion
  X = (mu-0.5*sigma**2)*t + sigma*W
  S = S0*np.exp(X) # geometric brownian motion
  plt.plot(t, S) #plots time against stock price
  plt.show() #shows plot

if __name__ == '__main__':
    main()