import typing
import re

if typing.TYPE_CHECKING:
    from tinyapi.application import TinyAPI

from tinyapi.wrappers import Request, Respone 
from tinyapi.routing import Router, ErrorRoute
from tinyapi.http import STATUS_MESSAGE
from tinyapi.utils import guess_mimi_type

from itsdangerous.url_safe import URLSafeSerializer

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
        return [self.get_isinstance(self.get_error_rule(405).callback())]

    def not_found(self, start_response: typing.Callable) -> None:
        """
            This method will return a 404 error.
        """
        start_response("404 Not Found", [("Content-Type", "text/html")])
        return [self.get_isinstance(self.get_error_rule(404).callback())]

    def no_body_found(self, start_response: typing.Callable) -> None:
        """
            This method will return a 404 error.
        """
        start_response("404 Not Found", [("Content-Type", "text/html")])
        return [b'No body returned']

    def get_rule(self, path: str) -> typing.Optional["Router"]:
        """
            This method will return the rule that matches the request.
            If the request doesn't match any rule, it will return None.
        """
        for rule in self.app.rules:
            match = re.match(rule.path, path)
            if match is not None:
                return (rule, match.groupdict())
        return (None,{})

    def get_error_rule(self, code: int) -> typing.Optional["ErrorRoute"]:
        """
            This method will return the error rule that matches the error.
            If the error doesn't match any rule, it will return None.
        """
        for rule in self.app.errors:
            if rule.code == code:
                return rule
        return None

    def get_isinstance(self, obj: typing.Any) -> typing.Any:
        """
            This method will return True if the object is an instance of the class.
            Otherwise, it will return False.
        """
        if isinstance(obj, Respone):
            return [str(obj.body).encode('utf-8')]
        return [str(obj).encode('utf-8')]

    def get_status_code(self, status_code: str) -> int:
        """
            This method will return the status code of the request.
        """
        try:
            return int(status_code.split(" ")[0])
        except ValueError:
            return None

    def get_status_message(self, status_code: int) -> str:
        """
            This method will return the status message of the request.
        """
        try:
            return f'{status_code} {STATUS_MESSAGE[int(status_code)]}'
        except KeyError:
            return 'Unknown'

    def error_handler(self, code: int, start_response: typing.Callable) -> None:
        """
            This method is the entry point of the error handler.
            It will dispatch the error to the callback of the error rule.
        """
        error_rule = self.get_error_rule(code)
        if error_rule is None:
            self.not_found(start_response)
            return [self.get_isinstance(self.get_error_rule(404).callback())]

        start_response(f"{self.get_status_message(code)}", [("Content-Type", "text/html")])
        return [self.get_isinstance(error_rule.callback())]

    def request_handler(self, callback: typing.Any, start_response: typing.Callable) -> None:
        """
            This method is the entry point of the request handler.
            It will dispatch the request to the callback of the rule.
            If the request doesn't match any rule, it will return a 404 error.
        """

        resp = self.get_isinstance(callback)

        if isinstance(callback, Respone):
            self.error_handler(callback.status_code, start_response)
            print(callback._form_header())

            start_response(callback.status_code, callback._form_header())
        else:
            mimi_type = guess_mimi_type(callback)

            start_response(f"{self.get_status_message(200)}", [("Content-Type", mimi_type)])

        return resp
    
    def __call__(self, env: typing.Dict[str,typing.Any], start_response: typing.Callable) -> None:
        """
            This method is the responsible of the request and binding the request to the callback.
        """
        global request
        request.bind(env)

        rule, match_data = self.get_rule(request.path)

        if rule is None:
            return self.not_found(404, start_response)

        if request.method not in rule.methods:
            return self.method_not_allowed(405, start_response)

        callback = rule.callback(**match_data)

        if callback is None:
            return self.no_body_found(start_response)
        
        return self.request_handler(callback, start_response)