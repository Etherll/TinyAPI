import typing

if typing.TYPE_CHECKING:
    from tinyapi.extension import Extension
    from tinyapi.class_route import ClassRoute

from tinyapi.serving import Serving
from tinyapi.routing import Routering
from tinyapi.exception import ExtensionNotFound

class Base(Routering):
    def rule(self, rule:str, methods: typing.List[str]) -> typing.Callable:
        """
            This method is used to register a rule.
            The rule is a regular expression that will be used to match the request.

            Parameters
            ----------
            rule: `str`
                The rule that will be used to match the request.
            methods: `typing.List[str]`
                The methods that will be used to match the request.
        """
        def decorator(func: typing.Callable) -> typing.Callable:
            self.add_rule(rule, methods, func)
            
            return func
        return decorator
    
    def error(self, code: int) -> typing.Callable:
        """
            This method is used to register a error.
            The callback is a function that will be called when the error is raised.
        """
        def decorator(func: typing.Callable) -> typing.Callable:
            self.add_error(code, func)
            return func
        return decorator

    def add_class_rule(self, route: "ClassRoute") -> None:
        """
            This method is used to add a class rule to the application.
        """
        for method in route.methods:
            self.add_rule(route.path, [method.__name__[3:].upper()], method)
            
    def class_rule(self, path: str) -> "ClassRoute":
        """
            This method is used to register a class rule.
            The class rule is a class that will be used to match the request.

            Parameters
            ----------
            path: `str`
                The path that will be used to match the request.
        """
        def decorator(cls: "ClassRoute") -> "ClassRoute":
            self.add_class_rule(cls(path))
            return cls

        return decorator

class TinyAPI(Base):
    def __init__(self, middlewares: typing.Optional[typing.List[typing.Callable]] = []) -> None:
        self.server = Serving(self)
        self.extensions: typing.List["Extension"] = []

        self.middlewares = middlewares

    def run(self, host: typing.Optional[str] = 'localhost', port: typing.Optional[int] = 5000) -> None:
        """
            This method is used to run the application.

            Parameters
            ----------
            host: `str`
                The host that will be used to run the application.
            port: `int`
                The port that will be used to run the application.
        """
        from wsgiref.simple_server import make_server

        print(f"* Running on http://{host}:{port}")
        print(f"* Use prodcution WSGI like gunicon/uwsgi to run the application in production.")
        print(f"* Use Ctrl+C to quit")

        make_server(host, port, self.server).serve_forever()

    def add_extension(self, extension: "Extension") -> None:
        """
            This method is used to add an extension to the application.
        """
        extension.app = self

        self.extensions.append(extension)

        print(f"* Extension {extension.name} added.")

    def remove_extension(self, extension_name: str) -> None:
        """
            This method is used to remove an extension from the application.
        """
        try:
            extension = [extension for extension in self.extensions if extension.name == extension_name][0]
        except IndexError:
            raise ExtensionNotFound(f"Extension {extension_name} not found.")

        for rule in extension.rules:
            self.rules.remove(rule)

        for error in extension.errors:
            self.errors.remove(error)

        self.extensions.remove(extension)

        print(f"* Extension {extension.name} removed.")

    def use(self, callable: typing.Callable) -> None:
        """
            This method is use to extend the application. With custom middleware.
        """
        resp = callable(self)
        return resp

    def __call__(self, env, start_response):
        return self.server.__call__(env, start_response)