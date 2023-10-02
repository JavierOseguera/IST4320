from scipy.stats import poisson
import matplotlib.pyplot as plt

#generate Poisson distribution with sample size 5000
x = poisson.rvs(mu=7, size=5000)

#create plot of Poisson distribution
plt.hist(x, density=True, edgecolor='red')

print("Javier Oseguera Jr")
