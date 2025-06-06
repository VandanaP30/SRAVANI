import numpy as np

def normal_dist(x, mean, sd):
    prob_density = (1 / (np.sqrt(2 * np.pi) * sd)) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    return prob_density

# Example values
mean = 0
sd = 1
x = 1

result = normal_dist(x, mean, sd)
print(result)
