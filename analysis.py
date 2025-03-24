import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
df = pd.read_pickle('big_frame.pkl')
print(df.columns)

def parabola(x):
    return 1.952 * x**2 - 1.952 * x + 1.618


# Define the catenary function
def catenary(x, a, b, c):
    return a * np.cosh((x - c) / a) + b


# Define the catenary equation for the points
def equations(var_list):
    a_var = var_list[0]
    b_var = var_list[1]
    c_var = var_list[2]
    eq1 = a_var * np.cosh(-1*c_var / a_var) + b_var - 1.618  # From the point (0, 1.618)
    eq2 = a_var * np.cosh((0.5-c_var) / a_var) + b_var - 1.13  # From the point (0.5, 1.13)
    eq3 = a_var * np.cosh((1-c_var) / a_var) + b_var - 1.618  # From the point (1, 1.618)
    return [eq1
            ,eq2
            ,eq3
            ]

# Initial guess for a and b
initial_guess = [1, 1, 1]

# Solve the system of equations
a, b, c = fsolve(equations, initial_guess)

x_catenary = np.linspace(0, 1, 100)
y_catenary = catenary(x_catenary, a, b, c)

# Plot the catenary
plt.plot(x_catenary, y_catenary, label=f'Catenary: a={a:.3f}, b={b:.3f}, c={c:.3f}')

df_grouped = df.groupby(by='prob').mean()
df_grouped.reset_index(inplace=True)
print(df_grouped.head())
norm = plt.Normalize(df_grouped['n'].min(), df_grouped['n'].max())
cmap = plt.get_cmap('RdYlGn')
plt.scatter(x=df_grouped['prob'], y=df_grouped['nth_root'], c=df_grouped['n'], cmap=cmap, norm=norm, s=2)
plt.colorbar(label='Number of Terms Until Convergence')
plt.xlabel('Probability of Addition')
plt.ylabel('Approximate Growth Ratio')
plt.title("Approximate Growth Rates of Random Fibonacci Sequences")
# Generate x values for plotting the parabola (you can adjust the range and density)
x_parabola = np.linspace(min(df_grouped['prob']), max(df_grouped['prob']), 1000)

# Generate corresponding y values for the parabola
y_parabola = parabola(x_parabola)

# Plot the parabola
plt.plot(x_parabola, y_parabola, color='red', label='Parabola: $1.952x^2 - 1.952x + 1.618$')

plt.show()