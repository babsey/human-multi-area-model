from importlib import metadata

try:
    __version__ = metadata.version("humam")
except metadata.PackageNotFoundError:
    pass

del metadata

from .analysis import Analysis
from .data_preprocessing.connectivity import SynapseNumbers
from .data_preprocessing.cytoarchitecture import NeuronNumbers
from .network import Network
from .simulation import Simulation
