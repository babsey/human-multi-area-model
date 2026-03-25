from importlib import metadata

try:
    __version__ = metadata.version("humam")
except metadata.PackageNotFoundError:
    pass

del metadata

from humam.analysis import Analysis  # noqa: F401, E402
from humam.data_preprocessing.connectivity import SynapseNumbers  # noqa: F401, E402
from humam.data_preprocessing.cytoarchitecture import NeuronNumbers  # noqa: F401, E402
from humam.network import Network  # noqa: F401, E402
from humam.simulation import Simulation  # noqa: F401, E402
