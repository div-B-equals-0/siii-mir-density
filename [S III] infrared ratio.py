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


