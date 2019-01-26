
#%%
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 2, 5, 4])
plt.show()

plt.plot([0, 1, 2, 4, 8])
plt.show()

x = [1, 5, 3, 2, 7, 4]
y = [1, 2, 5, 0, 6, 2]
plt.plot(x, y)
plt.show()

xs, ys = zip(*sorted(zip(x, y)))
plt.plot(xs, ys)
plt.show()

#%%
import numpy as np
x = np.linspace(-1, 1, 100)
y = x ** 2
plt.plot(x, y)
plt.show()

x1 = np.linspace(-1, 1, 100)
y1 = x1 ** 2
x2 = np.linspace(0, 1, 50)
y2 = x2 ** 0.5

plt.figure(figsize=(5, 3))
plt.plot(x1, y1, lw=3, color='g', alpha=0.6, ls='', marker='o')
plt.plot(x2, y2, lw=3, color='b', alpha=0.6, ls='-', marker='s')
plt.plot(x2, x2, lw=3, color='r', alpha=0.6, ls='', marker='v')
plt.show()

#%%
x=np.random.normal(0,1,1000)
plt.hist(x)
plt.show()
y=np.random.normal(0,1,1000)
plt.scatter(x,y)
plt.show

#%%
plt.style.use('ggplot')
x=np.random.normal(0,1,1000)
plt.hist(x)
plt.show()

#### Radar plot
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

data = pd.read_csv('cities_ranking.csv')
data.head()
data


