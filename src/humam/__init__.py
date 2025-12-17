from importlib import metadata

try:
    __version__ = metadata.version("humam")
except metadata.PackageNotFoundError:
    pass

del metadata

from .analysis import Analysis  # noqa: F401, E402
from .data_preprocessing.connectivity import SynapseNumbers  # noqa: F401, E402
from .data_preprocessing.cytoarchitecture import NeuronNumbers  # noqa: F401, E402
from .network import Network  # noqa: F401, E402
from .simulation import Simulation  # noqa: F401, E402
