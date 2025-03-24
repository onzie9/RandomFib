import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import matplotlib.colors as mcolors


def safe_divide(x: float, y: float) -> float:
    if y != 0:
        return x/y
    else:
        return -99


def rand_fib(prob: float,
             num_trials: int = 100,
             seed0: float = 0,
             seed1: float = 1,
             conv_tol: float = .01,
             conv_len: int = 7,
             conv_min: int=50) -> list:
    convergent_successes = [False]*(conv_len-2)
    conv_check = [0]*conv_len
    for n in range(num_trials):
        if n < conv_len:
            conv_check[n] = seed0
        else:
            conv_check = conv_check[1:] + conv_check[0:1]
            conv_check[-1] = seed0
        s = int(np.random.choice(np.array([1, -1]), p=[prob, 1 - prob]))
        next_num = seed0 + s*seed1
        seed0 = seed1
        seed1 = next_num
        if n > conv_min:
            for i in range(conv_len-2):
                if abs(abs(safe_divide(conv_check[i+1],conv_check[i])) -
                       abs(safe_divide(conv_check[i+2],conv_check[i+1]))) < conv_tol:
                    convergent_successes[i] = True
                else:
                    convergent_successes[i] = False
                    break

            if all(convergent_successes):
                return [n, abs(conv_check[-1])**(1/n)]

    return [False, False]



print(rand_fib(.5, num_trials=500, conv_len=6, conv_tol=.05, seed0=0, seed1=1))
data = []
for x in range(100000):
    p = round(random.random(),3)
    n = 1000
    f = rand_fib(p, n, conv_len=6, conv_tol=.005, conv_min=100)
    if f[1]:
        data.append([p, f[1], f[0]])

df = pd.DataFrame(columns=['prob', 'nth_root', 'n'], data=data)
norm = plt.Normalize(df['n'].min(), df['n'].max())
cmap = plt.get_cmap('RdYlGn')
plt.scatter(x=df['prob'], y=df['nth_root'], c=df['n'], cmap=cmap, norm=norm, s=2)
plt.colorbar(label='Number of Terms Until Convergence')
plt.xlabel('Probability of Addition')
plt.ylabel('Approximate Growth Ratio')
plt.title("Approximate Growth Rates of Random Fibonacci Sequences")
plt.show()

df.to_pickle('big_frame.pkl')
