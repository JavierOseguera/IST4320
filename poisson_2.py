from scipy.stats import poisson
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
avg = 2

poisson_pd = poisson.pmf(X, avg)

#Plot

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, poisson_pd, 'bo', ms=8, label='poisson pmf')

ax.vlines(X, 0, poisson_pd, colors='b', lw=5, alpha=0.5)

print("Javier Oseguera Jr.")
