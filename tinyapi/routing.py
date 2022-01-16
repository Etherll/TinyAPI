import typing

from tinyapi.utils import format_pattern

class Router:
    """
        Router is the class that is used to create a route.
        It has a path, methods and callback.

        It represents a route. Which can be use to dispatch the callback of the request.

        Parameters
        ----------
        path : `str`
            The path of the route.
        methods : `list`
            The methods of the route.
        callback : `typing.Callable`
            The callback of the route.
    """
    def __init__(self, path: str, methods: typing.List[str], callback: typing.Callable) -> None:
        self.path: str = format_pattern(path)
        " The path of the route. "
        self.methods: typing.List[str] = methods
        " The methods of the route. "
        self.callback: typing.Callable = callback
        " The callback of the route. "

    def __repr__(self) -> str:
        return f"<Router {self.path} {self.methods}>"

class ErrorRoute:
    """
        This method is used to register a error.
        The callback is a function that will be called when the error is raised.
    """
    def __init__(self, code: int, callback: typing.Callable) -> None:
        self.code: int = code
        " The error code of the route. "
        self.callback: typing.Callable = callback
        " The callback of the route. "

    def __repr__(self) -> str:
        return f"<ErrorRoute {self.code}>"

class Routering:
    rules: typing.List["Router"] = []
    errors: typing.List["ErrorRoute"] = []

    def add_rule(self, path: str, methods: typing.List[str], func: typing.Callable) -> None:
        """
            This method adds a new rule to the router
            When the request matches the rule, the callback function will be called.

            Parameters
            ----------
            path : `str`
                The path of the request.
            method : `str`
                The method of the request.
            func : `typing.Callable`
                The callback function.
        """
        self.rules.append(
            Router(path, methods, func))

    def remove_rule(self, path: str, method: str) -> None:
        """
            This method removes a rule from the router.

            Parameters
            ----------
            path : `str`
                The path of the request.
            method : `str`
                The method of the request.
        """
        for router in self.rules:
            if router.path == path and method in router.methods:
                self.rules.remove(router)

    def get_rule(self, path: str) -> typing.Union[None, "Router"]:
        """
            This method returns the rule that matches the request.

            Parameters
            ----------
            path : `str`
                The path of the request.

        """
        for router in self.rules:
            if router.path == path:
                return router
        return None

    def add_error(self, code: int, func: typing.Callable) -> None:
        """
            This method adds a new error to the router.
            When the error is raised, the callback function will be called.

            Parameters
            ----------
            code : `int`
                The error code.
            func : `typing.Callable`
                The callback function.
        """
        self.errors.append(ErrorRoute(code, func))

    def remove_error(self, code: int) -> None:
        """
            This method removes a error from the router.

            Parameters
            ----------
            code : `int`
                The error code.
        """
        for error in self.errors:
            if error.code == code:
                self.errors.remove(error)