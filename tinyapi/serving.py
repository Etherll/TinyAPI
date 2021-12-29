import typing
import re

if typing.TYPE_CHECKING:
    from tinyapi.application import TinyAPI

from tinyapi.wrappers import Request
from tinyapi.wrappers import Respone
from tinyapi.routing import Router

request = Request()

class Serving:
    def __init__(self, app: "TinyAPI") -> None:
        self.app: "TinyAPI" = app
        " The application that is used to serve the request. "

    def method_not_allowed(self, start_response: typing.Callable) -> None:
        """
            This method will return a 405 error.
        """
        start_response("405 Method Not Allowed", [("Content-Type", "text/html")])
        return [b"Method Not Allowed"]

    def not_found(self, start_response: typing.Callable) -> None:
        """
            This method will return a 404 error.
        """
        start_response("404 Not Found", [("Content-Type", "text/html")])
        return [b"Not Found"]

    def get_rule(self, path: str) -> typing.Optional["Router"]:
        """
            This method will return the rule that matches the request.
            If the request doesn't match any rule, it will return None.
        """
        for rule in self.app.rules:
            match = re.match(rule.path, path)
            if match is not None:
                return (rule, match.groupdict())
        return None
    
    def __call__(self, env: typing.Dict[str,typing.Any], start_response: typing.Callable) -> None:
        """
            This method is the entry point of the application.
            It will dispatch the request to the callback of the rule.
            If the request doesn't match any rule, it will return a 404 error.
        """
        global request
        request.bind(env)

        rule, match_data = self.get_rule(request.path)

        if rule is None:
            return self.not_found(start_response)

        if request.method not in rule.methods:
            return self.method_not_allowed(start_response)

        callback = rule.callback(**match_data)

        if isinstance(callback, Respone):
            start_response(callback.status, callback.__form_header())
            return [str(callback.body).encode('utf-8')]
        elif isinstance(callback, str):
            start_response("200 OK", [("Content-Type", "text/html")])
            return [callback.encode('utf-8')]