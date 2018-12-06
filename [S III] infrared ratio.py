# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.3
# ---

import numpy as np
import pyneb as pn

s3 = pn.Atom('S', 3)

s3.lineList


# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("talk")

s3.plotEmiss()

densities = np.logspace(0.0, 6.0)


em = s3.getEmissivity(1.e4, densities)
em.shape

s3.getTransition('33.47m'), s3.getTransition('18.71m')

fig, ax = plt.subplots(figsize=(12, 6))
for T in 5000, 1e4, 2e4:
    em33 = s3.getEmissivity(T, densities, 2, 1)
    em18 = s3.getEmissivity(T, densities, 3, 2)
    ax.plot(densities, em33/em18, label=f"$T = {T:.0f}$ K")
ax.legend()
ax.set(
    xscale='log', yscale='linear',
    xlabel="Density, $\mathrm{cm}^{-3}$",
    ylabel="[S III] 33.47 $\mu$m / 18.71 $\mu$m",
)
fig.savefig("siii-mir-density-ratio.pdf")

temperatures = np.linspace(4000, 12000, 200)
densities = np.linspace(0.0, 1000.0, 200)
em33 = s3.getEmissivity(temperatures, densities, 2, 1)
em18 = s3.getEmissivity(temperatures, densities, 3, 2)

fig, ax = plt.subplots(figsize=(8, 8))
cs = ax.contour(densities, temperatures, em18/em33, [0.7, 0.8, 0.9], cmap="Accent")
ax.clabel(cs)
ax.axhspan(7000, 8000, color="k", alpha=0.05)
ax.set(
    title="[S III] 18.71 $\mu$m / 33.47 $\mu$m",
    xlabel="Density, $\mathrm{cm}^{-3}$",
    ylabel="Temperature, K",    
)
fig.savefig("siii-mir-temden-contour-R08.pdf")

ax.clabel?


