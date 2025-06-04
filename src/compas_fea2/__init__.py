import os
from collections import defaultdict
from dotenv import load_dotenv
from compas.tolerance import Tolerance  # noqa: F401


__author__ = ["Francesco Ranaudo"]
__copyright__ = "COMPAS Association"
__license__ = "MIT License"
__email__ = "francesco.ranaudo@gmail.com"
__version__ = "0.3.1"


def init_fea2(verbose=False, point_overlap=True, global_tolerance=1, precision=3, part_nodes_limit=100000):
    """Create a default environment file if it doesn't exist and loads its variables.

    Parameters
    ----------
    verbose : bool, optional
        Be verbose when printing output, by default False
    point_overlap : bool, optional
        Allow two nodes to be at the same location, by default True
    global_tolerance : int, optional
        Tolerance for the model, by default 1
    precision : str, optional
        Values approximation, by default '3'.
        See `compas.tolerance.Tolerance.precision` for more information.
    part_nodes_limit : int, optional
        Limit of nodes for a part, by default 100000.
    """
    env_path = os.path.abspath(os.path.join(HERE, ".env"))
    if not os.path.exists(env_path):
        with open(env_path, "x") as f:
            f.write(
                "\n".join(
                    [
                        "VERBOSE={}".format(verbose),
                        "POINT_OVERLAP={}".format(point_overlap),
                        "GLOBAL_TOLERANCE={}".format(global_tolerance),
                        "PRECISION={}".format(precision),
                    ]
                )
            )
    load_dotenv(env_path)


# pluggable function to be
def _register_backend():
    """Create the class registry for the plugin.

    Raises
    ------
    NotImplementedError
        This function is implemented within the backend plugin implementation.
    """
    raise NotImplementedError


def set_backend(plugin):
    """Set the backend plugin to be used.

    Parameters
    ----------
    plugin : str
        Name of the plugin library. You can find some backend plugins on the
        official ``compas_fea2`` website.

    Raises
    ------
    ImportError
        If the plugin library is not found.
    """
    import importlib

    global BACKEND
    BACKEND = plugin
    try:
        importlib.import_module(plugin)._register_backend()
    except ImportError:
        print("backend plugin not found. Make sure that you have installed it before.")


def _get_backend_implementation(cls):
    return BACKENDS[BACKEND].get(cls)


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
UMAT = os.path.abspath(os.path.join(DATA, "umat"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))

if not load_dotenv():
    init_fea2()

VERBOSE = os.getenv("VERBOSE").lower() == "true"
POINT_OVERLAP = os.getenv("POINT_OVERLAP").lower() == "true"
GLOBAL_TOLERANCE = float(os.getenv("GLOBAL_TOLERANCE"))
PRECISION = int(os.getenv("PRECISION"))
BACKEND = None
BACKENDS = defaultdict(dict)

__all__ = ["HOME", "DATA", "DOCS", "TEMP"]
