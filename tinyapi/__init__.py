"""
    :copyright: (c) 2021 by Zaid Ali (email@xarty.xyz).
    :license: MIT, see LICENSE for more details.

    TinyAPI is a small WSGI framework for Python. It provides a simple way to implement a REST API.
    It is designed fast and easy. It is also very easy to extend. You can use custom classes.
"""

__author__ = "Zaid Ali"
__copyright__ = "Copyright (c) 2020, Zaid Ali"
__credits__ = ["Zaid Ali"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Zaid Ali"
__email__ = "email@xarty.xyz"

from .application import TinyAPI
from .exception import *
from .http import *
from .template import *
from .wrappers import *
