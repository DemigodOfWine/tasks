import numpy as np
import matplotlib.pyplot as plt
a = 5
b = 5
L = 5

N = np.random.randint(2, size=[a, b], dtype=int)
np.fill_diagonal(N, 0)
N = np.tril(N) + np.tril(N, -1).T
print(N)

fig, ax = plt.subplots()
naming = []
for _ in range(L):
    naming.append(np.random.randint(np.size(N), size=2, dtype=int))

print(naming)
for label, dot in enumerate(naming):
    ax.add_patch(plt.Circle(tuple(dot), L/4, facecolor='#9ebcda', alpha=0.8))
    plt.text(dot[0], dot[1], label)

ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

[i_true, j_true] = np.where(N == True)

for i in range(len(i_true)):
    a = naming[i_true[i]]
    b = naming[j_true[i]]
    plt.plot([naming[i_true[i]][0], naming[j_true[i]][0]],
             [naming[i_true[i]][1], naming[j_true[i]][1]])


plt.plot()
plt.show()



