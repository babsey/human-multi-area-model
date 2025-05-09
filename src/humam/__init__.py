from importlib import metadata

try:
    __version__ = metadata.version("humam")
except metadata.PackageNotFoundError:
    pass

del metadata

from .network import Network
from .simulation import Simulation
from .analysis import Analysis

from .data_preprocessing.cytoarchitecture import NeuronNumbers
from .data_preprocessing.connectivity import SynapseNumbers
