"""
Loads the parameters of the microcircuit (Potjans & Diesmann 2014).

Returns
-------
NN : Series
    Neuron numbers
conn_probs : DataFrame
    Connection probabilities within the microcircuit
N_syn : DataFrame
    Synapse numbers within the microcircuit
p : DataFrame
    Avg. number of synapses between a pair of neurons within the microcircuit
K : DataFrame
    Indegrees within the microcircuit
K_ext : Series
    Indegrees from external populations
"""

import numpy as np
import pandas as pd

lp_multiindex = pd.MultiIndex.from_product([["II/III", "IV", "V", "VI"], ["E", "I"]], names=["layer", "population"])

# Neuron numbers
NN = pd.Series(data=[20683.0, 5834.0, 21915.0, 5479.0, 4850.0, 1065.0, 14395.0, 2948.0], index=lp_multiindex)

# Connection probabilities
conn_probs = pd.DataFrame(
    data=[
        [0.1009, 0.1689, 0.0437, 0.0818, 0.0323, 0.0, 0.0076, 0.0],
        [0.1346, 0.1371, 0.0316, 0.0515, 0.0755, 0.0, 0.0042, 0.0],
        [0.0077, 0.0059, 0.0497, 0.135, 0.0067, 0.0003, 0.0453, 0.0],
        [0.0691, 0.0029, 0.0794, 0.1597, 0.0033, 0.0, 0.1057, 0.0],
        [0.1004, 0.0622, 0.0505, 0.0057, 0.0831, 0.3726, 0.0204, 0.0],
        [0.0548, 0.0269, 0.0257, 0.0022, 0.06, 0.3158, 0.0086, 0.0],
        [0.0156, 0.0066, 0.0211, 0.0166, 0.0572, 0.0197, 0.0396, 0.2252],
        [0.0364, 0.001, 0.0034, 0.0005, 0.0277, 0.008, 0.0658, 0.1443],
    ],
    index=lp_multiindex,
    columns=lp_multiindex,
)

# Synapse numbers, compare eq. (1) in Potjans & Diesmann 2014
N_syn = np.log(1.0 - conn_probs) / np.log(1.0 - 1.0 / np.outer(NN, NN))
N_syn = np.abs(N_syn)  # Fix the appearing '-0.00000' entries

# Avg. number of synapses between a pair of neurons
p = N_syn / np.outer(NN, NN)

# Indegrees from within the microcircuit
K = N_syn.div(NN, axis=0)

# Indegrees from external populations
K_ext = pd.Series(data=[1600.0, 1500.0, 2100.0, 1900.0, 2000.0, 1900.0, 2900.0, 2100.0], index=lp_multiindex)
