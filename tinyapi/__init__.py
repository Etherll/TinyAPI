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
from .extension import Extension
from .http import STATUS_MESSAGE
from .template import Renderer
from .wrappers import Request, Respone
from .serving import request
from .class_route import ClassRoute
from .exception import ExtensionNotFound

from .tools import redirect

__all__ = [
    "TinyAPI",
    "Extension",
    "STATUS_MESSAGE",
    "Renderer",
    "Request",
    "Respone",

    "request",
]